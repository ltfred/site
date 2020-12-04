from celery import shared_task
from django.core.mail import send_mail


@shared_task
def sync_send_mail(subject, message, from_user, to_user, html_message):
    """异步发送邮件"""
    send_mail(subject, message, from_user, [to_user], html_message=html_message)
