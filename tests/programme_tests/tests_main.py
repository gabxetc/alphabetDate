import unittest
from io import StringIO
import Source
import Dates
import Programme

class MyMainTestCase(unittest.TestCase):
    #This test ensures that a user is succesfully registered and added to the database
    def test_registerUser(self):
        pass
    
    #This test ensures that the user can successfully login
    def test_loginUser(self):
        pass

    #This test ensures that the user can successfully logout
    def test_logoutUser(self):
        pass

    #This test ensures that a user can successfully be removed from the database
    def test_removeUser(self):
        pass

if __name__ == '__main__':
    unittest.main()