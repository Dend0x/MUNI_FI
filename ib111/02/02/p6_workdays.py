from ib111 import week_02  # noqa


# Napište funkci, která zjistí, kolik bude pracovních dnů v roce
# ‹year›. Dny v týdnu mají hodnoty 0–6 počínaje pondělím s hodnotou 0.
# Předpokládejte, že ‹year› je větší než 1600.

# České státní svátky jsou:
#
# │  datum │ svátek                                         │
# ├┄┄┄┄┄┄┄▻┼◅┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
# │   1.1. │ Den obnovy samostatného českého státu          │
# │      — │ Velký pátek                                    │
# │      — │ Velikonoční pondělí                            │
# │   1.5. │ Svátek práce                                   │
# │   8.5. │ Den vítězství                                  │
# │   5.7. │ Den slovanských věrozvěstů Cyrila a Metoděje   │
# │   6.7. │ Den upálení mistra Jana Husa                   │
# │  28.9. │ Den české státnosti                            │
# │ 28.10. │ Den vzniku samostatného československého státu │
# │ 17.11. │ Den boje za svobodu a demokracii               │
# │ 24.12. │ Štědrý den                                     │
# │ 25.12. │ 1. svátek vánoční                              │
# │ 26.12. │ 2. svátek vánoční                              │

# Přestupné roky: v některých letech se na konec února přidává 29.
# den. Jsou to roky, které jsou dělitelné čtyřmi, s výjimkou těch,
# které jsou zároveň dělitelné 100 a nedělitelné 400.

# Čistou funkci ‹first_day› můžete použít k tomu, abyste zjistili,
# na který den v týdnu padne 1. leden daného roku. Např.
# ‹first_day(2001)› vrátí nulu, protože rok 2001 začínal pondělím.


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def first_day(year):
    assert 1601 <= year
    years = year - 1601
    offset = years + years // 4 - years // 100 + years // 400
    return offset % 7


def set_all_workdays(year):
    first_day_year = first_day(year)
    if not is_leap(year):
        if first_day_year < 5:
            return 261
        return 260

    if first_day_year == 5:
        return 260
    if first_day_year < 4:
        return 262
    return 261


def is_weekend(day, year):
    test_day = (first_day(year) + day) % 7
    return test_day >= 5


def check_holiday(workdays_count, day, year):
    return workdays_count - (not is_weekend(day, year))


def workdays(year):
    workdays_count = set_all_workdays(year)
    leap = is_leap(year)

    # DOSCS
    workdays_count = check_holiday(workdays_count, 0, year)
    # SP
    workdays_count = check_holiday(workdays_count, 120 + leap, year)
    # DV
    workdays_count = check_holiday(workdays_count, 127 + leap, year)
    # DSVCAM
    workdays_count = check_holiday(workdays_count, 185 + leap, year)
    # DUJH
    workdays_count = check_holiday(workdays_count, 186 + leap, year)
    # DCS
    workdays_count = check_holiday(workdays_count, 270 + leap, year)
    # DVSCS
    workdays_count = check_holiday(workdays_count, 300 + leap, year)
    # DBZSAD
    workdays_count = check_holiday(workdays_count, 320 + leap, year)
    # SD
    workdays_count = check_holiday(workdays_count, 357 + leap, year)
    # PSV
    workdays_count = check_holiday(workdays_count, 358 + leap, year)
    # DSV
    workdays_count = check_holiday(workdays_count, 359 + leap, year)

    return workdays_count - 2


def main():
    assert workdays(2020) == 251
    assert workdays(2021) == 252
    assert workdays(2016) == 252
    assert workdays(2004) == 253
    assert workdays(1993) == 252
    assert workdays(1991) == 251
    assert workdays(1990) == 250
    assert workdays(1900) == 250
    assert workdays(2000) == 250
    assert workdays(1996) == 252


if __name__ == "__main__":
    main()
