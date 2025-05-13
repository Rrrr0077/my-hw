import sqlite3
from datetime import datetime

import sqlite3
from datetime import datetime

def create_tables():
    try:
        with sqlite3.connect("kfc.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT,
                    phone_number TEXT,
                    reg_date TEXT,
                    location TEXT
                );
            ''')
            conn.commit()
        print("Таблицы успешно созданы!")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблиц: {e}")

def add_user(user_id, name, phone_number):
    try:
        with sqlite3.connect("kfc.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO users (user_id, name, phone_number, reg_date)
                VALUES (?, ?, ?, ?)
            ''', (user_id, name, phone_number, datetime.now()))
            conn.commit()
        print("Пользователь добавлен в базу данных!")
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении пользователя: {e}")

def update_location(user_id, location):
    try:
        with sqlite3.connect("kfc.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users SET location = ? WHERE user_id = ?
            ''', (location, user_id))
            conn.commit()
        print("Локация обновлена!")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении локации: {e}")
