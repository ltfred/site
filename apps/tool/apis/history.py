import datetime

import requests

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "izone.settings")
django.setup()

from django.conf import settings


class History(object):
    def __init__(self):
        self.base_url = "https://api.jisuapi.com/todayhistory/query"
        self.app_key = settings.JI_SU_APP_KEY

    def get_data(self):
        date = datetime.datetime.today().date()
        month, day = date.month, date.day
        url = self.base_url + f"?appkey={self.app_key}&month={month}&day={day}"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise
            data = response.json()["result"]
        except:
            data = []
        history_data = []
        for each_data in data:
            history_data.append({
                "title": each_data["title"],
                "date": each_data["year"] + "-" + each_data["month"] + "-" + each_data["day"],
            })
        return history_data[::-1]
