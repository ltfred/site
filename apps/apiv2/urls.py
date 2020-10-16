from django.urls import re_path, path

from apiv2.views import next_holiday, holiday, date_info

urlpatterns = [
    re_path(r"^holiday/year/$", holiday),  # 获取某年的法定假日
    re_path(r"^holiday/info/$", date_info),  # 获取某天的节假日情况
    path("holiday/next/", next_holiday),  # 获取下一个法定假日
]
