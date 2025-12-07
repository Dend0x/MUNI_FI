from ib111 import week_10  # noqa

# «Malované křížovky¹» (nonogramy) jsou logické hlavolamy, u kterých je cílem
# vybarvit některá políčka čtvercové sítě podle zadané číselné legendy.
# Výsledkem je typicky jednoduchý obrázek. Existují různé druhy malovaných
# křížovek, v této úloze nás budou zajímat pouze ty základní černobílé.
#
# ¹ ‹https://en.wikipedia.org/wiki/Nonogram›
#
# Zadání malované křížovky vypadá např. takto:
#
#  ┌──────────────────────────────┐
#  │               1              │
#  │               2     1  1     │
#  │         1  2  1  4  2  1  3  │
#  │       ┌──┬──┬──┬──┬──┬──┬──┐ │
#  │     1 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │ 1 1 1 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     7 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   2 1 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     3 │  │  │  │  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   1 1 │  │  │  │  │  │  │  │ │
#  │       └──┴──┴──┴──┴──┴──┴──┘ │
#  └──────────────────────────────●
#
# Číselná legenda u řádků a sloupců ukazuje, kolik políček máme v dané řadě
# (řádku nebo sloupci) vybarvit a jak mají být vybarvená políčka seskupena.
# Pokud bychom tedy například měli legendu «1 3 2» a řádek délky 9 políček,
# pak jej můžeme vyplnit jedním z těchto způsobů:
#
#  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
#  │▓▓│  │▓▓│▓▓│▓▓│  │▓▓│▓▓│  │
#  └──┴──┴──┴──┴──┴──┴──┴──┴──┘
#  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
#  │▓▓│  │▓▓│▓▓│▓▓│  │  │▓▓│▓▓│
#  └──┴──┴──┴──┴──┴──┴──┴──┴──┘
#  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
#  │▓▓│  │  │▓▓│▓▓│▓▓│  │▓▓│▓▓│
#  └──┴──┴──┴──┴──┴──┴──┴──┴──┘
#  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
#  │  │▓▓│  │▓▓│▓▓│▓▓│  │▓▓│▓▓│
#  └──┴──┴──┴──┴──┴──┴──┴──┴──┘
#
# Řešením malované křížovky je vybarvení políček takové, že každý řádek
# a každý sloupec odpovídá zadané legendě. Výše uvedený příklad má tedy
# následující (jediné) řešení:
#
#  ┌──────────────────────────────┐
#  │               1              │
#  │               2     1  1     │
#  │         1  2  1  4  2  1  3  │
#  │       ┌──┬──┬──┬──┬──┬──┬──┐ │
#  │     1 │  │  │▓▓│  │  │  │  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │ 1 1 1 │  │▓▓│  │▓▓│  │  │▓▓│ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     7 │▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   2 1 │  │  │▓▓│▓▓│  │  │▓▓│ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │     3 │  │  │  │▓▓│▓▓│▓▓│  │ │
#  │       ├──┼──┼──┼──┼──┼──┼──┤ │
#  │   1 1 │  │  │▓▓│  │▓▓│  │  │ │
#  │       └──┴──┴──┴──┴──┴──┴──┘ │
#  └──────────────────────────────●
#
# V této úloze si zkusíte napsat program, který bude schopen některé jednodušší
# malované křížovky řešit pomocí techniky backtrackingu. Jednotlivá políčka
# křížovky budeme reprezentovat typem ‹Pixel›, což je zde typový alias pro
# ‹int› použitý pouze pro lepší čitelnost anotací.

Pixel = int
EMPTY, FULL, UNKNOWN = 0, 1, 2

# Máme zde připravené globální konstanty ‹EMPTY› (reprezentuje prázdné
# políčko), ‹FULL› (reprezentuje vybarvené políčko), ‹UNKNOWN› (reprezentuje
# neznámý stav políčka). Počet různých druhů políček si můžete pro účely
# implementace případně rozšířit, ale tyto tři konstanty zachovejte.
#
# Dále máme připraven typový alias pro číselnou legendu. Legenda pro řádky bude
# v seznamu uložená zleva doprava, legenda pro sloupce shora dolů.

Clue = list[int]


