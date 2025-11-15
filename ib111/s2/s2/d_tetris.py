from ib111 import week_07  # noqa

# Jistě už jste někdy slyšeli o hře Tetris. Pokud ne, vítejte v civilizaci!
# Hledat můžete začít například tady: ‹https://duckduckgo.com/?q=tetris›.
# V tomto domácím úkolu si klon této hry naprogramujete.
#
# Abyste si hru mohli vyzkoušet (poté, co implementujete všechny níže
# uvedené metody), je vám k dispozici soubor ‹game_tetris.py›, který vložte do
# stejného adresáře, jako je soubor s vaším řešením, případně jej upravte
# dle komentářů na jeho začátku a spusťte.
# Hra se ovládá těmito klávesami:
#
# • pohyb doleva: šipka doleva nebo ‹A›,
# • pohyb doprava: šipka doprava nebo ‹D›,
# • pohyb dolů: šipka dolů nebo ‹S› (děje se také automaticky s nastavenou
#   prodlevou),
# • rychlý pád dolů: mezerník,
# • otočení proti směru hodinových ručiček: ‹Q› nebo Page Up,
# • otočení po směru hodinových ručiček: ‹E› nebo Page Down,
# • ukončení hry: ‹X›,
# • restart: ‹R›.
#
# Třída ‹Tetris›, kterou máte implementovat, reprezentuje stav hry, tj. obsah
# herní oblasti (již spadlé kostky), aktuálně padající blok, jeho pozici
# a aktuální skóre. Způsob reprezentace je na vás. Testy i grafické rozhraní
# používají ke komunikaci s vaší třídou pouze zde popsané metody.
#
# Rozměry herní oblasti budou zadány při inicializaci (funkci ‹__init__›).
# Všechny pozice mimo zadané rozměry považujeme za neprostupnou zeď.
# Souřadnice zde používáme ve tvaru (sloupec, řádek), přičemž pozice (0, 0)
# je v levém horním rohu herní oblasti. Čísla sloupců rostou zleva doprava,
# čísla řádků shora dolů.
#
# Padající bloky reprezentujeme seznamem relativních souřadnic, přičemž (0, 0)
# je střed otáčení. Tedy např. ‹[(-1, 0), (0, 0), (1, 0), (0, 1)]› je tetromino
# tvaru T otočené směrem dolů, které se bude otáčet kolem své prostřední
# kostky. Blok ‹[(-1, -1), (0, -1), (1, -1), (0, 0)]› má stejný tvar, ale otáčí
# se kolem své „spodní nožičky“. Střed otáčení nemusí být nutně součástí bloku,
# např. ‹[(-1, -1), (-1, 0), (-1, 1), (0, 1)]› je tetromino tvaru L, které se
# otáčí kolem prázdného místa ve svém rohu.
#
# Přestože se v grafickém rozhraní používají pouze tetromina (tedy klasické
# tetrisové bloky), vaše řešení musí být obecné a fungovat s libovolnými tvary
# bloků.
#
# «Poznámka:» Protože za zeď považujeme i prostor „nad“ herní oblastí, může se
# v mnoha případech stát, že blok, který se nově objevil, nebude možné otočit,
# dokud se neposune o něco níže. Ačkoli reálné implementace tuto možnost
# většinou nějak ošetřují, zde pro zjednodušení nic takového neděláme
# a považujeme to za očekávané chování.

Position = tuple[int, int]


