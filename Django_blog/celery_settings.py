from django.conf import settings

CELERY_TIMEZONE = settings.TIME_ZONE
CELERY_ENABLE_UTC = True
CELERY_BROKER_URL = f"{settings.REDIS_URL}/1"
CELERY_RESULT_BACKEND = 'django_celery_results.backends.database.DatabaseBackend'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191
DJANGO_CELERY_RESULTS = {
    'ALLOW_EDITS': False
}