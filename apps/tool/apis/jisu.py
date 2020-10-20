import datetime
import logging

import requests

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "izone.settings")

from django.conf import settings

logger = logging.getLogger("log")


class JiSu(object):
    def __init__(self):
        self.history_url = "https://api.jisuapi.com/todayhistory/query"
        self.phone_url = "https://api.jisuapi.com/shouji/query"
        self.app_key = settings.JI_SU_APP_KEY

    def get_history_data(self):
        """获取历史上的今天数据"""
        date = datetime.date.today()
        month, day = date.month, date.day
        url = self.history_url + f"?appkey={self.app_key}&month={month}&day={day}"
        try:
            response = requests.get(url)
            if response.json()["status"] != 0:
                raise
        except Exception as e:
            logger.error("JiSu:get_history_data:" + str(e))
            return -1, []
        data = response.json()["result"]
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
        return 0, history_data[::-1]

    def get_phone(self, phone):
        """获取手机号归属地数据"""
        url = self.phone_url + f"?appkey={self.app_key}&shouji={phone}"
        response = requests.get(url)
        data = response.json()
        if data["status"] != 0:
            return {"msg": data["msg"], "result": {}, "status": data["status"]}
        return {"msg": data["msg"], "result": data["result"], "status": 200}
