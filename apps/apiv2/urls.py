from django.urls import re_path, path

from apiv2.views import HolidayView, DateView

urlpatterns = [
    re_path(r"^holiday/year/$", HolidayView.as_view()),  # 获取某年的法定假日
    re_path(r"^holiday/info/$", DateView.as_view()),  # 获取某天的节假日情况
    path("holiday/next/"),  # 获取下一个法定假日
]