# Nakonec je připravena třída ‹Picture›, která bude reprezentovat výsledný
# obrázek. Tuto třídu můžete libovolně upravovat (přidávat vlastní atributy
# a metody), ale zachovejte parametry metody ‹__init__› i způsob inicializace
# atributů ‹height›, ‹width› a ‹pixels›.

class Picture:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.pixels = [[UNKNOWN for _ in range(width)]
                       for _ in range(height)]


# Nejprve implementujte čistou funkci ‹gen_lines_with_prefix›, která vrátí
# seznam všech řad délky ‹size›, které odpovídají zadané legendě (‹clue›)
# a zároveň začínají zadaným prefixem (‹prefix›). Předpokládejte, že ‹prefix›
# má délku nejvýše ‹size› a obsahuje pouze hodnoty ‹EMPTY› a ‹FULL›.
# Na pořadí seznamů uvnitř vnějšího seznamu nezáleží.
#
# «Nápověda:» Využijte backtracking. Zkuste začít implementací pro situace,
# kdy je ‹prefix› prázdný, a tuto implementaci pak rozšiřte.

def get_lines_with_prefix_rec(old_size: int, index: int, clue: Clue,
                              result: list[list[Pixel]],
                              current: list[Pixel]) -> None:
    if index == len(clue):
        left = old_size - len(current)
        if left < 0:
            return
        for _ in range(left):
            current.append(EMPTY)
        result.append(current.copy())
        for _ in range(left):
            current.pop()
        return

    if len(current) > old_size:
        return

    sum_clue = 0

    for j in range(index, len(clue)):
        sum_clue += clue[j]

    left = old_size - len(current)
    if index < len(clue):
        remain = len(clue) - index
    else:
        remain = 0
    if remain > 0:
        remain -= 1
    need_more = sum_clue + remain

    for i in range(left - need_more + 1):
        for _ in range(i):
            current.append(EMPTY)
        if index < len(clue):
            for _ in range(clue[index]):
                current.append(FULL)
        changed = False
        if index < len(clue) - 1:
            current.append(EMPTY)
            changed = True

        get_lines_with_prefix_rec(old_size, index + 1, clue, result, current)

        if changed:
            current.pop()
        if index < len(clue):
            for _ in range(clue[index]):
                current.pop()

        for _ in range(i):
            current.pop()


def gen_lines_with_prefix(clue: Clue, size: int,
                          prefix: list[Pixel]) -> list[list[Pixel]]:
    if len(prefix) > size:
        return []
    result: list[list[Pixel]] = []
    current: list[Pixel] = []
    actual = 0
    in_clue = False
    clue = clue.copy()

    parts: list[tuple[int, bool]] = []
    index = 0

    while index < len(prefix):
        if prefix[index] == FULL:
            new = old = index
            while new < len(prefix) and prefix[new] == FULL:
                new += 1
            is_full = new < len(prefix) and prefix[new] == EMPTY
            parts.append((new - old, is_full))
            index = new
        else:
            index += 1

    if prefix and prefix[-1] == EMPTY:
        for i, part in enumerate(parts):
            length, _ = part
            if i >= len(clue) or length != clue[i]:
                return []

    for i, part in enumerate(parts):
        length, is_full = part
        if i >= len(clue) or length > clue[i]:
            return []
        if is_full and length != clue[i]:
            return []

    if sum(clue) + len(clue) - 1 > size:
        return []

    for pix in prefix:
        if pix == FULL:
            if not in_clue:
                in_clue = True
            clue[actual] -= 1
        else:
            if in_clue:
                in_clue = False
                actual += 1
        current.append(pix)

    if prefix and prefix[-1] == FULL:
        if actual >= len(clue):
            return []
        for _ in range(clue[actual]):
            current.append(FULL)
            clue[actual] -= 1
        actual += 1
        if actual < len(clue) and len(current) < size:
            current.append(EMPTY)
    get_lines_with_prefix_rec(size, actual, clue, result, current)
    return result


# Dále implementujte čistou funkci ‹solve›, která najde řešení malované
# křížovky se zadanou legendou. Pokud žádné řešení neexistuje, vrátí ‹None›.
# Pokud existuje více než jedno řešení, vrátí libovolné z nich.
#
# «Nápověda:» Využijte backtracking. Použijte funkci ‹gen_lines_with_prefix›.
# Začněte v levém horním rohu. Střídejte řádky a sloupce. V testech budeme
# používat jen takové vstupy, které se tímto přístupem dají dostatečně rychle
# vyřešit.


