
from collections import deque

# --- Implementacni test 24. 5. 2018: Bludiste ---
#
# V tomto prikladu budeme pracovat s bludistem reprezentovanym ctvercovou siti.
# Bludiste je objekt typu Maze, viz nize.
# Pohyb v bludisti je mozny nejvyse ctyrmi smery (nahoru, dolu, doleva,
# doprava). Zdi nejsou pruchozi.
# Nasledujici konstanty reprezentuji ruzne druhy mist v bludisti.
# Muzete je pouzit ve svem kodu pro lepsi citelnost a prehlednost.
# Znaky START, TREASURE a PATH se pouzivaji jen v poslednim ukolu.
WALL = "#" # tento znak reprezentuje zed (neni pruchozi)
EMPTY = "." # tento znak reprezentuje chodbu (pruchozi misto)
START = "?" # tento znak reprezentuje pocatecni pozici (jen pro 4. ukol)
TREASURE = "$" # tento znak reprezentuje poklad (jen pro 4. ukol)
PATH = "*" # timto znakem budete ve 4. ukolu znacit cestu
# V ukolech 1, 2 a 3 bude zadane bludiste vzdy obsahovat jen znaky WALL a
# EMPTY. V ukolu 4 bude zadane bludiste navic obsahovat prave jeden znak START
# a libovolny pocet znaku TREASURE.
class Maze:
    """Trida Maze slouzi k reprezentaci bludiste. Nijak ji nemodifikujte.
    Atributy:
    rows pocet radku ctvercove site (vzdy alespon 3)
    cols pocet sloupcu ctvercove site (vzdy alespon 3)
    map 2D matice s obsahem bludiste
    Rozmer matice map je rows krat cols.
    Pro lepsi praci s bludistem bude zaruceno, ze okrajova mista jsou zdi,
    tedy na souradnicich [0][x], [rows - 1][x], [y][0] a [y][cols - 1] je vzdy
    zed (WALL) pro vsechna x, y.
    K textovemu vykreslovani bludiste muzete pouzit funkci print_maze
    (definovanou na zacatku testu nize); funkce bere jeden parametr typu Maze."""
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.maze = [["#" for _ in range(cols)] for _ in range(rows)]
# Priklad bludiste s indexy:
# Nasledujici bludiste ma rows = 9, cols = 17, matice ma tedy rozmery 9x17 a
# obsahuje indexy radku 0..8 a indexy sloupcu 0..16. Na indexech [0][.],
# [8][.], [.][0], [.][16] se tedy zarucene nachazeji zdi.
#
# sloupce
# 1111111
# 01234567890123456
# 0 #################
# 1 #.......#.......#
# r 2 #.#######.##.##.#
# a 3 #.#.....#.#..$#.# na pozici [3][13] se nachazi znak TREASURE
# d 4 #.#.###.#.##.##.#
# k 5 #.#...#.#.......#
# y 6 #.#####.#######.#
# 7 #.......#..?....# na pozici [7][11] se nachazi znak START
# 8 #################
# Ukol 1. (15 bodu)
# Implementujte funkce neigbours (5 bodu) a count_directions (10 bodu).
# Funkce neighbours vrati k zadanym souradnicim seznam souradnic vsech
# sousedu, napr. sousede (1, 3) jsou (0, 3), (1, 2), (2, 3), (1, 4);
# ve vyslednem seznamu mohou byt v libovolnem poradi.
def neighbours(row, col):
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)] # TODO

# Funkce count_directions kazde prazdne misto (EMPTY) v matici bludiste nahradi
# cislem od 0 do 4 reprezentujicim pocet smeru, kterymi se z daneho mista da
# odejit.
#
# Priklad: vstup vysledne bludiste
# ####### #######
# #...### ---> #231###
# #..##.# #22##0#
# ####### #######
def count_directions(maze: Maze):
    for i in range(1, maze.rows - 1):
        for j in range(1, maze.cols - 1):
            if maze.maze[i][j] == EMPTY:
                count = 0
                for x, y in neighbours(i, j):
                    if maze.maze[x][y] != WALL:
                        count += 1
                maze.maze[i][j] = count


# Ukol 2. (20 bodu)
# Implementuje funkci separate_areas, ktera vrati pocet oddelenych oblasti
# bludiste, tj. takovych, mezi kterymi se vzajemne neda prechazet.
#
# Priklad:
# jedna oddelena oblast dve oddelene oblasti zadna oddelena oblast
# ######## ######## ########
# #.###..# #...#.## ########
# #......# #.#.#.## ########
# #.#.##.# #...#..# ########
# ######## ######## ########

def bfs(maze: Maze, visited: set[tuple[int, int]], i: int, j: int) -> None:
    queue: deque = deque()
    visited.add((i, j))
    queue.append((i, j))

    while len(queue) != 0:
        v: tuple[int, int] = queue.popleft()
        x, y = v
        if maze.maze[x][y] == WALL:
            continue
        for nx, ny in neighbours(x, y):
            if (maze.maze[nx][ny] == WALL):
                continue
            if ((nx, ny) in visited):
                continue
            visited.add((nx, ny))
            queue.append((nx, ny))
        
        visited.add(v)

