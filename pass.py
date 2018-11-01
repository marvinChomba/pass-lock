
class Password:
    """
    This is the class which we will use to create the passwords
    """
    def __init__(self,account,username,password):
        """
        This function will allow the user to create instances of the class with unique details
        """
        self.account = account
        self.username = username
        self.password = password
    