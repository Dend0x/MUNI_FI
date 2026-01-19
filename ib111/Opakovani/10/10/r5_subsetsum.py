from ib111 import week_10  # noqa


# Napište čistou funkci, která najde libovolnou podmnožinu zadané množiny
# kladných celých čísel ‹nums›, součet jejíchž prvků je přesně
# ‹total›. Pokud taková podmnožina neexistuje, funkce vrátí ‹None›.
#
# Při řešení přemýšlejte, jestli některé výpočty neprovádíte opakovaně
# a jak byste se tomu mohli vyhnout.


def subset_req(nums: list[int], current_sum: int, total: int, result: set[int], used: set[int], low: int):
    if current_sum == total:

        return True

    for i in range(low, len(nums)):
        if i in used:
            continue
        if nums[i] > total - current_sum:
            return False
        used.add(i)
        result.add(nums[i])
        if subset_req(nums, current_sum + nums[i], total, result, used, low + 1):
            return True
        result.remove(nums[i])
        used.remove(i)

    return False


def subset_sum(nums: set[int], total: int) -> set[int] | None:
    result: set[int] = set()
    if subset_req(list(nums), 0, total, result, set(), 0):
        return result
    return None


def main() -> None:
    assert subset_sum(set(), 5) is None

    nums = {1, 2, 3}
    assert subset_sum(nums, 7) is None
    assert nums == {1, 2, 3}

    assert subset_sum({1}, 1) == {1}
    assert subset_sum({1, 2, 3}, 5) == {2, 3}

    nums = {5, 10, 12, 13}
    assert subset_sum(nums, 27) == {5, 10, 12}
    assert nums == {5, 10, 12, 13}

    assert subset_sum({2022, 2021, 2020, 2019, 2018}, 5050) is None
    assert subset_sum({2, 3, 4, 804, 390, 11, 597, 598}, 1204) \
        == {2, 3, 4, 597, 598}


if __name__ == '__main__':
    main()
