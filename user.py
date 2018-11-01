
class User:
    """
    This is a class that will contain all the details of the user
    """
    def __init__(self,login,password):
        """
        This will create unique details for each instance of the User class
        """
        self.login = login
        self.password = password

    def user_exists(self,password):
        """
        This will use the password to authenticate the user before showing the passwords
        Args:
            The user's password
        Return:
            boolean
        """
        if self.password == password:
            return True
        return False

