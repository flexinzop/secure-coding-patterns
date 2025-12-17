import sqlite3

def login_vulnerable(username, password):
    # Simulating a database connection
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'sup3rd4mns3cr3t')")

    # VULNERABILITY (CWE-89):
    # Direct concatenation of user input into the SQL command string.
    # If the user sends "admin' --" or other valid username, the query becomes:
    # SELECT * FROM users WHERE username = 'admin' --' AND password = '...'
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"[LOG] Executing Query: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    
    conn.close()
    return user

# Simulation of an attack
# The attacker bypasses the password check completely
print("--- Vulnerable Execution ---")
user = login_vulnerable("admin' --", "anything")
if user:
    print("✅ Login Successful (Logged as Admin via SQLi!)")
else:
    print("❌ Login Failed")