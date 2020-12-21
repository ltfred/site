from django.urls import re_path, path

from apiv2.views import next_holiday, holiday, date_info, today_history
from photo.views import PhotoView

app_name = "photo"

urlpatterns = [
    path("", PhotoView.as_view(), name="list")
]
