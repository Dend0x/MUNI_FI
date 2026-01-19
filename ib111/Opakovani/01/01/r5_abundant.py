from ib111 import week_01  # noqa
from math import isqrt


# † Napište predikát ‹is_abundant›, který je pravdivý, pokud je
# kladné celé číslo ‹number› abundantní, t.j. je menší, než součet
# jeho vlastních dělitelů.
#
# Za vlastní dělitele čísla považujeme všechny jeho kladné
# dělitele s výjimkou čísla samotného; např. vlastní dělitelé
# čísla 12 jsou 1, 2, 3, 4, 6.

def is_abundant(number):
    dividors = 1

    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            dividors += i
            dividors += number // i
            if isqrt(number) == number // i:
                dividors -= number // i

    return number < dividors




def main():
    assert is_abundant(12)
    assert is_abundant(18)
    assert is_abundant(20)
    assert is_abundant(24)
    assert is_abundant(36)
    assert is_abundant(100)
    assert is_abundant(120)

    assert not is_abundant(7)
    assert not is_abundant(15)
    assert not is_abundant(55)
    assert not is_abundant(62)
    assert not is_abundant(130)


if __name__ == "__main__":
    main()
