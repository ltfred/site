from django.contrib import admin
from photo.models import Photo, PhotoCategory


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    ordering = ("-created_at",)


@admin.register(PhotoCategory)
class PhotoCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("-created_at",)
