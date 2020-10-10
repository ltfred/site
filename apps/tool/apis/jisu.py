import datetime

import requests

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "izone.settings")
django.setup()

from django.conf import settings


class JiSu(object):
    def __init__(self):
        self.history_url = "https://api.jisuapi.com/todayhistory/query"
        self.phone_url = "https://api.jisuapi.com/shouji/query"
        self.app_key = settings.JI_SU_APP_KEY

    def get_history_data(self):
        date = datetime.datetime.today().date()
        month, day = date.month, date.day
        url = self.history_url + f"?appkey={self.app_key}&month={month}&day={day}"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise
            data = response.json()["result"]
        except:
            data = []
        history_data = []
        for each_data in data:
            history_data.append(
                {
                    "title": each_data["title"],
                    "date": each_data["year"]
                    + "-"
                    + each_data["month"]
                    + "-"
                    + each_data["day"],
                }
            )
        return history_data[::-1]

    def get_phone(self, phone):
        url = self.phone_url + f"?appkey={self.app_key}&shouji={phone}"
        response = requests.get(url)
        data = response.json()
        if data["status"] != 0:
            return {"msg": data["msg"], "result": {}, "status": data["status"]}
        return {"msg": data["msg"], "result": data["result"], "status": 200}