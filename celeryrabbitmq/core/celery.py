from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

"""
nombre de la instancia de celery 'core'
"""
app = Celery("core")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
