from ib111 import week_10  # noqa


# V tomto příkladu máme na vstupu neprázdný řetězec desítkových číslic
# (tj. znaků ‹'0'› až ‹'9'›), který «nezačíná znakem ‹'0'›», a chceme je
# rozsekat na části tak, aby tvořily rostoucí posloupnost čísel zapsaných
# v desítkové soustavě, přitom žádná část nesmí začínat znakem ‹'0'›.
# Ze všech takových posloupností pak chceme vybrat tu, která má co nejnižší
# své poslední číslo. Vaším úkolem je napsat čistou funkci, která spočítá
# toto číslo. Funkce by měla fungovat na vstupech o řádově desítkách znaků.
#
# Příklad: Řetězec ‹"23245"› můžeme rozsekat na rostoucí posloupnosti
# následujícími způsoby: 2, 3, 245 nebo 2, 32, 45 nebo 23, 245 nebo 23245.
# Nejnižší poslední číslo je 45; volání
# ‹lowest_increasing_sequence_end("23245")› tedy vrátí ‹45›.


def lowest_rec(digits: list[int], prev: int | None, pos: int) -> int | None:
    if pos == len(digits):
        return prev

    value = 0
    mini: int | None = None
    for i in range(pos, len(digits)):
        if i > pos and digits[pos] == 0:
            break

        value = value * 10 + digits[i]

        if prev is not None and value <= prev:
            continue
        
        if i + 1 >= len(digits):
            cur = value
        else:
            cur = lowest_rec(digits, value, i + 1)
        if cur is not None:
            if mini is None or cur < mini:
                mini = cur

    return mini



def lowest_increasing_sequence_end(digits: list[int]) -> int:
    print(lowest_rec(digits, None, 0))
    return lowest_rec(digits, None, 0)


def main() -> None:
    assert lowest_increasing_sequence_end([2, 3, 2, 4, 5]) == 45
    assert lowest_increasing_sequence_end([2, 0, 4, 4, 5]) == 445
    assert lowest_increasing_sequence_end([3, 2, 4, 5]) == 45
    assert lowest_increasing_sequence_end([9, 0, 1]) == 901
    assert lowest_increasing_sequence_end([9, 0, 2, 1, 0]) == 210
    assert lowest_increasing_sequence_end([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert lowest_increasing_sequence_end([1, 1, 1, 1, 1,
                                           1, 1, 1, 1, 1]) == 1111
    assert lowest_increasing_sequence_end([9, 9, 9]) == 99
    assert lowest_increasing_sequence_end([9, 9]) == 99


if __name__ == '__main__':
    main()
