from django.conf import settings
from django.contrib import admin

from .models import ToolCategory, ToolLink

# Register your models here.
if settings.TOOL_FLAG:

    @admin.register(ToolLink)
    class ToolLinkAdmin(admin.ModelAdmin):
        list_display = ("name", "description", "link", "order_num", "category")

        list_filter = ("category",)

    @admin.register(ToolCategory)
    class ToolCategoryAdmin(admin.ModelAdmin):
        list_display = ("name", "order_num")
