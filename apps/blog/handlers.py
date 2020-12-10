from django.db.models.signals import post_save

from .models import FriendLink
from .tasks import sync_send_mail
from izone.settings import DEFAULT_FROM_EMAIL


def email_notify_handler(sender, instance, created, **kwargs):
    email = instance.email
    print(1111111111)
    if created and email:
        print(1111111111)
        subject = message = "友链申请成功"
        html_message = f"网站名称：{instance.name}<br>网站地址：{instance.address}<br>网站简介：{instance.desc}<br>邮箱：{email}"
        sync_send_mail.delay(subject, message, DEFAULT_FROM_EMAIL, email, html_message=html_message)


post_save.connect(email_notify_handler, sender=FriendLink)