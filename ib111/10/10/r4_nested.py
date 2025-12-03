from ib111 import week_10  # noqa

# † Z přednášky již znáte vnořený seznam čísel ‹NestedList›:

NestedList = list['int | NestedList']


# Napište proceduru, která na vstupu dostane ‹NestedList› celých
# čísel a upraví ho tak, aby v něm byla čísla seřazená vzestupně
# napříč všemi vnitřními seznamy. Například seznam ‹[[4, 7, 1], [],
# [8], [0, 5]]› se použitím této procedury změní na ‹[[0, 1, 4], [],
# [5], [7, 8]]›.


def numbers_used(list_of_lists: int | NestedList, numbers: list[int | None]) -> None:
    if list_of_lists == []:
        numbers.append(None)
        return
    if isinstance(list_of_lists, int):
        numbers.append(list_of_lists)
        return
    for n in list_of_lists:
        numbers_used(n, numbers)

def sort_nested_rec(list_of_lists: NestedList, numbers: list[int], i: list[int]) -> None:
    for index, n in enumerate(list_of_lists):
        if isinstance(n, int):
            num = numbers[i[0]]
            if num is not None:
                list_of_lists[index] = num
            i[0] += 1
        else:
            sort_nested_rec(n, numbers, i)

def sort_nested(list_of_lists: NestedList) -> None:
    numbers: list[int | None] = []
    numbers_used(list_of_lists, numbers)
    ints_sorted: list[int] = sorted([x for x in numbers if isinstance(x, int)])
    sort_nested_rec(list_of_lists, ints_sorted, [0])


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
