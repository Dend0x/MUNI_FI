from ib111 import week_06  # noqa

# «Flood fill» je algoritmus z oblasti rastrové grafiky, který
# vyplní souvislou jednobarevnou plochu novou barvou. Postupuje
# tak, že nejdříve na novou barvu obarví pozici, na které začíná,
# dále se pokusí obarvit její sousedy (pozice jiné než cílové barvy
# se neobarvují), a podobně pokračuje se sousedy těchto sousedů,
# atd. Zastaví se, dojde-li na okraj obrázku, nebo narazí na pixel,
# který nemá žádné nové stejnobarevné sousedy.
#
# Sousední pixely uvažujeme pouze ve čtyřech směrech, tj. ne
# diagonálně.

# Napište proceduru, která na vstupu dostane plochu reprezentovanou
# obdélníkovým seznamem seznamů (délky všech vnitřních seznamů jsou
# stejné), počáteční pozici (je zaručeno, že se bude jednat o platné
# souřadnice), a cílovou barvu, na kterou mají být vybrané pozice
# přebarveny.

Position = tuple[int, int]
Area = list[list[int]]


def flood_fill(area: Area, start: Position, colour: int) -> None:
    x, y = start
    if area == []:
        return

    original = area[x][y]

    if original == colour:
        return

    area[x][y] = colour
    stack = [(x, y)]

    move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while stack != []:
        x1, y1 = stack.pop()
        for item in move:
            x_off, y_off = item
            x_pre = x1 + x_off
            y_pre = y1 + y_off
            if (0 <= x_pre < len(area)
                    and 0 <= y_pre < len(area[0])
                    and original == area[x_pre][y_pre]):
                area[x_pre][y_pre] = colour
                stack.append((x_pre, y_pre))


def main() -> None:
    check_flood([[0]], (0, 0), 1, [[1]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 3), 2, [[0, 0, 2, 2, 2, 0]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 0), 2, [[2, 2, 1, 1, 1, 0]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [5, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [5, 5, 8, 8]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [1, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [1, 5, 8, 8]])


def check_flood(area: Area, start: Position,
                new_colour: int, expected_result: Area) -> None:
    flood_fill(area, start, new_colour)
    assert area == expected_result


if __name__ == '__main__':
    main()
