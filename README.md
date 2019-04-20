# Simple Blog Engine

- [Начало](#начало)
- [Вход](#вход)
- [Список](#список)

---

## Начало
```
git clone https://github.com/karaname/django-blog-engine.git
cd django-blog-engine && virtualenv env && source env/bin/activate
sudo pip install -r requirements.txt

python manage.py migrate && python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser
```

## Вход
```
python manage.py runserver --insecure
http://localhost:8000
```

## Список
- Виртуальная среда, настройк (изолирование), установка пакетов
```
virtualenv env && source env/bin/activate && sudo pip install -r requirements.txt

Если нужно создать requirements.txt с модулями окружения
pip freeze > requirements.txt
```

- Настройка .gitignore

- Старт проекта (project), первая миграция
```
django-admin startproject main . && python manage.py migrate
```

- Старт приложения (app)
```
python manage.py startapp blog
```

- Импорты
```
from django.conf.urls import url, include
Добавить приложение в настройки main/settings.py
Осуществить include
```

- Возврат HttpResponse
```
from django.http import HttpResponse
return HttpResponse('Hello Web')
```

- Создание модели, миграция, создание объектов через shell
```
python manage.py shell
from blog.models import Post
post = Post.objects.create(title='Title', body='Random text')
post.save()
```

- Вывод через templates, использование for, вывод title

- Создание метода show в views.py
```
post = Post.objects.get(id=pk)
```

- Для удобства работы с терминалом вывод show_urls (django-extensions)
```
python manage.py show_urls
```

- Авторизация и условия, предоставление прав new/update/del
```
from django.contrib.auth import views as auth_views
login.html
if user.is_authenticated
LOGIN_REDIRECT_URL = '/'
```

- Создание метода new, создание формы и импорт
```
from django.forms import ModelForm
```

- Создание метода update

- Создание метода del

- Добавление @login_required

- Разбиение на классы для удобства views.py
```
from django.views.generic import TemplateView
```

- Пагинация

- Передача подзаголовка родителю {% block title %}

- Создание 404.html

- Отключение DEBUG=False

- ALLOWED_HOSTS *

- Добавление стилей {% load static %} и favicon

- Написание тестов
