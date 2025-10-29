from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eshop.settings')

app = Celery('Eshop')
app.config_from_object('django.conf:settings', namespace='CELERY')

# This line automatically discovers tasks in all INSTALLED_APPS
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
