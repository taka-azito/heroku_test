import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

SECRET_KEY = 'cg)+nx_15#e+j3&d6h8v(l88!#@t$gs&mj%u2pk53cys)57x^*'