from django.http import JsonResponse

from tool.apis.holiday import Holiday


def holiday_api(request, year):
    try:
        data, code = Holiday().get_legal_holiday(str(year))
    except:
        return JsonResponse({"status": -1, "data": {"message": "出了点问题，请联系我"}})
    return JsonResponse({"status": code, "data": data})


def date_api(request, date):
    try:
        data, code = Holiday().get_today(str(date))
    except:
        return JsonResponse({"status": -1, "data": {"message": "出了点问题，请联系我"}})
    return JsonResponse({"status": code, "data": data})
