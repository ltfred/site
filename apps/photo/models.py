from django.db import models


class Photo(models.Model):
    """照片"""
    name = models.CharField(max_length=50, verbose_name="名称")
    description = models.CharField(max_length=100, verbose_name="描述")
    url = models.URLField(verbose_name="照片地址")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "照片"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
