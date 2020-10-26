import datetime

import hutils
from django.http import JsonResponse
from tool.apis.holiday import Holiday
from utils.common import split_date_duration, generate_response_data


def holiday(request):
    """获取某年的法定节假日"""
    year = request.GET.get("year", datetime.date.today().year)
    try:
        data, code = Holiday().get_legal_holiday(str(year))
    except:
        return JsonResponse({"status": -1, "data": {"message": "出了点问题，请联系我"}})
    return JsonResponse({"status": code, "data": data})


def date_info(request):
    """查询某日期的节假日信息"""
    date_str = request.GET.get("date", hutils.date_to_str(datetime.date.today()))
    try:
        data, code = Holiday().get_today(date_str)
    except:
        return JsonResponse({"status": -1, "data": {"message": "出了点问题，请联系我"}})
    return JsonResponse({"status": code, "data": data})


def next_holiday(request):
    """获取下一个法定节假日"""
    # 没传日期事默认为今天
    date = datetime.date.today()
    date_str = request.GET.get("date", None)
    if date_str:
        try:
            date = hutils.str_to_date(date_str)
        except:
            return JsonResponse({"status": -1, "data": {"message": "暂不支持该年的查询或输入的格式不正确"}})
    data, code = Holiday().get_legal_holiday(str(date.year))
    holiday_list: list = data["message"]
    holiday_count = len(holiday_list)
    for holiday_info in holiday_list:
        holiday_index = holiday_list.index(holiday_info)
        start_date, end_date = split_date_duration(holiday_info["duration"], str(date.today().year))
        if date < start_date:
            response_data = generate_response_data(start_date, date, holiday_info)
            return JsonResponse(response_data)
        if holiday_index + 1 >= holiday_count:
            # 今年没有假期了，尝试获取下一年的假期
            try:
                next_year_data, code = Holiday().get_legal_holiday(str(date.today().year + 1))
            except:
                # 没有获取到下一年的假期，直接返回
                return JsonResponse({"status": 0, "data": {"message": "今年没有假期了哦"}})
            next_year_holiday_list: list = next_year_data["message"]
            next_start_date, next_end_date = split_date_duration(
                next_year_holiday_list[0]["duration"], str(date.today().year + 1)
            )
            response_data = generate_response_data(next_start_date, date, next_year_holiday_list[0])
            return JsonResponse(response_data)
        next_holiday_info = holiday_list[holiday_index + 1]
        next_start_date, next_end_date = split_date_duration(
            next_holiday_info["duration"], str(date.today().year)
        )
        if (start_date <= date <= end_date) or (end_date < date < next_start_date):
            response_data = generate_response_data(next_start_date, date, next_holiday_info)
            return JsonResponse(response_data)
