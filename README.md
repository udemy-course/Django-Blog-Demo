# Django Demo

This is Django Blog Demo

## How to Set up?

### 1. Clone source code

```
$ git clone https://github.com/udemy-course/Django-Blog-Demo
```

### 2. Create a virtual environments

```
$ python -m venv django
$ source django/bin/activate
$ cd Django-Blog-Demo

```


### 3. Install requirements


```
$ pip install -r requirements.txt
```

### 4. Configure database

In the setting.py, change the database configuration as your environment.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 5. Database Migration

```
$ python manage.py migrate
```

### 6. Running the application

```
$ python manage.py runserver
```