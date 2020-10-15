import datetime

import hutils
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from tool.apis.holiday import Holiday


class HolidayView(APIView):

    @staticmethod
    def get(request):
        year = request.query_params.get("year", datetime.datetime.now().year)
        try:
            data, code = Holiday().get_legal_holiday(str(year))
        except:
            return Response({"status": -1, "data": {"message": "出了点问题，请联系我"}})
        return Response({"status": code, "data": data})


class DateView(APIView):

    @staticmethod
    def get(request):
        date = request.query_params.get("date", datetime.date.today())
        try:
            data, code = Holiday().get_today(str(date))
        except:
            return Response({"status": -1, "data": {"message": "出了点问题，请联系我"}})
        return Response({"status": code, "data": data})


def next_holiday(request):
    """获取下一个法定节假日"""
    date = datetime.date.today()
    data, code = Holiday().get_legal_holiday(str(date.year))
    holiday_list = data["message"]
    for holiday in holiday_list:
        duration = holiday["duration"].split("~")
        start, end = duration[0], duration[1]
        start_date_str = str(date.year) + "-" + start[:2] + "-" + start[3:5]
        end_date_str = str(date.year) + "-" + end[:2] + "-" + end[3:5]
        start_date, end_date = hutils.str_to_date(start_date_str), hutils.str_to_date(end_date_str)
        if date < start_date:
            return JsonResponse(
                {
                    "status": 0,
                    "data": {
                        "duration": holiday["duration"],
                        "message": f"下一个节假日是{holiday['name']}, 距离今天还有{(start_date - date).days}"
                    }
                }
            )