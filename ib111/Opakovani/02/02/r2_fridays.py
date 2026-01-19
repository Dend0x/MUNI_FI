from ib111 import week_02  # noqa


# Napište funkci, která spočítá počet pátků 13. v daném roce ‹year›.
# Parametr ‹day_of_week› udává den v týdnu, na který v daném roce
# padne 1. leden. Dny v týdnu mají hodnoty 0–6, počínaje pondělím
# s hodnotou 0.
#
# Přestupné roky: v některých letech se na konec února přidává 29.
# den. Jsou to roky, které jsou dělitelné čtyřmi, s výjimkou těch,
# které jsou zároveň dělitelné 100 a nedělitelné 400.


def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


def is_friday(day):
    return day == 4


def fridays(year, day_of_week):
    count = 0
    for i in range(1, 13):
        for d in range(1, days_in_month(year, i) + 1):
            if is_friday(day_of_week) and d == 13:
                count += 1
            day_of_week = (day_of_week + 1) % 7
    return count


def main():
    assert fridays(2020, 2) == 2
    assert fridays(2019, 1) == 2
    assert fridays(2018, 0) == 2
    assert fridays(2017, 6) == 2
    assert fridays(2016, 4) == 1
    assert fridays(2015, 3) == 3
    assert fridays(2012, 6) == 3
    assert fridays(2000, 5) == 1
    assert fridays(1996, 0) == 2
    assert fridays(1643, 3) == 3
    assert fridays(1501, 1) == 2


if __name__ == "__main__":
    main()
