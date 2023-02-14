import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv("POSTGRES_HOST", "app-postgres"),
        'PORT': os.getenv("POSTGRES_PORT", "5432"),
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD")
    }
}

REDIS_CONF = {
    "host": os.getenv("REDIS_HOST", "app-redis"),
    "port": os.getenv("REDIS_PORT", "6379")
}
REDIS_URL = f'redis://{REDIS_CONF["host"]}:{REDIS_CONF["port"]}'

CACHES = {
    "default": {
        "VERSION": 1,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{REDIS_URL}/0",
    }
}

DEBUG = False

ALLOWED_HOSTS = ['*']

# 这里替换成你上线后的域名或者服务器公网IP
SITE_URL = 'https://oneisall.top'

# 生产环境下真实发送邮件
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
