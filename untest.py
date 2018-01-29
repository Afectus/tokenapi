import unittest
import main
import re

#    Для роверки генерации токена
#    не забываем поднять базу


class TestToken(unittest.TestCase):

    def test_add_token(self):
        token = main.add_token()
        self.assertTrue(main.bdcon.hlen(token["key:"]) == 1)


if __name__ == '__main__':
    unittest.main()
