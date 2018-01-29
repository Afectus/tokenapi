import unittest
import main
import re
import redis
import config
#    Для роверки генерации токена
#    не забываем поднять базу

#    Конфигурация для тестовой базы
#    Задаем хост базы
hostbd = 'localhost'
#    Задаем порт базы
portbd = 6370
#    Задаем номер базы
numberbd = 0

#   Переинциализируем переменную дял конекта к базе


class TestToken(unittest.TestCase):
    main.bdcon = redis.StrictRedis(host=hostbd, port=portbd, db=numberbd)

    def test_add_token(self):
        token = main.add_token()
        self.assertTrue(main.bdcon.hlen(token["key:"]) == 1)

    def test_activate_token(self):
        token = main.add_token()
        activtoken = main.activate_token(token["key:"])
        self.assertTrue(main.bdcon.hlen(token["key:"]) == 2)

    def test_get_token_status_active(self):
        token = main.add_token()
        activtoken = main.activate_token(token["key:"])
        keystatus = {"keystatus:": "Ключ не выдан"}
        self.assertEqual(main.get_token_status(activtoken), keystatus)


if __name__ == '__main__':
    unittest.main()

