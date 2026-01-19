from ib111 import week_10  # noqa

# Na vstupu dostanete neprázdný seznam čísel. Vaším úkolem je vrátit
# množinu všech seznamů, které:
#
#  1. jsou vlastními podposloupnostmi vstupního seznamu, tzn.
#     vzniknou ze vstupního seznamu vynecháním alespoň jednoho
#     prvku,
#  2. jsou neklesající, tzn. pro seznam ‹out› a celá čísla ‹i›, ‹j›
#     platí ‹i < j› → ‹out[i] ≤ out[j]›.
#
# Protože datový typ ‹set› neumožňuje ukládat seznamy jako prvky,
# výstup uložte do seznamu (na pořadí jednotlivých posloupností
# v tomto seznamu nezáleží).


def subseq_rec(seq: list[int], used: set[int], result: list[list[int]], current: list[int], length: int, max_length: int, low: int) -> None:
    if length == max_length:
        return

    if current != seq:
        to_add = []
        for elem in current:
            to_add.append(seq[elem])
        if to_add not in result:
            result.append(to_add)

    for i in range(low, len(seq)):
        if i in used:
            continue
        added: bool = False
        used.add(i)
        if current == []:
            current.append(i)
            added = True
        else:
            if seq[current[-1]] <= seq[i] and current[-1] < i:
                current.append(i)
                added = True
        subseq_rec(seq, used, result, current, length + 1, max_length, i + 1)
        if added:
            current.pop()
        used.remove(i)


def subseq(seq: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    subseq_rec(seq, set(), result, [], 0, len(seq), 0)
    return result


def main() -> None:
    subseq_test([1], [[]])
    subseq_test([1, 2], [[], [1], [2]])
    subseq_test([2, 1], [[], [1], [2]])
    subseq_test([2, 2, 2], [[], [2], [2, 2]])
    subseq_test([2, 1, 2], [[], [1], [2], [2, 2], [1, 2]])
    subseq_test([-1, 0, 1], [[], [-1], [0], [1],
                             [-1, 0], [-1, 1], [0, 1]])
    subseq_test([1, -12, 0, 55], [[], [1], [-12],
                                  [0], [55], [1, 55],
                                  [-12, 0], [-12, 0, 55],
                                  [-12, 55], [0, 55]])
    subseq_test([3, 2, 1], [[], [3], [2], [1]])


def subseq_test(input_seq: list[int],
                expected: list[list[int]]) -> None:
    original_seq = input_seq.copy()
    result = subseq(input_seq)

    assert input_seq == original_seq

    result.sort()
    expected.sort()
    assert result == expected, (result, expected)


if __name__ == '__main__':
    main()
