# api_final_yatube
### Описание
API для социальной сети публикации личных дневников Yatube
### Технологии
- Python 3.9
- Django 3.2.16
- Django REST Framework 3.12.4
### Запуск проекта в dev-режиме
- Клонируйте репозиторий и перейдите в созданную директорию
```
git clone git@github.com:ArtemKAF/api_yatube.git
cd api_yatube/
```
- Установите и активируйте виртуальное окружение
```
python3 -m venv venv
. ./venv/bin/activate - для linux
venv\Scripts\activate.bat - для Windows
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Перейдите в папку с проектом и выполните миграции
```
cd yatube_api/
python3 manage.py migrate
```
- Запустите проект:
```
python3 manage.py runserver
```
### Возможности:
По адресу http://localhost:8000/redoc/ будет доступна спецификация к API проекта.
1. Запросы для работы с публикациями:

Доступны по адресу: http://localhost:8000/api/v1/posts/

Примечание: Анонимно доступны только GET запросы, остальные требуют аутентификацию.
PUT, PATCH и DELETE доступны только автору публикации.

2. Запросы для работы с сообществами:

Доступны по адресу: http://localhost:8000/api/v1/groups/

Примечание: Проектом предусмотрен только просмотр информации о сообществах.

3. Запросы для работы с комментариями:

Доступны по адресу: http://localhost:8000/api/v1/posts/{post_id}/comments/

Примечание: Анонимно доступны только GET запросы, остальные требуют аутентификацию.
PUT, PATCH и DELETE доступны только автору комментария. Параметр post_id - идентификатор публикации.

4. Запросы для работы с подписками:

Доступны по адресу: http://localhost:8000/api/v1/follow/

Примечание: Недоступны анонимным пользователям. Редактирование и удаление подписок не предусмотрено проектом.

5. Адреса для работы с токенами:

http://localhost:8000/api/jwt/create/

http://localhost:8000/api/jwt/refresh/

http://localhost:8000/api/jwt/verify/

Примечание: Время жизни токена - 1 день. По истечении этого срока необходимо создавать новый.
Токен необходимо передавать в заголовке запроса "Authorization" в следующем виде: "Bearer {access_token}"

### License
MIT
### Авторы
Козин Артем
