import hutils
import xlrd
import os


class Holiday(object):
    def __init__(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/doc/holiday.xlsx"
        self.xlsx = xlrd.open_workbook(path)
        self.sheet = self.xlsx.sheets()[0]
        self.weekday = {1: "周一", 2: "周二", 3: "周三", 4: "周四", 5: "周五", 6: "周六", 7: "周日"}

    def get_legal_holiday(self, year: str):
        if year not in self.xlsx.sheet_names():
            return {"year": year, "message": "暂不支持该年的查询"}, -1
        sheet = self.xlsx.sheet_by_name(year)
        holiday_data = []
        for i in range(sheet.nrows):
            row_data = sheet.row_values(i)
            holiday_data.append({
                "name": row_data[0],
                "duration": row_data[1],
                "rest": row_data[2],
                "days": row_data[3]
            })
        return {"year": year, "message": holiday_data}, 0

    def get_today(self, date_str: str):
        try:
            date = hutils.str_to_date(date_str)
        except:
            return {"date": date_str, "message": "输入的日期有误"}, -1
        data, code = self.get_legal_holiday(str(date.year))
        if code == -1:
            return {"date": date, "message": "暂不支持该日期的查询"}, -1
        # 判断今天是否是法定假日
        for each in data["message"]:
            duration = each["duration"].split("~")
            start, end = duration[0], duration[1]
            start_date_str = str(date.year) + "-" + start[:2] + "-" + start[3:5]
            end_date_str = str(date.year) + "-" + end[:2] + "-" + end[3:5]
            start_date, end_date = hutils.str_to_date(start_date_str), hutils.str_to_date(end_date_str)
            if start_date <= date <= end_date:
                return {"date": date, "message": f"今天是{each['name']}呢，好好休息一下吧！"}, 0
            # 判断是否是调休日
            rest = each["rest"].split("、")
            if "无调休" not in rest:
                for each_rest in rest:
                    date_str = str(date.year) + "-" + each_rest[:2] + "-" + each_rest[3:5]
                    if date == hutils.str_to_date(date_str):
                        return {"date": date, "message": f"今天是{each['name']}的调休哦，要上班呢"}, 0
        weekday = date.weekday() + 1
        if weekday in [6, 7]:
            return {"date": date, "message": f"今天是{self.weekday[weekday]}哦，工作一周了，好好放松一下吧！"}, 0
        return {"date": date, "message": f"今天是{self.weekday[weekday]}哦，努力工作吧！"}, 0
