REST API веб сервер, с использованием технологий:/n
1)Bottle python framework
2)Redis no sql BD

Для запуска сервера используется файл main.py
Для работы сервиса необходимо:
1)Коннект с redis-server
2)Установленные пакеты из requirements.txt

Конфигурацию подключения к redis-server в файле main.py

В api объявлены следующие методы:
1)GET
2)PUT
3)POST
4)DELETE

Метод POST используется для получения ключа.
Для получения ключа необходимо использовать метод POST и запрос "/api/get_token".
Пример использования метода
"http post http://localhost:8080/api/get_token"
Где "localhost" доменное имя или же ip адрес на котором запущен сервис, а ":8080" - порт.
При выполнении данного метода запустится ф-ия "add_token"
В консоль будет выведено сообщение о сгенирированном ключе, и кол-ве оставшихся ключей.
Каждый сгенированный ключ уникальный.
За генерацию ключа отвечает ф-ия "maketoken".
Кол-во возможных ключей конфигурируется 2 переменными в ф-ии "maketoken":
1)stringForToken. Данная переменная отвечает за возможные символы в ключе
2)lenKey. Данная переменная отвечает за кол-во символов в ключе

Метод PUT используется для активации ключей.
Для активации ключа необходимо использовать метод PUT и запрос "/api/activate_token/<token>",
"token" ключ который необходимо активировать.
При выполнении данного запроса запустится ф-ия "activate_token".
Пример использования метода
Для активацию ключа qwer
"http put http://localhost:8080/api/activate_token/qwer"
Где "localhost" доменное имя или же ip адрес на котором запущен сервис, а ":8080" - порт.
По результату работы данного метода в запись бд будет добавлена метка о том что ключ активирован и
в консоль выводится сообщениe:
1)"Ключ не выдан", в случае если ключ не был выдан
2)"Вы активировали ключ", в случае если ключ выдан и не был ранее активирован
3)"Ключ уже активирован", в случае если ключ уже активирован

Метод GET используется для получения информации о ключе:
1)Выдан ли ключ
2)Активирован ли ключ
Для получения данной информации необходимо использовать метод GET и запрос "/api/get_token_status/<token>",
"token" ключ который необходимо проверить.
При выполнении данного запроса запустится ф-ия "get_token_status".
Пример использования метода
Для получения информации о ключе qwer
"http put http://localhost:8080/api/activate_token/qwer"
Где "localhost" доменное имя или же ip адрес на котором запущен сервис, а ":8080" - порт.
По результату работы данного метода в консоль выводится сообщениe:
1)"Ключ не выдан", в случае если ключ не был выдан
2)"Ключ выдан, но не активирован", в случае если ключ выдан и не был активирован
3)"Ключ выдан и активирован", в случае если ключ уже активирован

Метод DELETE используется для удаления ключа.
Для удаления ключа необходимо использовать метод DELETE и запрос "/api/del_token/<token>"
"token" ключ который необходимо удалить.
При выполнении данного запроса запустится ф-ия "del_tokken".
Пример использования метода
Для удаления о ключа qwer
"http delete http://localhost:8080/api/activate_token/qwer"
Где "localhost" доменное имя или же ip адрес на котором запущен сервис, а ":8080" - порт.
По результату работы данного метода в консоль выводится сообщениe о том что вы удалили ключ и какой ключ был удален
При удалении ключа теряется информация о том был ли он активирован или же выдан, а так же позволяет сгенерировать
данный ключ заново.
