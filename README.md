# 📝 Todo List API — Django REST Framework

Todo List API — Django REST Framework asosida ishlab chiqilgan, **Token Based Authentication** qo'llanilgan, CRUD funksionallikka ega backend xizmati.

Foydalanuvchilar avval ro‘yxatdan o‘tishi yoki login qilishi kerak. Har bir foydalanuvchi o‘zining todo ro‘yxatini boshqaradi.

---------------------------------------------------------------------------

## 🚀 Texnologiyalar

-Python 3.x
-Django 4.x
-Django REST Framework
-SQLite / PostgreSQL
------------------------------------------------------------------------

## 📦 O'rnatish

### 1. Repo ni clone qilish

``` bash
git clone https://github.com/username/todo-api.git
cd todo-api
```

### 2. Virtual ortam yaratish

``` bash
python -m venv venv
source venv/bin/activate      # Mac / Linux
venv\Scripts\activate       # Windows
```

### 3. Kutubxonalarni o'rnatish

``` bash
pip install -r requirements.txt
```

### 4. Migratsiya qilish

``` bash
python manage.py migrate
```

### 5. Serverni ishga tushirish

``` bash
python manage.py runserver
```

API:

http://127.0.0.1:8000/api/
------------------------------------------------------------------------
🔐 Authentication (Token Based)

Login yoki Registratsiyadan so‘ng foydalanuvchi Token oladi.
Har bir so‘rovga quyidagicha header qo‘shish shart:

Authorization: Token <token>

🔑Auth API Endpoints

| Method | URL                   | Tavsif               |
| ------ | --------------------- | -------------------- |
| POST   | `/api/auth/register/` | Ro‘yxatdan o‘tish    |
| POST   | `/api/auth/login/`    | Login va Token olish |
| POST   | `/api/auth/logout/`   | Tokenni bekor qilish |

------------------------------------------------------------------------

## 📌 API Endpoints

  | Method  | URL                       | Tavsif                       |
  |------=--|--------------------------|------------------------------|
  | GET     | `/api/todos/`            | Barcha todo larni olish      |
  | POST    | `/api/todos/`            | Yangi todo yaratish          |
  | GET     | `/api/todos/<id>/`       | Bitta todo olish             |
  | PUT     | `/api/todos/<id>/`       | To'liq yangilash             |
  | PATCH   | `/api/todos/<id>/`       | Qisman yangilash             |
  | DELETE  | `/api/todos/<id>/`       | O'chirish                    |


------------------------------------------------------------------------

## 🗂 Model (models.py)

``` python
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

------------------------------------------------------------------------

## 🛠 Serializer (serializers.py)

``` python
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
```

------------------------------------------------------------------------

