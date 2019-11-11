import unittest
#from functions import get_formatted_name

def get_formatted_name(first_name, last_name,middle=''):
    """Return a full formatted name"""
    if middle:
        full_name = f"{first_name} {middle} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

class NameTestCase(unittest.TestCase):
    """Test for functions.get_formatted_name"""

    def test_first_last_name(self):
        """Test if first/last name work as expected"""
        formatted_name = get_formatted_name('Stefano','Mazzone')
        self.assertEqual(formatted_name,'Stefano Mazzone')

    def test_first_middle_last_name(self):
        """Test if first/middle/last name work as expected"""
        formatted_name = get_formatted_name('wolfgang','mozart','amedeus')
        self.assertEqual(formatted_name,'Wolfgang Amedeus Mozart')


if __name__ == '__main__':
    unittest.main()