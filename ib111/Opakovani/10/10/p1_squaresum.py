from ib111 import week_10  # noqa
from math import isqrt


# Napište predikát, který rozhodne, zda lze dané číslo ‹num› napsat
# jako součet ⟦∑ᵢ₌₁ⁿaᵢ²⟧, kde ⟦n⟧ je zadáno parametrem ‹count› a
# ⟦aᵢ⟧ jsou po dvou různá kladná čísla. Jinými slovy, lze ‹num›
# zapsat jako součet ‹count› druhých mocnin různých kladných čísel?


def is_sum_rec(num: int, count: int, current_count: int, current_sum: int , low: int) -> bool:
    if current_count >= count:
        return num == current_sum

    for i in range(low, isqrt(num - current_sum) + 1):
        if is_sum_rec(num, count, current_count + 1, current_sum + i ** 2, i + 1):
            return True

    return False



def is_sum_of_squares(num: int, count: int) -> bool:
    return is_sum_rec(num, count, 0, 0, 1)


def main() -> None:
    assert is_sum_of_squares(42, 3)
    assert not is_sum_of_squares(42, 2)
    assert not is_sum_of_squares(18, 2)
    assert not is_sum_of_squares(100, 3)
    assert is_sum_of_squares(100, 5)
    assert not is_sum_of_squares(1000, 13)


if __name__ == '__main__':
    main()
