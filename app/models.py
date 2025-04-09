import sqlite3
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0,1))
        )
    ''')
    conn.commit()
    conn.close()