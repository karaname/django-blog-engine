# Simple Blog Engine

- [Начало](#начало)
- [Вход](#вход)

---

## Начало
```
git clone https://github.com/karaname/django-blog-engine.git
cd django-blog-engine && virtualenv env && source .env/bin/activate
sudo pip install -r requirements.txt
```
```
vim main/settings.py
changes ↓
DEBUG = True
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
