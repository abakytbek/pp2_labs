import psycopg2
from config import load_config

def connect():
    config = load_config()
    try:
        conn = psycopg2.connect(**config)
        print("Connected to PostgreSQL")
        conn.close()
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    connect()
