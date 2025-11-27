import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS user_profile (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            level INT DEFAULT 1
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INT REFERENCES user_profile(id),
            score INT,
            state TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        )
        """
    )

    cfg = load_config()
    conn = psycopg2.connect(**cfg)
    cur = conn.cursor()

    for command in commands:
        cur.execute(command)

    conn.commit()
    cur.close()
    conn.close()
    print("Tables are created")

if __name__ == "__main__":
    create_tables()
