def secure_login(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Safe query using placeholders
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    c.execute(query, (username, password))
    result = c.fetchall()
    conn.close()

    return result
