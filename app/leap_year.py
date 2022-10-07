
def leap_year(year: int):
    if year % 400 == 0:
        return True
    if year % 100 == 0: #1100 1300 1500
        return False
    if year % 4 == 0: 
        return True
    return False


if __name__ == '__main__':
    year = int(input('Năm:'))
    print(leap_year(year))