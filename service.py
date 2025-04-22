from utils import match_password
from database import cursor

def login_page(username,password):
    try:
        with open("logged_in_users.txt", "r") as f:
            logged_users = f.read().splitlines()
    except Exception:
        logged_users = []

    if username in logged_users:
        print("You are already logged in")
        return True
    
    query = "SELECT id, username, password, role FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()


    if user:
        user_id, db_username, db_password, role = user
        if match_password(password, db_password):
            print(f"You are succelsfully login  ed. Role: {role}")

            with open("logged_in_users.txt", "a") as f:
                f.write(username + "\n")

            return True
        else:
            print("Incorrect password")

        return True
    else:
        print("User not found")
        return False
