import sqlite3

def create_table():

    conn = sqlite3.connect("ats.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_name TEXT,
        score REAL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_result(resume_name, score):

    conn = sqlite3.connect("ats.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history(resume_name, score) VALUES (?, ?)",
        (resume_name, score)
    )

    conn.commit()
    conn.close()


def get_history():

    conn = sqlite3.connect("ats.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM history ORDER BY id DESC"
    )

    data = cursor.fetchall()

    conn.close()

    return data