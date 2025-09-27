from ib111 import week_02  # noqa


# Napište funkci, která vytvoří číslo zřetězením ‹count› po sobě
# jdoucích kladných čísel počínaje zadaným číslem ‹start›.  Tato
# čísla zřetězte vyjádřená v binární soustavě. Například volání
# ‹joined(1, 3)› zřetězí sekvenci ⟦(1)₂ = 1⟧, ⟦(10)₂ = 2⟧, ⟦(11)₂ = 3⟧
# a vrátí číslo ⟦(11011)₂ = 27⟧. V Pythonu lze binární čísla přímo
# zapisovat v tomto tvaru: ‹0b11011› (podobně lze stejné číslo
# zapsat v šestnáctkové soustavě zápisem ‹0x1b› nebo osmičkové jako
# ‹0o33›).

def two_to_ten(number):
    result = 0
    i = 0

    while number > 0:
        result += (number % 10) * 2 ** i
        number //= 10
        i += 1

    return result


def joined(start, count):
    bi_number = 0

    for i in range(start, start + count):
        number = i
        current_number_bi = 0
        digit = 0

        while number > 0:
            current_number_bi += (number % 2) * 10 ** digit
            number //= 2
            digit += 1
        bi_number = bi_number * 10 ** digit + current_number_bi

    return two_to_ten(bi_number)


def main() -> None:
    assert joined(1, 3) == 0b11011
    assert joined(10, 4) == 0b1010101111001101
    assert joined(8, 5) == 0b10001001101010111100
    assert joined(99, 2) == 0b11000111100100
    assert joined(999, 3) == 0b111110011111111010001111101001
    assert joined(1111, 1) == 0b10001010111


if __name__ == "__main__":
    main()
