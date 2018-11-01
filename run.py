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
    This is a function that will delete the password
    Args:
        acc - the acc of the pass the user wants to delete
    """
    Password.delete_password(acc)

def password_exists(acc):
    return Password.password_exist(acc)

    
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
        command = input("You can use 'generate' to  generate a password, 'add' to add an existing password, 'del' to delete a password, 'view' to view all your passwords, 'exit' to leave :( \n")
        if command == "add":
            print("Oh cool. I love new passwords\n")
            acc = input("Which platform is the password for?\n")
            u_name = input("What is your username?\n")
            password = input("What is your password?\n")

            add_password(acc,u_name,password)

            print(f"New password for {acc} added")
        elif command == "generate":
            print("I love generating password for you!")
            acc = input("Which platform is the password for?\n")
            u_name = input("What is your username?\n")
            length = input("What is the length of the password you would like me to generate\n")
            add_password(acc,u_name,generate_password(int(length)))
            print(f"New password for {acc} generated")
        elif command == "del":
            print("Oh no!:(\n")
            acc= input("Which account would you like to delete their password?\n")
            if password_exists(acc):
                delete_password(acc)
                print(f"{acc} password deleted")
            else:
                print("Password doesn't exist")
        elif command == "view":
            pass_word = input("Enter your password")
            if view_passwords():
                for password in view_passwords():
                    print("-"*6,view_passwords().index(password)+1,"-"*6,"\n")
                    print(f"Account --> {password.account}\n")
                    print(f"Username --> {password.username}\n")
                    print(f"Password --> {password.password}\n")
            else:
                print("You have no passwords")
        elif command == "exit":
            print("Please stay")
            break

if __name__ == "__main__":
    main()




