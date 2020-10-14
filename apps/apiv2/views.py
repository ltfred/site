import datetime

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
        date = request.query_params.get("date", datetime.datetime.now().date())
        try:
            data, code = Holiday().get_today(str(date))
        except:
            return Response({"status": -1, "data": {"message": "出了点问题，请联系我"}})
        return Response({"status": code, "data": data})
