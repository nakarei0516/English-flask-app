import sqlite3

DATABASE = 'db/wordbook.db'

def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = connect_db()
    with open("schema.sql", mode="r", encoding="utf-8") as f:
        db.executescript(f.read())
    db.commit()
