# tasks/utils.py
from datetime import date, timedelta

def get_days_in_month(year, month):
    next_month = month % 12 + 1
    next_year = year + (month // 12)
    return (date(next_year, next_month, 1) - timedelta(days=1)).day

def get_month_name(month):
    return date(1, month, 1).strftime("%B")

from datetime import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def init_month(year, month):
    if month == 2:
        num_days = 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        num_days = 30
    else:
        num_days = 31

    y = year - (14 - month) // 12
    m1 = month + 12 * ((14 - month) // 12) - 2
    start_day = (1 + y + y // 4 - y // 100 + y // 400 + (31 * m1) // 12) % 7

    return num_days, start_day

