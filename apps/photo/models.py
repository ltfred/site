from django.db import models


class Photo(models.Model):
    """照片"""
    name = models.CharField(max_length=50, verbose_name="名称")
    description = models.CharField(max_length=100, verbose_name="描述")
    url = models.URLField(verbose_name="照片地址")
    category = models.ForeignKey("PhotoCategory", on_delete=models.PROTECT, verbose_name="分类")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "照片"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class PhotoCategory(models.Model):
    """照片分类"""
    name = models.CharField(max_length=50, verbose_name="名称")
    description = models.CharField(max_length=100, verbose_name="相册描述")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "照片分类"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
