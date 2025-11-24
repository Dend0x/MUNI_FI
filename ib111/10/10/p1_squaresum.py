from ib111 import week_10  # noqa
from math import isqrt


# Napište predikát, který rozhodne, zda lze dané číslo ‹num› napsat
# jako součet ⟦∑ᵢ₌₁ⁿaᵢ²⟧, kde ⟦n⟧ je zadáno parametrem ‹count› a
# ⟦aᵢ⟧ jsou po dvou různá kladná čísla. Jinými slovy, lze ‹num›
# zapsat jako součet ‹count› druhých mocnin různých kladných čísel?

def is_sum_of_squares_rec(low: int, sum_num: int,
                          num: int, count: int) -> bool:
    if num == sum_num:
        return count == 0

    if count == 0 or sum_num > num:
        return False

    for i in range(low, isqrt(num - sum_num) + 1):
        if is_sum_of_squares_rec(i + 1, sum_num + i ** 2, num, count - 1):
            return True

    return False


def is_sum_of_squares(num: int, count: int) -> bool:
    return is_sum_of_squares_rec(1, 0, num, count)


def main() -> None:
    assert is_sum_of_squares(42, 3)
    assert not is_sum_of_squares(42, 2)
    assert not is_sum_of_squares(18, 2)
    assert not is_sum_of_squares(100, 3)
    assert is_sum_of_squares(100, 5)
    assert not is_sum_of_squares(1000, 13)


if __name__ == '__main__':
    main()
