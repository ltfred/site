from django.urls import re_path, path

from apiv2.views import HolidayView, DateView

urlpatterns = [
    re_path(r"^holiday/year/$", HolidayView.as_view()),
    re_path(r"^holiday/info/$", DateView.as_view())
]