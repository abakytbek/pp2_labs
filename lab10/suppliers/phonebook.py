import psycopg2
from config import load_config
import csv

def get_connection():
    params = load_config()
    return psycopg2.connect(**params)

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✔️ Таблица phonebook создана (или уже существует).")

def insert_from_csv(path):
    conn = get_connection()
    cur = conn.cursor()

    with open(path, "r") as file:
        reader = csv.reader(file)
        next(reader)  

        for name, phone in reader:
            cur.execute("""
                INSERT INTO phonebook(first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("✔️ Данные из CSV загружены.")


def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO phonebook(first_name, phone)
        VALUES (%s, %s)
        ON CONFLICT (phone) DO NOTHING;
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Запись добавлена.")


def update_record():
    search_phone = input("Введите телефон пользователя, которого хотите изменить: ")

    new_name = input("Новое имя (нажмите Enter, если менять не нужно): ")
    new_phone = input("Новый телефон (Enter, если менять не нужно): ")

    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute("""
            UPDATE phonebook
            SET first_name = %s
            WHERE phone = %s;
        """, (new_name, search_phone))

    if new_phone:
        cur.execute("""
            UPDATE phonebook
            SET phone = %s
            WHERE phone = %s;
        """, (new_phone, search_phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Данные обновлены.")


def query_data():
    print("\nФильтр поиска:")
    print("1 — телефон начинается с …")
    print("2 — имя равно …")
    print("3 — показать всех")

    choice = input("Ваш выбор: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        prefix = input("Начинается с: ")
        cur.execute("""
            SELECT first_name, phone
            FROM phonebook
            WHERE phone LIKE %s;
        """, (prefix + "%",))

    elif choice == "2":
        name = input("Введите имя: ")
        cur.execute("""
            SELECT first_name, phone
            FROM phonebook
            WHERE first_name = %s;
        """, (name,))

    else:
        cur.execute("SELECT first_name, phone FROM phonebook;")

    rows = cur.fetchall()

    print("\n---- Результаты ----")
    for r in rows:
        print(f"{r[0]} — {r[1]}")

    cur.close()
    conn.close()


def delete_record():
    print("Удалить по:")
    print("1 — имени")
    print("2 — телефону")

    choice = input("Ваш выбор: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Введите имя: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))
    else:
        phone = input("Введите телефон: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("✔️ Запись удалена.")


def menu():
    while True:
        print("\n===== PHONEBOOK =====")
        print("1 — Создать таблицу")
        print("2 — Загрузить данные из CSV")
        print("3 — Добавить запись вручную")
        print("4 — Обновить данные")
        print("5 — Поиск")
        print("6 — Удалить запись")
        print("0 — Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("phonebook.csv")
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_record()
        elif choice == "5":
            query_data()
        elif choice == "6":
            delete_record()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    menu()
