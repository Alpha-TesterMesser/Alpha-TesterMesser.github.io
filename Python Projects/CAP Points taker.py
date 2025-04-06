import sqlite3
from datetime import datetime

def get_user_input():
    username = input("Enter username: ").strip()
    while not username:
        print("Username cannot be empty.")
        username = input("Enter username: ").strip()

    try:
        points = int(input("Enter points: ").strip())
    except ValueError:
        print("Points must be a number. Try again.")
        return get_user_input()

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not validate_date_format(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return get_user_input()

    return username, points, date

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def save_to_db(username, points, date):
    conn = sqlite3.connect("userdata.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            points INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    cursor.execute('INSERT INTO users (username, points, date) VALUES (?, ?, ?)',
                   (username, points, date))
    
    conn.commit()
    conn.close()
    print("✅ Data saved to userdata.db")

def main():
    username, points, date = get_user_input()
    save_to_db(username, points, date)

if __name__ == "__main__":
    main()
