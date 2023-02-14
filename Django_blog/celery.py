from celery import Celery
import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
app = Celery('myblog')
app.now = timezone.now

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()