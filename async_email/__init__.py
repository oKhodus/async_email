from __future__ import absolute_import, unicode_literals

# Это гарантирует, что Celery будет использовать наш app при запуске
from .celery_config import app as celery_app

__all__ = ('celery_app',)
