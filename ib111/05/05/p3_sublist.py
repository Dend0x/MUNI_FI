from ib111 import week_05  # noqa


# V tomto příkladu dostanete dva seznamy obsahující celá čísla.
# Vaším úkolem je napsat čistou funkci ‹largest_common_sublist_sum›,
# která najde takový společný podseznam seznamů ‹left› a ‹right›,
# který má největší celkový součet, a tento součet vrátí.

# Podseznamem seznamu ‹S› myslíme takový seznam ‹T›, pro který
# existuje číslo ‹k› takové, že platí ‹S[k + i] == T[i]› pro všechna
# ‹i› taková, že ⟦0 ≤ i < len(T)⟧. Například seznam ‹[1, 2]› je
# podseznamem seznamu ‹[0, 1, 2, 3]›, kde ‹k = 1›.

# Složitost smí být v nejhorším případě až kubická vzhledem k délce
# delšího vstupního seznamu.

def largest_common_sublist_sum(left: list[int], right: list[int]) -> int:
    left_index = len(left) - 1
    right_index = len(right) - 1
    res_index = 0
    in_seq = True
    pos_result: list[int] = [0]

    while left_index >= 0 and right_index >= 0:
        if left[left_index] == right[right_index]:
            if not in_seq:
                pos_result.append(left[left_index])
                in_seq = True
            else:
                pos_result[res_index] += left[left_index]
            left_index -= 1
            right_index -= 1
        elif left[left_index] > right[right_index]:
            if in_seq:
                res_index += 1
            in_seq = False
            left_index -= 1
        else:
            if in_seq:
                res_index += 1
            in_seq = False
            right_index -= 1

    return max(pos_result)


def main() -> None:
    l1: list[int] = []
    l2 = [1, 2, 3, 4, 5]
    l3 = [2, 3, 4, 6, 7, 9, 10]
    l4 = [1, 2, 3, 8, 9]

    assert largest_common_sublist_sum(l1, l2) == 0
    assert largest_common_sublist_sum(l2, l3) == 9
    assert largest_common_sublist_sum(l2, l4) == 6
    assert largest_common_sublist_sum(l3, l4) == 9


if __name__ == "__main__":
    main()
