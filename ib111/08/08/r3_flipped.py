from ib111 import week_08  # noqa


# Implementujte predikát ‹is_almost_sorted›, který je pravdivý,
# je-li v seznamu ‹items› potřeba prohodit právě jednu dvojici
# různých čísel, aby se stal vzestupně seřazeným.
# Existuje řešení, jehož časová složitost je lineární.


def is_sorted(items: list[int]) -> bool:
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False

    return True


def is_almost_sorted(items: list[int]) -> bool:
    bad_index = -1
    result = items.copy()

    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            bad_index = i
            break

    if bad_index == -1:
        return False

    for i in range(len(result)):
        left = None if i - 1 < 0 else result[i - 1]
        right = None if i + 1 >= len(result) else result[i + 1]
        if (left is None or result[i - 1] <= result[bad_index]) and (right is None or result[bad_index] < result[i + 1]):
            temp = result[i]
            result[i] = result[bad_index]
            result[bad_index] = temp
            break
    return is_sorted(result)



def main() -> None:
    items = [1, 0, 0, 0]
    assert is_almost_sorted(items)
    assert items == [1, 0, 0, 0]

    assert is_almost_sorted([1, 0, 0, 2])
    assert is_almost_sorted([0, 1, 0, 0, 2])
    assert is_almost_sorted([0, 2, 0, 0, 2, 0])
    assert is_almost_sorted([1, 2, 4, 3, 5])
    assert is_almost_sorted([1, 5, 3, 4, 2])
    assert is_almost_sorted([5, 2, 3, 4, 1])
    assert not is_almost_sorted([4, 5, 6, 7, 8])
    assert not is_almost_sorted([2, 2, 4, 4, 4])
    assert not is_almost_sorted([5, 1, 3, 4, 2])
    assert not is_almost_sorted([5, 4, 3, 2, 1])

    items = [1, 2, 5, 3, 4]
    assert not is_almost_sorted(items)
    assert items == [1, 2, 5, 3, 4]


if __name__ == "__main__":
    main()
