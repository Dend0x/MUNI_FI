from ib111 import week_10  # noqa

# † Z přednášky již znáte vnořený seznam čísel ‹NestedList›:

NestedList = list['int | NestedList']
End = list[int]

# Napište proceduru, která na vstupu dostane ‹NestedList› celých
# čísel a upraví ho tak, aby v něm byla čísla seřazená vzestupně
# napříč všemi vnitřními seznamy. Například seznam ‹[[4, 7, 1], [],
# [8], [0, 5]]› se použitím této procedury změní na ‹[[0, 1, 4], [],
# [5], [7, 8]]›.


def get_numbers(list_get: NestedList, result: list[int]) -> None:
    for elem in list_get:
        if isinstance(elem, int):
            result.append(elem)
        else:
            get_numbers(elem, result)


def write_numbers(list_get: NestedList, numbers: list[int], index: list[int]) -> None:
    for elem in list_get:
        if isinstance(elem, int):
            elem = numbers[index[0]]
            index[0] += 1
        else:
            write_numbers(elem, numbers, index)


def sort_nested(list_of_lists: NestedList) -> None:
    numbers: list[int] = []
    get_numbers(list_of_lists, numbers)
    numbers.sort()
    write_numbers(list_of_lists, numbers, [0])
    print(list_of_lists)
    return

def main() -> None:
    check_sort_nested([], [])
    check_sort_nested([[4, 1, 7], [], [8], [0, 5]],
                      [[0, 1, 4], [], [5], [7, 8]])
    check_sort_nested([[1, 8, [2]]], [[1, 2, [8]]])
    check_sort_nested([[[1]]],
                      [[[1]]])


def equal_nested(a: int | NestedList, b: int | NestedList) -> bool:
    if isinstance(a, int) or isinstance(b, int):
        return isinstance(a, int) and isinstance(b, int) and a == b

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if not equal_nested(a[i], b[i]):
            return False

    return True


def check_sort_nested(original: 'NestedList', expected: 'NestedList') -> None:
    sort_nested(original)
    assert equal_nested(original, expected)


if __name__ == '__main__':
    main()
