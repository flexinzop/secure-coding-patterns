import sqlite3

def login_secure(username, password):
    conn = sqlite3.connect(':memory')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'sup3rd4mns3cr3t')")

    # REMEDIATION
    # Using Parameterized queries/placeholders
    # The database treats the input strictly as data, never as executable code
    # Even if the input contains some sort of SQL syntax like ("admin' --"), it is neutralized
    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    # The parameters are passed as a separate tuple argument
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    conn.close()
    return user

# Simulation using the same attack attempt
print("--- Secure Execution ---")
user = login_secure("admin' --", "anything")
if user:
    print("✅ Login Successful")
else:
    print("❌ Login Failed (Attack mitigated)")