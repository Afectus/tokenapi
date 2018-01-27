from bottle import route, run
import redis
import random
#    Задаем конфигурацию для подключения к базе
#    Задаем хост базы
hostdb = 'localhost'
#    Задаем порт базы
portdb = 6379
#    Задаем номер базы
numberdb = 0
#    Подключаемся к базе
r = redis.StrictRedis(host=hostdb, port=portdb, db=numberdb)
#    Ф-ия для выдачи токеннов

#    Задаем Возможные символы в ключе
stringForToken = 'qw'
#    Задаем длинну ключа
lenKey = int(1)


#    Высчитываем оставшееся кол-во ключей
def get_number_token():
    lenstringForToken = int(len(stringForToken))
    y = lenstringForToken ** lenKey
    getTokenList = int(len(r.keys("*")))
    x = y - getTokenList
    return x


def maketoken():
    number_key = get_number_token()
#    Проверяем не кончились ли ключи
    if number_key <= 0:
        return False
    else:
        token = ''
        while token == '':
            for x in range(lenKey):
                randomKeyGenerate = random.choice(stringForToken)
                token = token + randomKeyGenerate
#    Переменная для проверки получившегося ключа на предмет повторения
                a = r.hlen(token)
            if a != 0:
                token = ''
            else:
                return token

#    Объявлем методы и делаем ссылки


@route('/api/get_token', method='POST')
def add_token():
    token = maketoken()
    if token is False:
        print("Ключи кончились")
    else:
        r.hset(name=token, key="Token", value=token)
        print("Вы получили ключ:", token)
        print ("Ключей осталось:", get_number_token())


@route('/api/activate_token/<token>', method='PUT')
def activate_token(token="<token>"):
    if r.hlen(token) == 0:
        print("Ключ не выдан")
    elif r.hlen(token) == 1:
        r.hset(name=token, key="activated", value="yes")
        print("Вы активировали ключ", token)
    elif r.hlen(token) == 2:
        print("Ключ уже активирован")


@route('/api/get_token_status/<token>', method='GET')
def get_token_status(token="<token>"):
    if r.hlen(token) == 0:
        print("Ключ не выдан")
    elif r.hlen(token) == 1:
        print("Ключ выдан, но не активирован")
    elif r.hlen(token) == 2:
        print("Ключ выдан и активирован")


@route('/api/get_number_token', method='GET')
def print_number_token():
	print ("Ключей осталось:", get_number_token())

run(host='localhost', port=8080, debug=True)

