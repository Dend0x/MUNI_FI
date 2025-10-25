from ib111 import week_05  # noqa


# Vaším úkolem je naprogramovat tzv. „hru života“ – jednoduchý
# dvourozměrný celulární automat. Simulace běží na čtvercové síti,
# kde každá buňka je mrtvá (hodnota 0) nebo živá (hodnota 1).
# V každém kroku se přepočte hodnota všech buněk, a to podle toho,
# zda byly v předchozím kroku živé a kolik měly živých sousedů
# (z celkem osmi, tzn. včetně úhlopříčných):
#
# │  stav │ živí sousedé │ výsledek │
# ├───────┼──────────────┼──────────┤
# │  živá │          0–1 │    mrtvá │
# │  živá │          2–3 │     živá │
# │  živá │          4–8 │    mrtvá │
# │┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│
# │ mrtvá │          0–2 │    mrtvá │
# │ mrtvá │            3 │     živá │
# │ mrtvá │          4-8 │    mrtvá │

# Příklad krátkého výpočtu:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │ ○ │   │   │ → │ ○ │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Jiný (periodický) výpočet je například:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │   │   │   │   │ ○ │   │   │   │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │   │ ○ │   │ → │ ○ │ ○ │ ○ │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │   │   │   │   │ ○ │   │   │   │   │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Napište čistou funkci, která dostane jako parametry počáteční stav
# hry (jako množinu dvojic, která reprezentuje souřadnice živých
# buněk) a počet kroků, a vrátí stav hry po odpovídajícím počtu
# kroků.


def neighbours(aux: list[list[int]], x: int, y: int) -> int:
    sum_cells = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i >=0 and j >= 0:
                sum_cells += aux[x][y]

    return sum_cells


def eval_cell(result: list[list[int]], aux: list[list[int]], x: int, y: int) -> None:
    neigh = neighbours(aux, x, y)
    if aux[x][y] == 1:
        if 2 <= neigh <= 3:
            result[x][y] = 1
        else:
            result[x][y] = 0
    else:
        if neigh == 3:
            result[x][y] = 1
        else:
            result[x][y] = 0


def eval_board(result: list[list[int]]) -> None:

    aux = result.deepcopy()

    for i in range(3):
        for j in range(3):
            eval_cell(result, aux, i, j)


def life(cells: set[tuple[int, int]],
         n: int) -> set[tuple[int, int]]:
    alive = set(cells)  # copy, abychom neměnili vstup

    for _ in range(n):
        counts = dict()
        # pro každý živý cell zvýšíme count pro všech 8 sousedů (a/nebo i pro sebe, ale my nechceme)
        for (x, y) in alive:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    counts[(x + dx, y + dy)] += 1

        new_alive = set()
        # kandidáti jsou všechny pozice, které mají nonzero count, plus existující živé buňky (pokud count=0, stačí ignorovat)
        # pravidla: buňka žije dál pokud count==3 nebo (count==2 a byla již živá)
        for pos, cnt in counts.items():
            if cnt == 3 or (cnt == 2 and pos in alive):
                new_alive.add(pos)

        # také pozor: pokud nějaká buňka byla živá, ale všichni sousedé jsou 0, nebude v counts; ale podle pravidel taková buňka umírá (ok)
        alive = new_alive


def main() -> None:
    assert life(set(), 3) == set()
    assert life({(0, 0)}, 1) == set()
    block = {(0, 0), (1, 1), (0, 1), (1, 0)}

    blinker_0 = {(0, -1), (0, 0), (0, 1)}
    blinker_1 = {(-1, 0), (0, 0), (1, 0)}
    glider = blinker_1.copy()
    glider.add((1, -1))
    glider.add((0, -2))

    for i in range(20):
        assert life(block, i) == block, life(block, i)

    for i in range(20):
        expect = blinker_0 if i % 2 == 0 else blinker_1
        assert life(blinker_0, i) == expect

    for i in range(0, 40, 4):
        expect = set()
        for x, y in glider:
            expect.add((x + i // 4, y + i // 4))
        assert life(glider, i) == expect, (i, life(glider, i), expect)


if __name__ == "__main__":
    main()
