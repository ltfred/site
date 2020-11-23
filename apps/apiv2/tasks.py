import datetime

from celery import shared_task

from apiv2.models import APIToken


@shared_task
def reset_token_visit_count():
    """每天定时更新token的次数"""
    APIToken.objects.filter(deactivated_at__isnull=True).update(visit_count=0, update_at=datetime.datetime.now())