class Tetris:

    # Po inicializaci by měla být herní oblast prázdná, o zadaných rozměrech.
    # Není žádný padající blok a skóre je nastaveno na 0.

    def __init__(self, cols: int, rows: int):
        self.board = [[False for _ in range(cols)] for _ in range(rows)]
        self.score = 0
        self.is_block_falling = False
        self.rows = rows
        self.cols = cols
        self.current_block: list[Position] = []
        self.middle = (0, 0)

    # Čistá metoda ‹get_score› vrátí aktuální skóre.

    def get_score(self) -> int:
        return self.score

    # Metoda-predikát ‹has_block› vrátí ‹True› právě tehdy, existuje-li
    # padající blok.

    def has_block(self) -> bool:
        return self.is_block_falling

    # Metoda ‹add_block› přidá do hry padající blok na zadaných souřadnicích.
    # Pokud přidání bloku není možné (překrýval by se s již položenými
    # kostkami), metoda situaci nezmění a vrátí ‹False›; jinak vrátí ‹True›.
    # Metoda bude volána pouze tehdy, neexistuje-li žádný padající blok.
    # Seznam ‹block› nijak nemodifikujte. Pokud si ho hodláte někam uložit,
    # tak buďto zaříďte, aby se ani později nemodifikoval, nebo si vytvořte
    # jeho kopii.

    def add_block(self, block: list[Position],
                  col: int, row: int) -> bool:
        if self.is_block_falling:
            return False

        for c, r in block:
            if (
                col + c < 0
                or col + c >= self.cols
                or row + r < 0
                or row + r >= self.rows
            ):
                return False
            if self.board[row + r][col + c]:
                return False

        self.middle = (col, row)
        self.is_block_falling = True
        for c, r in block:
            self.board[row + r][col + c] = True
            self.current_block.append((col + c, row + r))

        return True

    # Metoda ‹left› posune padající blok o jednu pozici doleva, je-li to možné.
    # Tato metoda, stejně jako všechny následující metody pohybu, bude volána
    # jen tehdy, existuje-li padající blok.

    def left(self) -> None:
        if not self.is_block_falling:
            return

        current = set(self.current_block)
        for c, r in self.current_block:
            if c <= 0:
                return
            if self.board[r][c - 1] and (c - 1, r) not in current:
                return

        new_pos: list[Position] = list(self.current_block)

        c_m, r_m = self.middle
        c_m -= 1
        self.middle = (c_m, r_m)
        pieces = set()
        for c, r in new_pos:
            pieces.add((c - 1, r))

        for c, r in new_pos:
            if (c, r) not in pieces:
                self.board[r][c] = False
            self.board[r][c - 1] = True

        new_current: list[Position] = []
        for c, r in new_pos:
            new_current.append((c - 1, r))
        self.current_block = new_current

    # Metoda ‹right› posune padající blok o jednu pozici doprava,
    # je-li to možné.

    def right(self) -> None:
        if not self.is_block_falling:
            return

        current = set(self.current_block)
        for c, r in self.current_block:
            if c + 1 >= self.cols:
                return
            if self.board[r][c + 1] and (c + 1, r) not in current:
                return

        new_pos: list[Position] = list(self.current_block)

        c_m, r_m = self.middle
        c_m += 1
        self.middle = (c_m, r_m)
        pieces = set()
        for c, r in new_pos:
            pieces.add((c + 1, r))

        for c, r in new_pos:
            if (c, r) not in pieces:
                self.board[r][c] = False
            self.board[r][c + 1] = True

        new_current: list[Position] = []
        for c, r in new_pos:
            new_current.append((c + 1, r))
        self.current_block = new_current

    # Metoda ‹rotate_cw› otočí padající blok po směru hodinových ručiček o 90
    # stupňů, je-li to možné.

    def rotate_cw(self) -> None:
        if not self.is_block_falling:
            return

        new_pos: list[Position] = list(self.current_block)
        c_m, r_m = self.middle

        current = set(new_pos)
        pieces = set()
        for c, r in new_pos:
            col_n = c_m - r + r_m
            row_n = r_m + c - c_m

            if (
                col_n < 0
                or col_n >= self.cols
                or row_n < 0
                or row_n >= self.rows
            ):
                return

            if self.board[row_n][col_n] and (col_n, row_n) not in current:
                return

            pieces.add((col_n, row_n))

        for c, r in new_pos:
            if (c, r) not in pieces:
                self.board[r][c] = False
            col_n = c_m - r + r_m
            row_n = r_m + c - c_m
            self.board[row_n][col_n] = True

        new_current: list[Position] = []
        for c, r in new_pos:
            col_n = c_m - r + r_m
            row_n = r_m + c - c_m
            new_current.append((col_n, row_n))
        self.current_block = new_current

    # Metoda ‹rotate_ccw› otočí padající blok proti směru hodinových ručiček
    # o 90 stupňů, je-li to možné.

    def rotate_ccw(self) -> None:
        if not self.is_block_falling:
            return

        new_pos: list[Position] = list(self.current_block)
        c_m, r_m = self.middle
        pieces = set()

        current = set(new_pos)
        for c, r in new_pos:
            col_n = c_m + r - r_m
            row_n = r_m - c + c_m

            if (
                col_n < 0
                or col_n >= self.cols
                or row_n < 0
                or row_n >= self.rows
            ):
                return

            if self.board[row_n][col_n] and (col_n, row_n) not in current:
                return

            pieces.add((col_n, row_n))

        for c, r in new_pos:
            if (c, r) not in pieces:
                self.board[r][c] = False
            col_n = c_m + r - r_m
            row_n = r_m - c + c_m
            self.board[row_n][col_n] = True

        new_current: list[Position] = []
        for c, r in new_pos:
            col_n = c_m + r - r_m
            row_n = r_m - c + c_m
            new_current.append((col_n, row_n))
        self.current_block = new_current

    def erase_rows(self) -> None:
        self.is_block_falling = False
        self.current_block = []

        while True:
            rows_to_del = {}

            for row in range(self.rows):
                full = True
                for col in range(self.cols):
                    if not self.board[row][col]:
                        full = False
                        break
                if full:
                    rows_to_del[row] = True
            if rows_to_del == {}:
                break

            new_score = 0
            for row, to_del in rows_to_del.items():
                if to_del:
                    for col in range(self.cols):
                        self.board[row][col] = False
                    new_score += 1

                    for row_d in range(row - 1, -1, -1):
                        for col in range(self.cols):
                            self.board[row_d + 1][col] = self.board[row_d][col]
                    for col in range(self.cols):
                        self.board[0][col] = False
            self.score += new_score ** 2

    # Metoda ‹down› posune padající blok o jednu pozici směrem dolů.
    # Pokud takový posun není možný, kostky z padajícího bloku se napevno
    # umístí do herní oblasti; zcela zaplněné řádky se pak z oblasti vymažou
    # a skóre se zvýší o druhou mocninu počtu vymazaných řádků.

    def down(self) -> None:
        if not self.is_block_falling:
            return

        cur = list(self.current_block)
        for c, r in cur:
            if r + 1 >= self.rows:
                self.erase_rows()
                return
            if (
                (c, r + 1) not in set(cur)
                and self.board[r + 1][c]
            ):
                self.erase_rows()
                return

        c_m, r_m = self.middle
        r_m += 1
        self.middle = (c_m, r_m)

        pieces = set()

        for c, r in cur:
            pieces.add((c, r + 1))

        for c, r in cur:
            if (c, r) not in pieces:
                self.board[r][c] = False
            self.board[r + 1][c] = True

        new_current: list[Position] = []
        for c, r in cur:
            new_current.append((c, r + 1))
        self.current_block = new_current

    # Metoda ‹drop› shodí padající blok směrem dolů (o tolik pozic, o kolik je
    # to možné). Kostky z padajícího bloku se pak napevno umístí do herní
    # oblasti; zcela zaplněné řádky se pak z oblasti vymažou a skóre se zvýší
    # o druhou mocninu počtu vymazaných řádků.

    def drop(self) -> None:
        while self.is_block_falling:
            self.down()

    # Čistá metoda ‹tiles› vrátí seznam všech pozic, na nichž má být vykreslena
    # kostka – tedy jednak všechny položené kostky v herní oblasti, jednak
    # všechny kostky tvořící padající blok. Na pořadí pozic v seznamu nezáleží.
    # Tuto metodu používají jak testy pro ověření správnosti implementace,
    # tak grafické rozhraní pro vykreslení hry.

    def tiles(self) -> list[Position]:
        positions: list[Position] = []

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c]:
                    positions.append((c, r))

        return positions


