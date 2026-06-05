import sqlite3
from datetime import datetime, timedelta
date = (datetime.utcnow() + timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
first_name TEXT,
last_name TEXT,
email TEXT PRIMARY KEY,
password TEXT,
profile_pic TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
email TEXT,
image_path TEXT,
disease TEXT,
confidence REAL,
predictions TEXT,
date DATETIME 
)
""")

conn.commit()