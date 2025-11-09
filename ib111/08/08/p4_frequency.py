from ib111 import week_08  # noqa


# Implementujte čistou funkci ‹frequency_sort›, která podle
# frekvencí výskytu seřadí hodnoty v seznamu ‹values›. Hodnoty se
# stejnou frekvencí výskytu nechť jsou seřazeny vzestupně podle
# hodnoty samotné. Výsledný seznam bude obsahovat každou hodnotu
# právě jednou.

def frequency_sort(values: list[int]) -> list[int]:
    count: dict[int, int] = {}
    reversed = []
    result = []

    for value in values:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1

    for key, value in count.items():
        reversed.append((-value, key))

    sorted_result = sorted(reversed)

    for _, value in sorted_result:
        result.append(value)

    return result


def main() -> None:
    assert frequency_sort([]) == []
    assert frequency_sort([1]) == [1]
    assert frequency_sort([1, 3, 2, 4]) == [1, 2, 3, 4]
    assert frequency_sort([5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]) == [5, 6, 3, 2]
    assert frequency_sort([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5,
                           5, 4, 4, 4, 4, 4, 4]) == [4, 3, 2, 5, 1]
    records = [1, 2, 2, 2, 3, 3]
    assert frequency_sort(records) == [2, 3, 1]
    assert records == [1, 2, 2, 2, 3, 3]


if __name__ == "__main__":
    main()
