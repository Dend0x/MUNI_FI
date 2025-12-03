from ib111 import week_10  # noqa


# Napište (čistou) funkci, která dostane na vstupu množinu čísel a
# vrátí délku nejdelšího šestnáctkového kruhu, který se z nich dá
# vytvořit. Pokud se žádný kruh vytvořit nedá, vrátí 0.

# Šestnáctkový kruh je posloupnost čísel (bez opakování) taková, že
# každé další číslo začíná v šestnáctkovém zápisu stejnou cifrou,
# jakou končí číslo předchozí. Navíc první číslo v posloupnosti
# začíná stejnou číslicí, jakou končí poslední číslo.


def first_last_hex(numbers: set[int]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for num in numbers:
        last = num % 16
        while num >= 16:
            num //= 16
        first = num
        result.append((first, last))

    return result


def hex_circle_rec(seen_indices: set[int], nums: list[int],
                   f_and_l: list[tuple[int, int]],
                   current: list[tuple[int, int]]) -> int:
    if len(seen_indices) == len(nums):
        if current == []:
            return 0
        first, _ = current[0]
        _, last = current[-1]
        if first == last:
            return len(current)
        return 0
    maxi = 0
    for i in range(len(nums)):
        if i in seen_indices:
            continue
        if current != []:
            _, last = current[-1]
            first, _ = f_and_l[i]
            if first != last:
                continue
        seen_indices.add(i)
        current.append(f_and_l[i])

        if first == last:
            maxi = max(maxi, len(current))

        length = hex_circle_rec(seen_indices, nums, f_and_l, current)
        maxi = max(maxi, length)
        current.pop()
        seen_indices.remove(i)

    return maxi


def hex_circle(numbers: set[int]) -> int:
    if len(numbers) == 0:
        return 0
    nums: list[int] = list(numbers)
    result: list[tuple[int, int]] = first_last_hex(numbers)

    maxi = hex_circle_rec(set(), nums, result, [])
    return maxi


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
