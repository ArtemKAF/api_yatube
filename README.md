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
git clone git@github.com:ArtemKAF/api_final_yatube.git
cd api_final_yatube/
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
1. Запросы для работы с публикациями:

| Тип                                | Запрос                                                             |
|------------------------------------|--------------------------------------------------------------------|
| GET                                | http://localhost:8000/api/v1/posts/                                |
| GET                                | http://localhost:8000/api/v1/posts/?limit={number}&offset={number} |
| GET, POST,<br/> PUT, PATCH, DELETE | http://localhost:8000/api/v1/posts/{pk}/                           |

Примечание: Анонимно доступны только GET запросы, остальные требуют аутентификацию.
PUT, PATCH и DELETE доступны только автору публикации. 

Поля для POST запроса:

| Имя   | Тип     | Требования |
|-------|---------|------------|
| text  | string  | required   |
| image | string  | binary     |
| group | integer |            |

2. Запросы для работы с сообществами:

| Тип  | Запрос                                    |
|------|-------------------------------------------|
| GET  | http://localhost:8000/api/v1/groups/      |
| GET  | http://localhost:8000/api/v1/groups/{pk}/ |

Примечание: Проектом предусмотрен только просмотр информации о сообществах.

3. Запросы для работы с комментариями:

| Тип                                | Запрос                                                      |
|------------------------------------|-------------------------------------------------------------|
| GET                                | http://localhost:8000/api/v1/posts/{post_id}/comments/      |
| GET, POST,<br/> PUT, PATCH, DELETE | http://localhost:8000/api/v1/posts/{post_id}/comments/{pk}/ |

Примечание: Анонимно доступны только GET запросы, остальные требуют аутентификацию.
PUT, PATCH и DELETE доступны только автору комментария. Параметр post_id - идентификатор публикации.

Поля для POST запроса:

| Имя   | Тип     | Требования |
|-------|---------|------------|
| text  | string  | required   |

4. Запросы для работы с подписками:

| Тип                           | Запрос                                                 |
|-------------------------------|--------------------------------------------------------|
| GET, POST                     | http://localhost:8000/api/v1/follow/                   |
| GET                           | http://localhost:8000/api/v1/follow/?search={username} |

Примечание: Недоступны анонимным пользователям. Редактирование и удаление подписок не предусмотрено проектом.

Поля для POST запроса:

| Имя       | Тип     | Требования |
|-----------|---------|------------|
| following | string  | required   |

5. Запросы для работы с токенами:

| Тип    | Запрос                                 |
|--------|----------------------------------------|
| POST   | http://localhost:8000/api/jwt/create/  |
| POST   | http://localhost:8000/api/jwt/refresh/ |
| POST   | http://localhost:8000/api/jwt/verify/  |

Примечание: Время жизни токена - 1 день. По истечении этого срока необходимо создавать новый.
Токен необходимо передавать в заголовке запроса "Authorization" в следующем виде: "Bearer {access_token}"

Поля для POST запроса создания токена:

| Имя      | Тип     | Требования |
|----------|---------|------------|
| username | string  | required   |
| password | string  | required   |

Поля для POST запроса обновления токена:

| Имя     | Тип     | Требования |
|---------|---------|------------|
| refresh | string  | required   |

Поля для POST запроса проверки токена:

| Имя   | Тип     | Требования |
|-------|---------|------------|
| token | string  | required   |

### License
MIT
### Авторы
Козин Артем
