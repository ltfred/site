import os

import hutils
import xlrd
from utils.common import split_date_duration


class Holiday(object):
    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/doc/holiday.xlsx"
        self.xlsx = xlrd.open_workbook(path)
        self.weekday = {1: "周一", 2: "周二", 3: "周三", 4: "周四", 5: "周五", 6: "周六", 7: "周日"}

    def get_legal_holiday(self, year: str) -> (dict, int):
        if year not in self.xlsx.sheet_names():
            return {"message": "暂不支持该年的查询或输入的格式不正确"}, -1
        sheet = self.xlsx.sheet_by_name(year)
        holiday_data = []
        for i in range(sheet.nrows):
            row_data = sheet.row_values(i)
            start_date, end_date = split_date_duration(row_data[1], year)
            holiday_data.append(
                {
                    "name": row_data[0],
                    "date": start_date,
                    "duration": row_data[1],
                    "rest": row_data[2],
                    "days": row_data[3],
                }
            )
        return {"year": year, "message": holiday_data}, 0

    def get_today(self, date_str: str) -> (dict, int):
        try:
            date = hutils.str_to_date(date_str)
        except:
            return {"message": "暂不支持该日期的查询或输入的日期格式有误"}, -1
        data, code = self.get_legal_holiday(str(date.year))
        if code == -1:
            return {"message": "暂不支持该日期的查询或输入的日期格式有误"}, -1
        for each in data["message"]:
            start_date, end_date = split_date_duration(each["duration"], str(date.year))
            # 判断今天是否是法定假日
            if start_date <= date <= end_date:
                return {"date": date, "message": f"今天是{each['name']}呢，好好休息一下吧！"}, 0
            # 判断是否是调休日
            rest = each["rest"].split("、")
            if "无调休" not in rest:
                for each_rest in rest:
                    date_str = str(date.year) + "-" + each_rest[:2] + "-" + each_rest[3:5]
                    if date == hutils.str_to_date(date_str):
                        return {"date": date, "message": f"今天是{each['name']}的调休哦，要上班呢"}, 0
        # 不是法定假日或者调休，判断是否为周末
        weekday = date.weekday() + 1
        if weekday in [6, 7]:
            return {"date": date, "message": f"今天是{self.weekday[weekday]}哦，工作一周了，好好放松一下吧！"}, 0
        return {"date": date, "message": f"今天是{self.weekday[weekday]}哦，努力工作吧！"}, 0
