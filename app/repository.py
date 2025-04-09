import sqlite3
from app.models import Task

def get_connection():
    return sqlite3.connect('todo.db')

def add_task(title: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title, completed) VALUES (?, 0)", (title,))
    conn.commit()
    conn.close()

def list_tasks():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, title, completed FROM tasks")
    rows = c.fetchall()
    conn.close()
    return [Task(id=row[0], title=row[1], completed=bool(row[2])) for row in rows]

def complete_task(task_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()