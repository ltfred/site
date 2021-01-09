# Register your models here.
from apiv2.models import APIToken
from django.contrib import admin


@admin.register(APIToken)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("token", "max_count", "visit_count")
