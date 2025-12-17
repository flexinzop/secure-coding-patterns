# SQL Injection (CWE-89)

## 🔍 Context
SQL Injection occurs when untrusted user input is directly concatenated into a database query string. This allows an attacker to manipulate the query structure, potentially accessing, modifying, or deleting unauthorized data.

## 🚩 Root Cause Analysis
In `vulnerable.py`, the application uses Python f-strings to build the SQL command:
```python
query = f"SELECT * FROM users WHERE username = '{username}'..."
```

## Attention

We cannot rely on regex alone to sanitize the username and password. Sanitization is complex. You would have to predict all the character combinations that the database interprets.

### Example:
```python
re.sub(r"--|'", "", value)
```
