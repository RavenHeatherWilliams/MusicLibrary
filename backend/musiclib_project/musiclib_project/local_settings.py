# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-utk&h)^dvq=5-v=6-p13pgd6+kgyyu!6&e9!4o*4$3ad7rs*dd'
# SECURITY WARNING: don't run with debug turned on in production!


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'musiclib_database',
        'HOST': 'sww',
        'USER': 'sww',
        'PASSWORD': 'test'
    }
}


