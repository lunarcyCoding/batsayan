import json

def load_users():
    try:
        with open("user_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open("user_data.json", "w") as file:
        json.dump(users, file, indent=None)

def add_user(username,password,email,phone):
    users=load_users()
    users.append({"username":username,"password":password,"email":email,"phone":phone})
    save_users(users)
    print("User added successfully!")
    
def remove_user(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            users.remove(user)
            print("User removed successfully!")
            return
    print("User not found!")
    
def forgot_password(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            print(f"vertification code sent to ********{user['phone'][-2:]}.")
            code = int(input("Enter the verification code:"))
            if code == 696720:
                new_password = input("Enter new password:")
                user["password"] = new_password
                save_users(users)
                print("Password updated successfully!")
            else:
                print("Invalid verification code!")
    return

def login(username,password):
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful!")
            return True
    print("Invalid username or password!")
    return False