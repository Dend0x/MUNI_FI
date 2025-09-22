from ib111 import week_01  # noqa
from math import sqrt

# Napište funkci, která vrátí počet různých kladných dělitelů
# kladného celého čísla ‹number› (např. číslo 12 je dělitelné 1, 2,
# 3, 4, 6 a 12 – výsledek ‹divisors(12)› bude tedy 6.

def divisors(number):
    divisors_count = 0
    n = sqrt(number)
    i = 1

    while(i <= n):
        if(number % i == 0):
            divisors_count += 1
        i += 1
    
    if (i - 1) ** 2 == number:
        divisors_count = (divisors_count - 1) * 2 + 1
    else:
        divisors_count *= 2

    return divisors_count

def main():
    assert divisors(1) == 1
    assert divisors(2) == 2
    assert divisors(3) == 2
    assert divisors(4) == 3
    assert divisors(5) == 2
    assert divisors(12) == 6
    assert divisors(16) == 5
    assert divisors(18) == 6
    assert divisors(42) == 8
    assert divisors(100) == 9
    assert divisors(127) == 2
    assert divisors(1024) == 11
    assert divisors(1069) == 2


if __name__ == "__main__":
    main()
