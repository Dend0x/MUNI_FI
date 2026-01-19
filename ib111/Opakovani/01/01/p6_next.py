from ib111 import week_01  # noqa
from math import isqrt


# Napište funkci, která pro zadané celé číslo ‹number›
# najde nejbližší větší číslo, které je násobkem kladného
# celého čísla ‹k›.

def next_multiple(number, k):
    num = number // k
    return k * (num + 1)


# Dále napište funkci, která pro zadané kladné celé číslo
# ‹number› najde nejbližší větší prvočíslo.


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return False

    return True


def next_prime(number):
    num =  number + 1

    while not is_prime(num):
        num += 1

    return num

def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13
    assert next_prime(13) == 17


if __name__ == "__main__":
    main()
