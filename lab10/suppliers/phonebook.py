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
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created.\n")

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
            cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV upload complete.\n")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Record added/updated.\n")

def search_pattern():
    pattern = input("Enter search pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_records(%s);", (pattern,))
    rows = cur.fetchall()

    print("\nResults:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()
    print()

def pagination():
    limit = int(input("Enter LIMIT: "))
    offset = int(input("Enter OFFSET: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    print("\nPage results:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()
    print()

def insert_many():
    n = int(input("How many users to add? "))

    names = []
    phones = []

    for _ in range(n):
        names.append(input("Name: "))
        phones.append(input("Phone: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM insert_many_users(%s, %s);", (names, phones))
    bad = cur.fetchone()[0]

    print("\nIncorrect phone numbers:", bad)

    conn.commit()
    cur.close()
    conn.close()
    print()

def delete_record():
    print("Delete:")
    print("1. By name")
    print("2. By phone")

    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("CALL delete_user(%s, NULL);", (name,))
    else:
        phone = input("Enter phone: ")
        cur.execute("CALL delete_user(NULL, %s);", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Record deleted.\n")

def menu():
    while True:
        print("\nPHONEBOOK SYSTEM (SQL procedures/functions)")
        print("1. Create table")
        print("2. Load data from CSV")
        print("3. Insert or update user")
        print("4. Insert many users")
        print("5. Search records")
        print("6. Pagination")
        print("7. Delete record")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("phonebook.csv")
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            insert_many()
        elif choice == "5":
            search_pattern()
        elif choice == "6":
            pagination()
        elif choice == "7":
            delete_record()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    menu()
