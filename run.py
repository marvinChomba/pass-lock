from password import Password
from user import User

def new_user(login,password):
    """
    This will create a new user everytime they login
    Args:
        login - user name
        password - the user's password
    """
    return User(login,password)

def add_password(account,username,password):
    """
    This is a function that will add a new password
    """
    new_pass = Password(account,username,password)
    new_pass.save_pass()

def generate_password(length):
    """
    This will create a random password for the user
    """
    return Password.generate_pass(length)

def view_passwords():
    """
    A function that will allow the user to view all the passwords
    """
    return Password.display_passwords()

def delete_password(acc):
    """
    This is a function 
    Password.delete_password(acc)
def main():
    """
    This is where the user will run all their functions
    """
    print("Welcome to PASSWORD LOCKER. We help you manage your passwords so that you can worry about things that matter\n")
    print("-"*6,"REGISTER","-"*6,"\n")

    user_name = input("User Name\n")
    user_pass = input("Password\n")

    new_user(user_name,user_pass)

    print(f"Welcome {user_name}\n")

    print("What would you like to do?\n")

    while True:
        print("You can use 'generate' to  generate a password, 'add' to add an existing password, 'del' to delete a password, 'view' to view all your passwords, 'exit' to leave :( ")


