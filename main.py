from bottle import route, run
import redis
import random
#    Задаем конфигурацию для подключения к базе
hostdb = 'localhost'
portdb = 6379
numberdb = 0
#    Подключаемся к базе
r = redis.StrictRedis(host=hostdb, port=portdb, db=numberdb)
#    Ф-ия для выдачи токеннов


def maketoken():
    stringForToken = 'qw'
    token = ''
#    Задаем длинну ключа
    lenKey = int(1)
#    Вычеляем возможное кол-во ключей
    lenstringForToken = int(len(stringForToken))
    y = lenstringForToken ** lenKey
#    Высчитываем оставшееся кол-во ключей
    getTokenList = int(len(r.keys("*")))
    x = y - getTokenList
    print("Ключей осталось:", x)
#    Проверяем не кончились ли ключи
    if x <= 0:
        return False
    else:
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


@route('/api/get_token_status/<token>', method='GET')
def get_token_status(token="<token>"):
    if r.hlen(token) == 0:
        print("Ключ не выдан")
    elif r.hlen(token) == 1:
        print("Ключ выдан, но не активирован")
    elif r.hlen(token) == 2:
        print("Ключ выдан и активирован")


@route('/api/del_token/<token>', method='DELETE')
def del_tokken(token="<token>"):
    r.delete(token)


@route('/api/activate_token/<name>', method='PUT')
def activate_token(token="<token>"):
    if r.hlen(token) == 0:
        print("Ключ не выдан")
    elif r.hlen(token) == 1:
        r.hset(name=token, key="activated", value="yes")
        print("Вы активировали ключ")
    elif r.hlen(token) == 2:
        print("Ключ уже активирован")


@route('/api/get_token', method='POST')
def add_token():
    token = maketoken()
    if token is False:
        print("Ключи кончились")
    else:
        r.hset(name=token, key="Token", value=token)


run(host='localhost', port=8080, debug=True)

