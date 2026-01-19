from ib111 import week_10  # noqa


# Napište predikát, který dostane na vstupu množinu čísel ⟦M⟧ a
# délku ⟦n⟧ a rozhodne, existuje-li navazující posloupnost čísel
# délky právě ⟦n⟧. Navazující posloupnost je taková, kde každé další
# číslo začíná v jedenáctkovém zápisu stejnou číslicí, jakou končí
# předchozí. Čísla se v posloupnosti nesmí opakovat.


def to_elv(numbers: set[int], changed: list[tuple[int, int]]) -> None:
    for num in numbers:
        last = num % 11
        num //= 11
        first = last
        while num > 0:
            first = num % 11
            num //= 11
        changed.append((first, last))


def chain_rec(count: int, current_count: int, changed: list[tuple[int, int]], used: set[int], last: int) -> bool:
    if current_count == count:
        return True

    for i in range(len(changed)):
        if i in used:
            continue
        first, _ = changed[i]
        if last == -1:
            last_last = first
        else:
            _, last_last = changed[last]
        if last_last == first:
            used.add(i)
            if chain_rec(count, current_count + 1, changed, used, i):
                return True
            used.remove(i)

    return False

def elven_chain(numbers: set[int], length: int) -> bool:
    changed: list[tuple[int, int]] = []
    to_elv(numbers, changed)
    return chain_rec(length, 0, changed, set(), -1)


def main() -> None:
    assert elven_chain(set(), 0)
    assert elven_chain({1}, 1)
    assert elven_chain({146, 12}, 2)
    assert elven_chain({146, 23}, 2)
    assert not elven_chain({146, 11}, 2)
    assert not elven_chain({146, 13}, 2)
    assert not elven_chain({2, 13}, 3)

    numbers = {146, 12}
    assert elven_chain(numbers, 2)
    assert numbers == {146, 12}


if __name__ == '__main__':
    main()
