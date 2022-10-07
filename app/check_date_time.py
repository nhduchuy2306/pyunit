
def leap_year(year: int):
    if year % 400 == 0:
        return True
    if year % 100 == 0:  # 1100 1300 1500
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(year: int, month: int) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:return 28
    return 0

def is_valid_date_v2(year: int, month: int, day: int) -> bool:
    if month is None or year is None or day is None:
        return False
    if year < 1000 or year > 3000:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if day > days_in_month(year, month):
        return False
    return True

def is_valid_date(year: int, month: int, day: int) -> bool:
    if month is None or year is None or day is None:
        return False
    if year < 1000 or year > 3000:
        return False
    if month >= 1 and month <= 12:
        if day >= 1:
            if day <= days_in_month(year,month):
                return True
            return False
        return False;
    return False
