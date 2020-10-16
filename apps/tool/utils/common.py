import datetime

import hutils


def split_date_duration(duration: str, date: datetime.date) -> (datetime.date, datetime.date):
    duration = duration.split("~")
    start, end = duration[0], duration[1]
    start_date_str = str(date.year) + "-" + start[:2] + "-" + start[3:5]
    end_date_str = str(date.year) + "-" + end[:2] + "-" + end[3:5]
    start_date, end_date = hutils.str_to_date(start_date_str), hutils.str_to_date(end_date_str)
    return start_date, end_date
