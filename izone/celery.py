from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'izone.settings')

app = Celery('izone', broker='redis://localhost:6379/0', backend='redis://localhost')

app.config_from_object('django.conf:settings', namespace='CELERY')

# 下面的设置就是关于调度器beat的设置
app.conf.beat_schedule ={
        'reset': {
            'task': 'apiv2.tasks.reset_token_visit_count',
            'schedule': crontab(hour=0),  # 每天零点将访问次数重置
        },
}
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
