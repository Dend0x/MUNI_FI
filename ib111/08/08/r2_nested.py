from ib111 import week_08  # noqa


# Implementujte čistou funkci ‹sort_nested›, která vzestupně
# uspořádá prvky v seznamu seznamů čísel ‹lists›, a to tak, že
# přeuspořádá jenom čísla ve vnitřních seznamech, aniž by měnil
# jejich délku. Výstupní seznam bude tedy obsahovat stejný počet
# stejně dlouhých seznamů jako ten vstupní, ale v obecném případě
# budou tyto vnořené seznamy obsahovat jiná čísla.

def sort_nested(lists: list[list[int]]) -> list[list[int]]:
    result = []
    final: list[list[int]] = []

    for list in lists:
        for elem in list:
            result.append(elem)
    result.sort()
    k = 0

    for i in range(len(lists)):
        final.append([])
        for j in range(len(lists[i])):
            final[i].append(result[k])
            k += 1

    return final



def main() -> None:
    assert sort_nested([[5, 4], [1, 2, 3]]) == [[1, 2], [3, 4, 5]]
    assert sort_nested([[5], [4], [1, 2, 3]]) == [[1], [2], [3, 4, 5]]
    assert sort_nested([[5], [4], [2, 1], [3]]) == [[1], [2], [3, 4], [5]]
    assert sort_nested([[5], [4, 2, 1], [3]]) == [[1], [2, 3, 4], [5]]
    lists = [[5], [4, 2, 1], [3]]
    assert sort_nested(lists) == [[1], [2, 3, 4], [5]]
    assert lists == [[5], [4, 2, 1], [3]]


if __name__ == "__main__":
    main()