def main() -> None:
    tetris = Tetris(10, 22)

    assert tetris.get_score() == 0
    assert not tetris.has_block()
    assert tetris.tiles() == []

    block_s = [(1, -1), (0, -1), (0, 0), (-1, 0)]

    assert not tetris.add_block(block_s, 4, 0)
    assert not tetris.has_block()

    assert tetris.add_block(block_s, 4, 1)
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(3, 1), (4, 0), (4, 1), (5, 0)}
    assert len(tetris.tiles()) == 4

    tetris.down()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(3, 2), (4, 1), (4, 2), (5, 1)}
    assert len(tetris.tiles()) == 4

    tetris.left()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(2, 2), (3, 1), (3, 2), (4, 1)}
    assert len(tetris.tiles()) == 4

    tetris.right()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(3, 2), (4, 1), (4, 2), (5, 1)}
    assert len(tetris.tiles()) == 4

    tetris.right()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(4, 2), (5, 1), (5, 2), (6, 1)}
    assert len(tetris.tiles()) == 4

    tetris.rotate_cw()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(5, 1), (5, 2), (6, 2), (6, 3)}
    assert len(tetris.tiles()) == 4

    tetris.rotate_ccw()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(4, 2), (5, 1), (5, 2), (6, 1)}
    assert len(tetris.tiles()) == 4

    tetris.rotate_ccw()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(4, 1), (4, 2), (5, 2), (5, 3)}
    assert len(tetris.tiles()) == 4
    tetris.drop()
    assert not tetris.has_block()
    assert set(tetris.tiles()) == {(4, 19), (4, 20), (5, 20), (5, 21)}
    assert len(tetris.tiles()) == 4

    assert tetris.get_score() == 0
    assert block_s == [(1, -1), (0, -1), (0, 0), (-1, 0)]


if __name__ == '__main__':
    main()
