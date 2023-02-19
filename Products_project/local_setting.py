# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b=wf(&$jy9f4=%4j4&nq&cn(3=1l2yt(h2tf9l8!k^*t0c#%tb'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password10'
    }
}
