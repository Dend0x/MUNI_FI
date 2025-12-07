from ib111 import week_11  # noqa


# Napište (čistou) funkci, která dostane na vstup řetězec složený
# pouze z číslic od 1 do 9 včetně a vrátí množinu všech možných IPv4
# adres, z nichž tento řetězec mohl vzniknout vynecháním teček.
# Za IPv4 adresu považujeme řetězec tvořený čtyřmi čísly v rozsahu
# od ‹0› po ‹255› včetně oddělenými tečkami. Například řetězec
# ‹25525511135› mohl vzniknout výše popsaným způsobem z adres
# ‹255.255.11.135› a ‹255.255.111.35›.

def convert(to_convert: str) -> tuple[int, bool]:
    digits: dict[str, int] = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    num = 0

    for i in range(len(to_convert)):
        if to_convert[i] not in digits:
            return 0, False
        digit = digits[to_convert[i]]
        num = num * 10 + digit

    return num, True


def ipv4_validate(address: str) -> bool:
    parts: list[str] = address.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdecimal():
            return False
        number, ok = convert(part)
        if not ok:
            return False
        if number > 255:
            return False

    return True


def ipv4_restore_rec(digits: str, index: int, address: str, result: set[str]) -> None:
    if index >= len(digits):
        if ipv4_validate(address):
            result.add(address)
        return

    ipv4_restore_rec(digits, index + 1, address + digits[index], result)
    ipv4_restore_rec(digits, index + 1, address + digits[index] + '.', result)

def ipv4_restore(digits: str) -> set[str]:
    result: set[str] = set()

    ipv4_restore_rec(digits, 0, "", result)
    return result


def main() -> None:
    assert ipv4_restore("25525511135") == {"255.255.11.135", "255.255.111.35"}
    assert ipv4_restore("1111") == {"1.1.1.1"}
    assert ipv4_restore("555") == set()
    assert ipv4_restore("11112") \
        == {"1.1.1.12", "1.1.11.2", "1.11.1.2", "11.1.1.2"}


if __name__ == '__main__':
    main()
