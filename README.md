# lagoontest

Проект являет собой тестовое задание, представлен в качестве примера. REST Api, на базе DRF, 

**Что включено?**

* REST (web api), на базе DRF
* Регистрация, авторизация, аутентификация (в т.ч. по токену)
* CRUD - модели
* OpenAPI документация на базе swagger/redoc 

## Базовая архитектура

* Python 3.7
* Django 3.0
* Django Rest Framework 3.11
* Swagger/Redoc
* и т.д. ... 

Все зависимости прописаны в фаилах Pipfile и req.txt
 
```
git clone https://github.com/beatum/lagoontest.git && cd $_
```
## Установка зависимостей

Создайте виртуальное окружение и установите зависимости
```
pipenv install или pip install req.txt
```

## Миграции, суперюзер, запуск

Миграции
```
./manage.py migrate 
```
Суперюзер
```
./manage.py createsuperuser 
```
Запуск
```
./manage.py runserver 
```
