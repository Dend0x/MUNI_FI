from ib111 import week_01  # noqa
from math import isqrt


# Napište funkci, která ověří, zda je číslo ‹number› prvočíslo.


def is_prime(number):

    if number < 2:
        return False

    if number == 2:
        return True

    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return False

    return True


def main():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(13)
    assert is_prime(29)
    assert is_prime(97)
    assert is_prime(619)

    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(68)
    assert not is_prime(77)
    assert not is_prime(81)
    assert not is_prime(323)
    assert not is_prime(36863)


if __name__ == "__main__":
    main()
