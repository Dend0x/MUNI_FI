from ib111 import week_01  # noqa
from math import sqrt

# † Napište predikát ‹is_abundant›, který je pravdivý, pokud je
# kladné celé číslo ‹number› abundantní, t.j. je menší, než součet
# jeho vlastních dělitelů.
#
# Za vlastní dělitele čísla považujeme všechny jeho kladné
# dělitele s výjimkou čísla samotného; např. vlastní dělitelé
# čísla 12 jsou 1, 2, 3, 4, 6.


def is_abundant(number):
    divisors_sum = 0
    n = sqrt(number)
    i = 2

    while(i <= n):
        if(number % i == 0):
            divisors_sum += i
            if(sqrt(number) != i):
                divisors_sum += number // i
        i += 1
    
    return (divisors_sum + 1) > number


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
