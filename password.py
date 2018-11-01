
class Password:
    """
    This is the class which we will use to create the passwords
    """
    passwords = []
    def __init__(self,account,username,password):
        """
        This function will allow the user to create instances of the class with unique details
        """
        self.account = account
        self.username = username
        self.password = password

    def save_pass(self):
        """
        This is a function that will add the user's password into the passwords array
        """
        Password.passwords.append(self)

        

    