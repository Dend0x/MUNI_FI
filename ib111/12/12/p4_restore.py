from ib111 import week_12  # noqa


# Napište čistou funkci ‹restore_sequence›, která dostane neprázdný řetězec
# složený pouze z číslic 0 a 1 a vrátí množinu všech možných
# řetězců, které vzniknou doplněním znaků čárky ‹','› do původního
# řetězce tak, aby části jimi oddělené byly dvojkové zápisy čísel
# v intervalu od ‹low› do ‹high› včetně. Hodnota ‹low› bude vždy
# alespoň 1. Rozdělení musí být takové, že žádný zápis neobsahuje
# levostranné nuly.


def to_dec(num: str, high: int) -> int:
    result = 0
    chars: dict[str, int] = {'0': 0, '1': 1}

    if not num or num[0] == '0':
        return high + 1

    for ch in num:
        result *= 2
        result += chars[ch]
        if result > high:
            return high + 1

    return result


def convert(digits: str, low: int, high: int) -> bool:
    parts = digits.split(',')
    for part in parts:
        if not part:
            return False
        num = to_dec(part, high)
        if low > num or high < num:
            return False

    return True


def restore_sequence_rec(digits: str, index: int, low: int,
                         high: int, result: set[str], current: str) -> None:
    if index >= len(digits):
        if convert(current, low, high):
            result.add(current)
        return

    restore_sequence_rec(digits, index + 1, low, high,
                         result, current + digits[index])
    if index + 1 < len(digits) and digits[index + 1] == '1':
        restore_sequence_rec(digits, index + 1, low, high,
                             result, current + digits[index] + ',')


def restore_sequence(digits: str, low: int, high: int) -> set[str]:
    result: set[str] = set()
    if low > high:
        return result
    restore_sequence_rec(digits, 0, low, high, result, "")
    return result


def main() -> None:
    assert restore_sequence("1111", 2, 3) == {"11,11"}
    assert restore_sequence("11110", 1, 6) == \
        {"1,1,1,10", "11,1,10", "11,110", "1,1,110", "1,11,10"}
    assert restore_sequence("1111", 100, 200) == set()
    assert restore_sequence("101010", 2, 10) \
        == {"10,10,10", "10,1010", "1010,10"}
    assert restore_sequence("1001", 1, 30) == {"1001", "100,1"}
    assert restore_sequence("111101111", 0b101, 0b111) == {"111,101,111"}
    assert restore_sequence("1110101", 1, 9) == {
        "1,1,10,101",
        "11,10,101",
        "11,10,10,1",
        "1,110,101",
        "1,110,10,1",
        "1,1,10,10,1",
    }


if __name__ == '__main__':
    main()
