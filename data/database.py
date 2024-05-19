import sqlite3

def init_db():
    conn = sqlite3.connect('bot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, user_id INTEGER, message TEXT)''')
    conn.commit()
    return conn, c

def check_user(conn, c, message):
    c.execute('INSERT INTO users (username) VALUES (?)', (message.from_user.username,))
    conn.commit()
