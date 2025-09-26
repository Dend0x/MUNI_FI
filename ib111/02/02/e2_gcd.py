from ib111 import week_02  # noqa


# Napište čistou funkci ‹gcd›, která pro zadaná kladná čísla nalezne
# jejich největšího společného dělitele. Použijte naivní algoritmus
# (tedy takový, který bude zkoušet všechny možnosti, počínaje
# největším vhodným kandidátem).

def gcd(x1, x2):
    if x1 > x2:
        c = x1
        x1 = x2
        x2 = c

    for i in range(x1, 1, -1):
        if x1 % i == 0:
            if x2 % i == 0:
                return i
    return 1


def main():
    assert gcd(5, 5) == 5
    assert gcd(5, 10) == 5
    assert gcd(6, 15) == 3
    assert gcd(18, 15) == 3
    assert gcd(12, 1) == 1


if __name__ == "__main__":
    main()
