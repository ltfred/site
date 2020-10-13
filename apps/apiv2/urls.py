from django.urls import re_path

from apiv2.views import holiday_api, date_api

urlpatterns = [
    re_path(r"^holiday/year/(?P<year>\d+)/$", holiday_api),
    re_path(r"^holiday/info/(?P<date>.*)/$", date_api)
]