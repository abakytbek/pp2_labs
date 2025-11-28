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
    print("Tables are created")

def insert_from_csv(path):
    conn = get_connection()
    cur = conn.cursor()

    with open(path, "r") as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            if len(row) < 2:
                continue
            name, phone = row

            cur.execute("""
                INSERT INTO phonebook(first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV data uploaded")


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

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
    print("Added")


def update_record():
    search_phone = input("Enter phone that u need to change: ")

    new_name = input("New name: ")
    new_phone = input("New phone: ")

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
    print("Data updated")


def query_data():
    print("\nSearch:")
    print("1.phone started with:")
    print("2.name:")
    print("3.show all")

    choice = input("Your choice: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        prefix = input("Start with: ")
        cur.execute("""
            SELECT first_name, phone
            FROM phonebook
            WHERE phone LIKE %s;
        """, (prefix + "%",))

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute("""
            SELECT first_name, phone
            FROM phonebook
            WHERE first_name = %s;
        """, (name,))

    else:
        cur.execute("SELECT first_name, phone FROM phonebook;")

    rows = cur.fetchall()

    print("\nResults")
    for r in rows:
        print(f"{r[0]} — {r[1]}")

    cur.close()
    conn.close()


def delete_record():
    print("Delete by:")
    print("1.name")
    print("2.phone")

    choice = input("Your choice: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))
    else:
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted")


def menu():
    while True:
        print("\nPHONEBOOK")
        print("1.Create table")
        print("2.Load data from CSV")
        print("3.Add record")
        print("4.Update record")
        print("5.Search")
        print("6.Delete record")
        print("0.Exit")

        choice = input("Choose an option: ")

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
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()
