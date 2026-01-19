from ib111 import week_10  # noqa


# Napište (čistou) funkci, která dostane na vstupu množinu čísel a
# vrátí délku nejdelšího šestnáctkového kruhu, který se z nich dá
# vytvořit. Pokud se žádný kruh vytvořit nedá, vrátí 0.

# Šestnáctkový kruh je posloupnost čísel (bez opakování) taková, že
# každé další číslo začíná v šestnáctkovém zápisu stejnou cifrou,
# jakou končí číslo předchozí. Navíc první číslo v posloupnosti
# začíná stejnou číslicí, jakou končí poslední číslo.

def to_hex(numbers: set[int]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for num in numbers:
        last = num % 16
        num //= 16
        first = last
        while num > 0:
            first = num % 16
            num //= 16
        result.append((first, last))

    return result


def hex_circle_rec(hex_list: list[tuple[int, int]], maxi: list[int], used: set[int], current_circle: list[int]):
    for index in range(len(hex_list)):
        if index in used:
            continue
        added: bool = False
        used.add(index)
        if current_circle == []:
            current_circle.append(index)
            added = True
        else:
            _, last = hex_list[current_circle[-1]]
            first, _ = hex_list[index]
            if first == last:
                current_circle.append(index)
                added = True

        first_all, _ = hex_list[current_circle[0]]
        _, last_all = hex_list[current_circle[-1]]
        if first_all == last_all:
            if len(current_circle) > maxi[0]:
                maxi[0] = len(current_circle)

        hex_circle_rec(hex_list, maxi, used, current_circle)
        if added:
            current_circle.pop()
        used.remove(index)

def hex_circle(numbers: set[int]) -> int:
    hex_list: list[tuple[int, int]] = to_hex(numbers)
    maxi: list[int] = [0]
    hex_circle_rec(hex_list, maxi, set(), [])
    return maxi[0]


def main() -> None:
    assert hex_circle(set()) == 0
    assert hex_circle({0xabc, 0x123}) == 0
    assert hex_circle({0xabcd, 0xdef, 0xfa}) == 3
    assert hex_circle({0xaba}) == 1
    assert hex_circle({0xabc, 0xca, 0xcd, 0xda}) == 3

    hexes = {0xabc, 0xca, 0xacd, 0xda}
    assert hex_circle(hexes) == 4
    assert hexes == {0xabc, 0xca, 0xacd, 0xda}


if __name__ == '__main__':
    main()
