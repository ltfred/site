from django.db import models


class APIToken(models.Model):

    token = models.CharField(max_length=12, unique=True, help_text="访问token")
    max_count = models.IntegerField(default=0, help_text="限制访问次数")
    visit_count = models.IntegerField(default=0, help_text="每日访问次数")
    deactivated_at = models.DateTimeField(null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    class Meta:
        verbose_name = "密钥"
        verbose_name_plural = verbose_name
        ordering = ["-create_at"]
