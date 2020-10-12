import xlrd


class Holiday(object):
    def __init__(self):
        self.xlsx = xlrd.open_workbook("../doc/holiday.xlsx")
        self.sheet = self.xlsx.sheets()[0]

    def get_legal_holiday(self):
        holiday_data = []
        for i in range(self.sheet.nrows):
            row_data = self.sheet.row_values(i)
            holiday_data.append({
                "节日名": row_data[0],
                "放假时间": row_data[1],
                "调休时间": row_data[2],
                "放假天数": row_data[3]
            })
        return holiday_data

    def get_today(self, date):
        pass


