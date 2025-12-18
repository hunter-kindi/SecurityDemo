import sqlite3

def get_user_status_insecure(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Insecure: User input is concatenated directly into the query string
    query = "SELECT status FROM users WHERE username = '" + username + "'"

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            print(f"Status for {username}: {result[0]}")
        else:
            print(f"User {username} not found.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# An attacker could use this input to bypass the login or extract data OK
# Example attack string: "' OR '1'='1"
# The resulting query would be: "SELECT status FROM users WHERE username = '' OR '1'='1'"
