from ib111 import week_12  # noqa

# V této úloze budeme implementovat simulaci procházky po 2D mřížce.
# Pro reprezentaci pozice v mřížce budeme používat uspořádanou
# dvojici ⟦(x, y)⟧.

Position = tuple[int, int]

# Cesta procházky je zadaná jako řetězec ‹path›, který se skládá
# z příkazů ‹←› / ‹→› pro pohyb doleva a doprava (po ose ⟦x⟧) a ‹↑›
# / ‹↓› pro pohyb nahoru a dolů (po ose ⟦y⟧). Souřadnice rostou ve
# směru doprava na ⟦x⟧-ové ose a nahoru na ⟦y⟧-ové ose.

# Napište čistou funkci ‹walk›, která vrátí finální pozici pro
# procházku ‹path› z počáteční pozice ‹start›.


def walk(path: str, start: Position) -> Position:
    vectors: dict[str, tuple[int, int]] = {"→": (1, 0), "↑": (0, 1), "←": (-1, 0), "↓": (0, -1)}
    x, y = start
    for arrow in path:
        xp, yp = vectors[arrow]
        x += xp
        y += yp

    return (x, y)



# Dále napište čistou funkci ‹meet›, která vrátí pro dvojici cest
# ‹path_1›, ‹path_2› a počátků ‹start_1› a ‹start_2›, první pozici
# na které se procházky potkají. Procházky se provádí synchronně,
# tj. kroky se vykonávají najednou pro obě procházky. Pokud se
# procházky nepotkají, funkce vrátí ‹None›.


def step(index: int, path_1: str, path_2: str, pos_1: Position, pos_2: Position) -> Position | None:
    if index >= len(path_1) or index >= len(path_2):
        return None if pos_1 != pos_2 else pos_1

    if pos_1 == pos_2:
        return pos_1

    vectors: dict[str, tuple[int, int]] = {"→": (1, 0), "↑": (0, 1), "←": (-1, 0), "↓": (0, -1)}

    xp1, yp1 = vectors[path_1[index]]
    x1, y1 = pos_1
    x1 += xp1
    y1 += yp1

    xp2, yp2 = vectors[path_2[index]]
    x2, y2 = pos_2
    x2 += xp2
    y2 += yp2   

    return step(index + 1, path_1, path_2, (x1, y1), (x2, y2))


def meet(path_1: str, path_2: str, start_1: Position,
         start_2: Position) -> Position | None:
    return step(0, path_1, path_2, start_1, start_2)


def main() -> None:
    assert walk("→→", (0, 0)) == (2, 0)
    assert walk("←↑→↓", (0, 0)) == (0, 0)
    assert walk("←←↑↑→↑↑→→↓→→→↑↑", (2, 3)) == (6, 8)
    assert walk("↑←↑→↑→", (-1, -3)) == (0, 0)

    assert meet("→→", "←←", (-1, 0), (1, 0)) == (0, 0)
    assert meet("←", "↓", (1, 0), (0, 1)) == (0, 0)

    assert meet("←↑→↓", "→↓←↑", (1, 0), (0, 1)) is None
    assert meet("↓↓↓↓↓↓", "↓↓↓↓↓↓", (1, 0), (0, 0)) is None

    assert meet("→↓→↓→↑←←→↓↓→", "↑→→↓→↓→↓→↑→←←",
                (2, 2), (-1, 1)) == (4, 0)


if __name__ == '__main__':
    main()