def separate_areas(maze: Maze) -> int:
    count: int = 0
    visited: set[tuple[int, int]] = set()

    for i in range(1, maze.rows - 1):
        for j in range(1, maze.cols - 1):
            if maze.maze[i][j] == WALL:
                continue
            if (i, j) in visited:
                continue
            count += 1
            bfs(maze, visited, i, j)

    return count

# Ukol 3. (30 bodu)
# Implementujte funkci has_loop, ktera zjisti, zda bludiste obsahuje smycku.
# Smyckou v bludisti zde nazyvame situaci, kdy muzeme vyjit z nektereho volneho
# mista a zase se do nej vratit, pricemz po ceste nenavstivime zadne misto
# vicekrat. Za smycku ovsem nepovazujeme pouhy krok na vedlejsi misto a zpet.
#
# Priklady: ##### #####
# #### ##### #...# #...#
# Tato bludiste neobsahuji smycku: #..# #...# #.#.# ##.##
# #### ##### ##### #...#
# #####
# ##### #####
# #...# #### #.###
# Tato bludiste obsahuji smycku: #.#.# #..# #..##
# #...# #..# #...#
# ##### #### #####

def is_cyclic(maze: Maze, i: int, j: int, visited: set[tuple[int, int]], previ: int, prevj: int) -> bool:
    visited.add((i, j))

    for xn, yn in neighbours(i, j):
        if maze.maze[xn][yn] == WALL:
            continue
        if (xn, yn) in visited and (xn, yn) != (previ, prevj):
            return True
        if (xn, yn) in visited:
            continue
        if is_cyclic(maze, xn, yn, visited, i, j):
            return True

    return False

def has_loop(maze: Maze) -> bool:
    visited: set[tuple[int, int]] = set()
    for i in range(1, maze.rows - 1):
        for j in range(1, maze.cols - 1):
            if maze.maze[i][j] == WALL:
                continue
            if (i, j) in visited:
                continue
            if is_cyclic(maze, i, j, visited, -1, -1):
                return True

    return False

# Ukol 4. (15 + 20 bodu)
# Implementuje funkci find_treasure, ktera v bludisti najde nejkratsi cestu
# od pocatecni pozice (zadane znakem START) k nejblizsimu pokladu (zadanemu
# znakem TREASURE).
# Bludiste zarucene obsahuje presne jeden znak START a muze obsahovat libovolny
# (vcetne 0) pocet znaku TREASURE.
# Zadana funkce jednak vrati delku cesty (15 bodu), jednak cestu do bludiste
# vykresli (20 bodu).
#
# K vykresleni cesty pouzijte symbol PATH, pricemz tento symbol piste pouze do
# volnych mist na nejkratsi ceste z pocatecniho mista k pokladu, symboly START
# a TREASURE ponechte v puvodnim stavu.
# Pokud zadna cesta k pokladu neexistuje, funkce vrati None.
#
# Priklad: vstup vysledne bludiste
# ######### #########
# #.?..##.# #.?**##.#
# #.##.#.$# ---> #.##*#.$# navratova hodnota je 10
# #..#.##.# #..#*##*#
# ##......# ##..****#
# ######### #########

def find_path(maze: Maze, i: int, j: int, paths: list[list[tuple[int, int]]], visited: set[tuple[int, int]], stack: list[int, int]) -> None:
    visited.add((i, j))
    stack.append((i, j))

    for xn, yn in neighbours(i, j):
        if maze.maze[xn][yn] == WALL:
            continue
        if maze.maze[xn][yn] == TREASURE:
            stack.append((xn, yn))
            paths.append(stack.copy())
            visited.remove((i, j))
            stack.pop()
            stack.pop()
            return
        if (xn, yn) in visited:
            continue
        find_path(maze, xn, yn, paths, visited, stack)

    visited.remove((i, j))
    stack.pop()



def find_treasure(maze: Maze) -> int | None:
    paths: list[list[tuple[int, int]]] = []
    visited: set[tuple[int, int]] = set()
    stack: list[tuple[int, int]] = []
    startI: int = -1
    startJ: int = -1
    for i in range(1, maze.rows - 1):
        for j in range(1, maze.cols - 1):
            if maze.maze[i][j] == START:
                startI = i
                startJ = j
                break
        if i != -1:
            break

    find_path(maze, i, j, paths, visited, stack)

    print(paths)

    if len(paths) == 0:
        return None

    best = paths[0]

    for k in range(1, len(paths)):
        if len(paths[k]) < len(best):
            best = paths[k]

    for k in range(1, len(best) - 1):
        x, y = best[k]
        maze.maze[x][y] = PATH

    return len(best) - 1

def main():
    print("Program běží")
    maze = Maze(6, 9)
    rows_data = [
    "#########",
    "#.?..##.#",
    "#.##.#.$#",
    "#..#.##.#",
    "##......#",
    "#########"
    ]

    maze_in = []

    for row in rows_data:
        maze_in.append([ch for ch in row])
    maze.maze = maze_in

    print(find_treasure(maze))
    print(maze.maze)


if __name__ == "__main__":
    main()