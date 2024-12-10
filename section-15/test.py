import unittest                 
import main 

# define class that inherits from unittest.TestCase
class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
        
    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))                     #checks if a result is an instance of value error 
        
        
        
    def test_do_stuff2(self):
        test_param = None
        result = main.do_stuff(test_param)   
        self.assertEqual(result, 'Please enter number')
        
unittest.main()
        
        
        
# Expected Failures:

# do_stuff('shkshks') will raise a TypeError, not a ValueError. To make the test work as written, you would need to catch the TypeError within do_stuff and raise a ValueError instead.
# Best Practices:

# Tests should clearly define the input and expected outcome. If expecting an exception, modify do_stuff to handle invalid input more explicitly.