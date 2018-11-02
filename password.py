from random import randint
class Password:
    """
    This is the class which we will use to create the passwords
    """
    passwords = [] # a list which will store all the user's passwords
    def __init__(self,account,username,password):
        """
        This function will allow the user to create instances of the class with unique details in each instance
        """
        self.account = account
        self.username = username
        self.password = password

    def save_pass(self):
        """
        This is a function that will add the user's password into the passwords array
        """
        Password.passwords.append(self)

    def generate_pass(length):
        """
        This function will generate a new and random pass for the user
        Args:
            length - the length of the password
        Return:
            a random password of specified length
        """
        items = ["a","b","c","d","e","k","n","q","p","v","x","z","1","2","4","5","7","8","0"]
        new_pass = ""
        while(len(new_pass) < length):
            item = items[randint(0,len(items) -1)]
            new_pass += item
        return new_pass

    @classmethod
    def display_passwords(cls):
        """
        This function will return all the passwords in the list
        """
        return cls.passwords
     
    @classmethod
    def delete_password(cls,account):
        """
        This function will delete the user's password from the passwords list
        Args:
            account - this is the account of the password the user ants to delete
        """
        for password in cls.passwords:
            if password.account.lower() == account.lower():
                cls.passwords.remove(password)
    
    @classmethod
    def password_exist(cls,acc):
        """
        This function will check whether a password exists
        Args:
         Acc- this is the account that the user wants to confirm its password
        Return:
            True or False
        """
        for password in cls.passwords:
            if password.account.lower() == acc.lower():
                return True
        return False