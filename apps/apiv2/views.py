import datetime

import hutils
from django.http import JsonResponse

from tool.apis.holiday import Holiday
from tool.utils.common import split_date_duration


def holiday(request):
    year = request.query_params.get("year", datetime.datetime.now().year)
    try:
        data, code = Holiday().get_legal_holiday(str(year))
    except:
        return JsonResponse({"status": -1, "data": {"message": "出了点问题，请联系我"}})
    return JsonResponse({"status": code, "data": data})


def date_info(request):
    date = request.query_params.get("date", datetime.date.today())
    try:
        data, code = Holiday().get_today(str(date))
    except:
        return JsonResponse({"status": -1, "data": {"message": "出了点问题，请联系我"}})
    return JsonResponse({"status": code, "data": data})


def next_holiday(request):
    """获取下一个法定节假日"""
    date = datetime.date.today()
    date_str = request.GET.get("date", None)
    if date_str:
        date = hutils.str_to_date(date_str)
    data, code = Holiday().get_legal_holiday(str(date.year))
    holiday_list: list = data["message"]
    holiday_count = len(holiday_list)
    for holiday_info in holiday_list:
        holiday_index = holiday_list.index(holiday_info)
        start_date, end_date = split_date_duration(holiday_info["duration"], date)
        response_data = {"status": 0}
        if date < start_date:
            response_data["data"] = {
                "duration": holiday_info["duration"],
                "rest": holiday_info["rest"],
                "days": holiday_info["days"],
                "message": f"下一个节假日是{holiday_info['name']}, 距离今天还有{(start_date - date).days}天"
            }
            return JsonResponse(response_data)
        if holiday_index + 1 >= holiday_count:
            response_data["data"] = {"message": "今年没有假期了呢"}
            return JsonResponse(response_data)
        next_holiday_info = holiday_list[holiday_index + 1]
        next_start_date, next_end_date = split_date_duration(next_holiday_info["duration"], date)
        if start_date <= date <= end_date and end_date < date < next_start_date:
            response_data["data"] = {
                "duration": next_holiday_info["duration"],
                "rest": next_holiday_info["rest"],
                "days": next_holiday_info["days"],
                "message": f"下一个节假日是{next_holiday_info['name']}, 距离今天还有{(next_start_date - date).days}天"
            }
            return JsonResponse(response_data)
