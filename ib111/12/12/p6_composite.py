from ib111 import week_12  # noqa
from math import isqrt


# Napište čistou funkci ‹highly_composite›, která dostane na vstupu
# množinu přirozených čísel a vrátí množinu těch z nich, která jsou
# vysoce složená relativně k původní množině. Přirozené číslo je
# vysoce složené, má-li striktně víc dělitelů (a to včetně těch,
# které v zadané množině nejsou), než libovolné menší číslo ze
# zadané množiny.


def dividors(num: int) -> int:
    count = 0

    for i in range(1, isqrt(num) + 1):
        if num % i == 0:
            if i ** 2 != num:
                count += 1
            count += 1

    return count

def highly_composite(numbers: set[int]) -> set[int]:
    nums = sorted(numbers)
    biggest = 0
    result: set[int] = set()

    for num in nums:
        divs_num = dividors(num)
        if biggest >= divs_num:
            continue
        result.add(num)
        biggest = divs_num

    return result


def main() -> None:
    small_c = {1, 2, 4, 6, 12, 24, 36, 48}

    assert highly_composite({1, 3, 7, 12}) == {1, 3, 12}
    assert highly_composite(set(range(1, 50))) == small_c

    big1 = set(range(1, 100)) | big_set(6, 4)
    big2 = set(range(1, 1000)) | big_set(6, 8)
    big1_c = {60, big_n(4, 2), big_n(5, 2), big_n(4, 3), big_n(5, 3)}
    big2_c = {60, 120, 180, 240, 360, 720, 840,
              big_n(5, 5), big_n(5, 6), big_n(5, 7)}
    assert highly_composite(big1) == small_c | big1_c
    assert highly_composite(big2) == small_c | big2_c


def big_set(a: int, b: int) -> set[int]:
    return set([big_n(i, j)
                for i in range(1, a)
                for j in range(b)])


def big_n(i: int, j: int) -> int:
    num: int = 7 ** i * 10099 ** j
    return num


if __name__ == '__main__':
    main()
