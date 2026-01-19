from ib111 import week_01  # noqa
from math import isqrt


# † Napište predikát, který určí, jsou-li dvě kladná celá čísla
# spřátelená (amicable). Spřátelená čísla jsou taková,
# že součet všech vlastních dělitelů jednoho čísla se rovná
# druhému číslu, a naopak – součet všech vlastních dělitelů
# druhého čísla se rovná prvnímu.
#
# Za vlastní dělitele čísla považujeme všechny jeho kladné
# dělitele s výjimkou čísla samotného; např. vlastní dělitelé
# čísla 12 jsou 1, 2, 3, 4, 6.

def amicable(a, b):
    dividorsa = 1 if a != 1 else 0

    for i in range(2, isqrt(a) + 1):
        if a % i == 0:
            dividorsa += i
            dividorsa += a // i
            if isqrt(a) == a // i:
                dividorsa -= a // i

    dividorsb = 1 if b != 1 else 0

    for i in range(2, isqrt(b) + 1):
        if b % i == 0:
            dividorsb += i
            dividorsb += b // i
            if isqrt(b) == b // i:
                dividorsb -= b // i

    return a == dividorsb and b == dividorsa

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
