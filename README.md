# Simple Blog Engine

- [Начало](#начало)
- [Вход](#вход)

---

## Начало
```
git clone https://github.com/karaname/django-blog-engine.git
cd django-blog-engine && virtualenv env && source env/bin/activate
sudo pip install -r requirements.txt
```
```
nano main/settings.py
changes ↓
ALLOWED_HOST = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
```
python manage.py migrate && python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser
```

## Вход
```
python manage.py runserver --insecure
http://localhost:8000
```
