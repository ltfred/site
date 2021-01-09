from apiv2.views import date_info, holiday, next_holiday, today_history
from django.urls import path, re_path
from photo.views import PhotoView

app_name = "photo"

urlpatterns = [path("", PhotoView.as_view(), name="list")]
