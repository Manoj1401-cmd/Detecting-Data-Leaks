import sqlite3

def vulnerable_login(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Vulnerable SQL query – susceptible to injection!
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("🔎 Executing query:", query)

    c.execute(query)
    result = c.fetchall()
    conn.close()

    return result

# Simulated user input
# Injection: ' OR '1'='1
username = "Manoj"
password = "' OR '1'='1"

if vulnerable_login(username, password):
    print("🚨 Access Granted – Data Leak Possible!")
else:
    print("⛔ Access Denied")
