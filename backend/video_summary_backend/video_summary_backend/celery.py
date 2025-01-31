# video_summary_backend/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_summary_backend.settings')

# Define the Celery application
app = Celery('video_summary_backend')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in all applications included in INSTALLED_APPS
app.autodiscover_tasks()
