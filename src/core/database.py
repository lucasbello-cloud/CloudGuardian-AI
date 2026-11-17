import sqlite3


def connect_db():
    return sqlite3.connect("data/audits.db")


def init_db():
    connection = connect_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS audits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL,
            classification TEXT NOT NULL,
            total_risks INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_audit(score, classification, total_risks):
    connection = connect_db()

    connection.execute("""
        INSERT INTO audits (score, classification, total_risks)
        VALUES (?, ?, ?)
    """, (score, classification, total_risks))

    connection.commit()
    connection.close()
def get_audits():
    connection = connect_db()

    cursor = connection.execute("""
        SELECT id, score, classification, total_risks, created_at
        FROM audits
        ORDER BY id DESC
    """)

    audits = cursor.fetchall()
    connection.close()

    return audits
