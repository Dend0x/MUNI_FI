from ib111 import week_01  # noqa
from math import sqrt

# † Napište predikát, který určí, jsou-li dvě kladná celá čísla
# spřátelená (amicable). Spřátelená čísla jsou taková,
# že součet všech vlastních dělitelů jednoho čísla se rovná
# druhému číslu, a naopak – součet všech vlastních dělitelů
# druhého čísla se rovná prvnímu.
#
# Za vlastní dělitele čísla považujeme všechny jeho kladné
# dělitele s výjimkou čísla samotného; např. vlastní dělitelé
# čísla 12 jsou 1, 2, 3, 4, 6.

def div_sum(number):
    if(number == 1):
        return 0

    divisors_sum = 0
    n = sqrt(number)
    i = 2
    while(i <= n):
        if(number % i == 0):
            divisors_sum += i
            if(sqrt(number) != i):
                divisors_sum += number // i
        i += 1
    return divisors_sum + 1

def amicable(a, b):
    return div_sum(a) == b and a == div_sum(b)


def main():
    assert not amicable(136, 241)
    assert not amicable(1, 1)
    assert amicable(220, 284)
    assert amicable(1184, 1210)
    assert amicable(2620, 2924)
    assert not amicable(1190, 1212)
    assert not amicable(349, 234)


if __name__ == "__main__":
    main()
