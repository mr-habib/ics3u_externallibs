from main import *
import datetime


def test_calc_days_until_future():
    today = datetime.date.today()
    wft = today + datetime.timedelta(days=7)
    date_string = f"{wft.month}/{wft.day}/{wft.year}"
    assert(calc_days_until(date_string) == 7)


def test_calc_days_until_future_2():
    today = datetime.date.today()
    wft = today + datetime.timedelta(weeks=10)
    date_string = f"{wft.month}/{wft.day}/{wft.year}"
    assert(calc_days_until(date_string) == 70)


def test_calc_days_until_past():
    today = datetime.date.today()
    wft = today - datetime.timedelta(days=5)
    date_string = f"{wft.month}/{wft.day}/{wft.year}"
    assert(calc_days_until(date_string) == -1)

def test_calc_days_until_today():
    today = datetime.date.today()
    date_string = f"{today.month}/{today.day}/{today.year}"
    assert(calc_days_until(date_string) == 0)


