from bottle import route, run
import redis
import random
import config


#    Подключаемся к базе
bdcon = redis.StrictRedis(host=config.host, port=config.port, db=config.number)


def get_number_token():
    lenstringForToken = len(config.stringForToken)
    y = lenstringForToken ** config.lenKey
    getTokenList = int(len(bdcon.keys("*")))
    x = y - getTokenList
    return x

#    Ф-ия для выдачи токеннов


def maketoken():
    number_key = get_number_token()
#    Проверяем не кончились ли ключи
    if number_key <= 0:
        return False
    else:
        token = ''
        while token == '':
            for x in range(config.lenKey):
                randomKeyGenerate = random.choice(config.stringForToken)
                token = token + randomKeyGenerate
#    Переменная для проверки получившегося ключа на предмет повторения
            a = bdcon.hlen(token)
            if a != 0:
                token = ''
            else:
                return token

#    Объявлем методы


@route('/api/get_token', method='POST')
def add_token():
    token = maketoken()
    if token is False:
        return {"keystatus:": "Ключи кончились"}
    else:
        bdcon.hset(name=token, key="Token", value=token)
        return {"key:": token, "leftkeys:": get_number_token()}


@route('/api/activate_token/<token>', method='PUT')
def activate_token(token="<token>"):
    if bdcon.hlen(token) == 0:
        return {"keystatus:": "Ключ не выдан"}
    elif bdcon.hlen(token) == 1:
        bdcon.hset(name=token, key="activated", value="yes")
        return {"keystatus:": "Вы активировали ключ " + token}
    elif bdcon.hlen(token) == 2:
        return {"keystatus:": "Ключ уже активирован"}


@route('/api/get_token_status/<token>', method='GET')
def get_token_status(token="<token>"):
    if bdcon.hlen(token) == 0:
        return {"keystatus:": "Ключ не выдан"}
    elif bdcon.hlen(token) == 1:
        return {"keystatus:": "Ключ выдан, но не активирован"}
    elif bdcon.hlen(token) == 2:
        return {"keystatus:": "Ключ выдан и активирован"}


@route('/api/get_number_token', method='GET')
def print_number_token():
    return {"leftkeys:": get_number_token()}


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
