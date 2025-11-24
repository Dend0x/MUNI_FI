from ib111 import week_10  # noqa


# Napište predikát, který dostane na vstupu množinu čísel ⟦M⟧ a
# délku ⟦n⟧ a rozhodne, existuje-li navazující posloupnost čísel
# délky právě ⟦n⟧. Navazující posloupnost je taková, kde každé další
# číslo začíná v jedenáctkovém zápisu stejnou číslicí, jakou končí
# předchozí. Čísla se v posloupnosti nesmí opakovat.


def first_digit_num(num: int) -> int:
    while num >= 11:
        num //= 11
    return num


def elven_chain_rec(current_length: int, length: int, numbers: set[int], seen: set[int], current_list: list[int]) -> bool:
    if current_length > length:
        return False

    if current_length == length:
        return True

    for num in numbers:
        if num in seen:
            continue
        if current_list != []:
            first_digit = first_digit_num(num)

            if current_list[-1] % 11 != first_digit:
                continue
        seen.add(num)
        current_list.append(num)
        if elven_chain_rec(current_length + 1, length, numbers, seen.copy(), current_list):
            return True
        seen.remove(num)
        current_list.pop()
    return False
        

def elven_chain(numbers: set[int], length: int) -> bool:
    if length == 0:
        return True
    return elven_chain_rec(0, length, numbers, set(), [])


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
