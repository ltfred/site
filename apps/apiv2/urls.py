from django.urls import re_path

from apiv2.views import HolidayView, DateView

urlpatterns = [
    re_path(r"^holiday/year/(?P<year>\d+)/$", HolidayView.as_view()),
    re_path(r"^holiday/info/(?P<date>.*)/$", DateView.as_view())
]