import unittest
from password import Password

class TestPass(unittest.TestCase):
    """
    This is the class where we will perform all our tests
    """
    def setUp(self):
        """
        This function will create a new instance of Password
        """
        self. new_password = Password("Facebook","marvin-j","kkk")
    
    def tearDown(self):
        Password.passwords = []

    def test_new_pass(self):
        """
        This will test whether a new password is added correcly
        """
        self.assertEqual(self.new_password.account,"Facebook")
        self.assertEqual(self.new_password.username,"marvin-j")
        self.assertEqual(self.new_password.password,"kkk")

    def test_save_pass(self): 
        """
        This will check whether the new password is added to the passwords list
        """
        self.new_password.save_pass()
        self.assertEqual(len(Password.passwords),1)
    
    def test_generate_password(self):
        """
        Will check whether the generated password has the user's required length
        """
        self.assertEqual(len(Password.generate_pass(9)),9)

    def test_add_generated_pass(self):
        """
        This will check whether the new pass will be added to the passwords list
        """
        new_pass = Password("Twitter","mck",Password.generate_pass(9))
        new_pass.save_pass()
        self.assertEqual(len(Password.passwords),1)

    def test_display_pass(self):
        self.new_password.save_pass()
        new_pass = Password("Twitter","mck",Password.generate_pass(9))
        new_pass.save_pass()
        self.assertEqual(len(Password.passwords),len(Password.display_passwords()))

    def test_delete(self):
        self.new_password.save_pass()
        new_pass = Password("Twitter","mck",Password.generate_pass(8))
        new_pass.save_pass()
        Password.delete_password("facebook")
        self.assertEqual(len(Password.passwords),1)

    def test_pass_exist(self):
        self.new_password.save_pass()
        self.assertTrue(Password.password_exist("Facebook"))
if __name__ == "__main__":
    unittest.main()