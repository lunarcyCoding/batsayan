from user_handle import add_user, remove_user, forgot_password, login
import json
def load_users():
    try:
        with open("user_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return

users= load_users()

def existing_user(username, users):
    for user in users:
        if user["username"] == username:
            return True
    return False

print(f"Welcome to the User Management System!")

username= input("Enter username:")

if not existing_user(username, users):
    print("opening new account...")
    p=input("Enter password: ")
    e=input("Enter email: ")
    ph=input("Enter phone number: ")
    add_user(username,p,e,ph)
elif existing_user(username, users):
    password = input("Enter password: ")
    
    for user in users:
        if password != user["password"]:

            forgot_password(username)
        else:
            if login(username, password):
                print("Welcome back!")
            else:
                print("Invalid password!")
else:
    print("Invalid username!")
    exit()