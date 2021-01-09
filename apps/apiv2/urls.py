from apiv2.views import date_info, holiday, next_holiday, today_history
from django.urls import path, re_path

urlpatterns = [
    re_path(r"^holiday/year/$", holiday),  # 获取某年的法定假日
    re_path(r"^holiday/info/$", date_info),  # 获取某天的节假日情况
    path("holiday/next/", next_holiday),  # 获取下一个法定假日
    path("todayhistory/", today_history),  # 历史上的今天数据
]
