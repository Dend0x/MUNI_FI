from ib111 import week_04  # noqa

# Magický čtverec je dvourozměrná matice vzájemně různých kladných celých
# čísel, pro niž platí, že součty čísel v každém řádku, každém sloupci a
# obou hlavních úhlopříčkách jsou stejné. Klasickým příkladem je magický
# čtverec 3x3:
# 8 1 6
# 3 5 7
# 4 9 2
# v němž se součty všech řádků, všech sloupců a obou diagonál rovnají 15.

# Napište predikát is_magic_square, který na vstupu dostane dvourozměrné pole
# celých čísel a ověří, že se jedná o magický čtverec.


def is_in(arr: list[int], val: int) -> bool:
    for elem in arr:
        if elem == val:
            return True

    return False


def is_magic_square(square: list[list[int]]) -> bool:
    number = 0
    seen: list[int] = []

    for i in range(len(square)):
        for j in range(len(square)):
            if is_in(seen, square[i][j]):
                return False
            seen.append(square[i][j])

    for i in range(len(square)):
        number += square[0][i]

    for i in range(len(square)):
        cont1 = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0
        for j in range(len(square)):
            cont1 += square[i][j]
            cont2 += square[j][i]
            cont3 += square[j][j]
            cont4 += square[j][len(square) - j - 1]
        if cont1 != number or cont2 != number or cont3 != number or cont4 != number:
            return False

    return True


def main() -> None:
    assert is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    assert is_magic_square([])
    assert is_magic_square([[1]])
    assert not is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert not is_magic_square([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert is_magic_square([[16, 2, 3, 13], [5, 11, 10, 8],
                           [9, 7, 6, 12], [4, 14, 15, 1]])


if __name__ == "__main__":
    main()
