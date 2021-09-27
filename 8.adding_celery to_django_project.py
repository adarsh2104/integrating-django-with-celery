# Add the celery file to django project inside project folder.
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html



# proj/proj/celery.py
# --------- START --------------

import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# - app1/
#     - tasks.py
#     - models.py
# - app2/
#     - tasks.py
#     - models.py

# All above tasks from registered apps will be loaded.



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}') 


# --------- END --------------


# Import this into proj/proj/__init__.py:
# To ensure celery is started when djnago starts.


# ---------------- START --------------------------------
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)

# ---------------- END --------------------------------



