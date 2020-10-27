import datetime

import hutils
from django.http import JsonResponse

from apiv2.models import APIToken


def split_date_duration(duration: str, year: str) -> (datetime.date, datetime.date):
    """
    将放假区间转为对应的date
    @param duration: 节假日放假区间
    @param year: 年
    @return:
    """
    duration = duration.split("~")
    start, end = duration[0], duration[1]
    start_date_str = year + "-" + start[:2] + "-" + start[3:5]
    end_date_str = year + "-" + end[:2] + "-" + end[3:5]
    start_date, end_date = hutils.str_to_date(start_date_str), hutils.str_to_date(end_date_str)
    return start_date, end_date


def generate_response_data(start_date, date, holiday):
    """
    生成下一节假日返回数据
    @param start_date: 节假日开始时间
    @param date: 查询的时间
    @param holiday: 节假日信息
    @return:
    """
    return {
        "status": 0,
        "data": {
            "date": start_date,
            "duration": holiday["duration"],
            "rest": holiday["rest"],
            "days": holiday["days"],
            "message": f"下一个节假日是{holiday['name']}, 距离今天还有{(start_date - date).days}天",
        }
    }


def token_verify(func):
    def wrapper(request):
        token = request.GET.get("token", "")
        if not token:
            return JsonResponse({"status": -1, "data": {"message": "请传入token"}})
        token: APIToken = APIToken.objects.filter(token=token, deactivated_at__isnull=True).first()
        if not token:
            return JsonResponse({"status": -1, "data": {"message": "无效的token"}})
        if token.max_count < token.visit_count and token.max_count != 0:
            return JsonResponse({"status": -1, "data": {"message": "当日没有访问次数了"}})
        token.visit_count += 1
        token.save(update_fields=['visit_count'])
        return func(request)
    return wrapper

