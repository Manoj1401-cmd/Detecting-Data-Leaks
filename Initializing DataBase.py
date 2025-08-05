import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a simple users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert sample users
c.executemany('INSERT INTO users (username, password) VALUES (?, ?)', [
    ('Manoj', 'Son123'),
    ('Raja', 'father456'),
    ('sunitha', 'sunitha789')
])

conn.commit()
conn.close()
print("Database initialized.")

