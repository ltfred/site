import datetime
import os

import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "izone.settings")

from django.conf import settings
from django.core.cache import cache


class JiSu(object):
    def __init__(self):
        self.history_url = "https://api.jisuapi.com/todayhistory/query"
        self.phone_url = "https://api.jisuapi.com/shouji/query"
        self.history_cache_key = "history" + datetime.datetime.today().strftime("%m%d")
        self.app_key = settings.JI_SU_APP_KEY

    def get_history_data(self):
        """获取历史上的今天数据"""
        history_data = cache.get(self.history_cache_key)
        if not history_data:
            date = datetime.date.today()
            month, day = date.month, date.day
            url = self.history_url + f"?appkey={self.app_key}&month={month}&day={day}"
            try:
                response = requests.get(url)
                if response.json()["status"] != 0:
                    raise
            except:
                return -1, []
            data = response.json()["result"]
            history_data = []
            for each_data in data:
                history_data.append(
                    {
                        "date": each_data["year"] + "-" + each_data["month"] + "-" + each_data["day"],
                        "title": each_data["title"],
                    }
                )
            cache.set(self.history_cache_key, history_data, 60 * 60 * 24)
        return 0, history_data[::-1]

    def get_phone(self, phone):
        """获取手机号归属地数据"""
        url = self.phone_url + f"?appkey={self.app_key}&shouji={phone}"
        response = requests.get(url)
        data = response.json()
        if data["status"] != 0:
            return {"msg": data["msg"], "result": {}, "status": data["status"]}
        return {"msg": data["msg"], "result": data["result"], "status": 200}
