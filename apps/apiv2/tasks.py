from celery import shared_task

from apiv2.models import APIToken


@shared_task
def reset_token_visit_count():
    APIToken.objects.filter(deactivated_at__isnull=True).update(visit_count=0)