def solve_rec_c(row: int, col: int, rows: list[Clue],
                cols: list[Clue], pic: Picture) -> bool:
    if row >= pic.height and col >= pic.width:
        return True

    if col >= pic.width:
        return solve_rec_r(row, col + 1, rows, cols, pic)
    prefix_c = []
    r = 0

    while r < pic.height and pic.pixels[r][col] != UNKNOWN:
        prefix_c.append(pic.pixels[r][col])
        r += 1

    options_c = gen_lines_with_prefix(cols[col], pic.height, prefix_c)

    for option in options_c:
        for r in range(pic.height):
            pic.pixels[r][col] = option[r]
        if solve_rec_r(row, col + 1, rows, cols, pic):
            return True
        for r in range(len(prefix_c)):
            pic.pixels[r][col] = prefix_c[r]
        for r in range(len(prefix_c), pic.height):
            pic.pixels[r][col] = UNKNOWN

    return False


def solve_rec_r(row: int, col: int, rows: list[Clue],
                cols: list[Clue], pic: Picture) -> bool:
    if row >= pic.height and col >= pic.width:
        return True

    if row >= pic.height:
        return solve_rec_c(row + 1, col, rows, cols, pic)
    prefix_r = []
    c = 0

    while c < pic.width and pic.pixels[row][c] != UNKNOWN:
        prefix_r.append(pic.pixels[row][c])
        c += 1

    options_r = gen_lines_with_prefix(rows[row], pic.width, prefix_r)

    for option in options_r:
        pic.pixels[row] = option
        if solve_rec_c(row + 1, col, rows, cols, pic):
            return True
        pic.pixels[row] = prefix_r
        for _ in range(len(option) - len(prefix_r)):
            pic.pixels[row].append(UNKNOWN)

    return False


def solve(rows: list[Clue], cols: list[Clue]) -> Picture | None:
    pic: Picture = Picture(len(rows), len(cols))
    if solve_rec_r(0, 0, rows, cols, pic):
        return pic
    return None


def main() -> None:
    # --- empty prefix ---

    assert sorted(gen_lines_with_prefix([1, 3, 2], 9, [])) == [
        [0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0],
    ]

    assert sorted(gen_lines_with_prefix([1], 4, [])) == [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0],
    ]

    assert gen_lines_with_prefix([], 10, []) \
        == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert gen_lines_with_prefix([1, 1, 1, 1], 6, []) == []

    assert gen_lines_with_prefix([1, 1, 1, 1], 7, []) \
        == [[1, 0, 1, 0, 1, 0, 1]]

    assert gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 64, []) \
        == [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
             1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    assert len(gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 67,
                                     [])) == 286

    # --- non-empty prefix ---

    assert sorted(gen_lines_with_prefix([1, 3, 2], 9, [1, 0, 1])) == [
        [1, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0],
    ]

    assert sorted(gen_lines_with_prefix([1], 4, [0])) == [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]

    assert gen_lines_with_prefix([], 10, [0, 0, 0]) \
        == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert gen_lines_with_prefix([1, 1, 1, 1], 7, [0]) == []

    assert gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 1000, [1, 1]) == []

    assert len(gen_lines_with_prefix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                     100,
                                     [0 for _ in range(32)])) == 1001

    # --- solve ---
    pic = solve([[1], [1, 1, 1], [7], [2, 1], [3], [1, 1]],
                [[1], [2], [1, 2, 1], [4], [1, 2], [1, 1], [3]])

    assert pic is not None
    assert pic.width == 7
    assert pic.height == 6
    assert pic.pixels == [
        [0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
    ]

    assert solve([[2], [], [2]], [[1, 1], [2]]) is None

    pic = solve([[2], [], [2]], [[1, 1], [1, 1]])
    assert pic is not None
    assert pic.width == 2
    assert pic.height == 3
    assert pic.pixels == [[1, 1], [0, 0], [1, 1]]


if __name__ == '__main__':
    main()
