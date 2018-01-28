import unittest
import main
import re

text = 'abcdfghijk'

parser = re.search('a[b-f]*f')
print(parser.group()) # 'abcdf'


a = main.add_token()
class TestToken(unittest.TestCase):


    def test_maketoken(self):
       self.assertFalse(a)


if __name__ == '__main__':
    unittest.main()
