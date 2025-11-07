from ib111 import week_07  # noqa


# Hashovací tabulka je datová struktura, která umožňuje rychlé
# ukládání a vyhledávání hodnot. Základem je hashovací funkce, která
# určí přihrádku, do níž hodnota patří. V každé přihrádce je pak
# jednosměrně zřetězený seznam obsahující hodnoty v dané přihrádce.
#
# V našem příkladu budeme používat hashovací funkci modulo,
# konkrétní hodnota modulu bude stanovena při vytváření hashovací
# tabulky jako parametr inicializační funkce.
#
# Vaším úkolem bude implementovat třídu ‹HashTable›:
#
#  • Inicializační funkce ‹__init__› vytvoří seznam (typ ‹list›)
#    o ‹m› přihrádkách. Každá přihrádka je na začátku tvořená
#    prázdným zřetězeným seznamem.
#  • Metodu ‹insert›, která vloží hodnotu do správné přihrádky.
#    Vstupní podmínkou je, že hodnota v tabulce není přítomna. Tuto
#    metodu implementujte co nejefektivněji.
#  • Metodu ‹contains›, která zjistí, zda se daná hodnota v tabulce
#    vyskytuje, či nikoliv.
#  • Metodu ‹remove›, která zadanou hodnotu z tabulky odebere.
#  • Metodu ‹bucket›, která pro zadaný klíč vrátí hlavu zřetězeného
#    seznamu, který tvoří klíči příslušnou přihrádku (bez ohledu na
#    přítomnost klíče v tabulce), nebo ‹None› je-li tato prázdná.
#
# Třídu ‹Node› nijak neměňte. Tabulka musí fungovat i v případě, že
# je seznam vrácený metodou ‹bucket› nějak upraven.


class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.next: Node | None = None


class HashTable:
    def __init__(self, m: int) -> None:
        self.table: list[Node | None] = [None for _ in range(m)]
        self.hash = m

    def insert(self, key: int) -> None:
        node: Node | None = self.table[key % self.hash]

        if node is None:
            self.table[key % self.hash] = Node(key)
            return

        node = Node(key)
        node.next = self.table[key % self.hash]
        self.table[key % self.hash] = node

    def contains(self, key: int) -> bool:
        node: Node | None = self.table[key % self.hash]

        while node is not None:
            if node.key == key:
                return True
            node = node.next

        return False

    def remove(self, key: int) -> None:
        node: Node | None = self.table[key % self.hash]

        if node is None:
            return
        if node.key == key:
            self.table[key % self.hash] = node.next
            return

        while node.next is not None:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def bucket(self, key: int) -> Node | None:
        return self.table[key % self.hash]


def main() -> None:
    ht = HashTable(7)
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8,
            10, 12, 14, 16, 18, 20, 22,
            23, 25, 31, 33, 34, 35, 36,
            39, 41, 44, 47, 50]

    ht.insert(333)
    node = ht.bucket(333)
    assert node is not None
    assert node.key == 333
    assert node.next is None
    assert ht.bucket(3) is None

    for i in keys:
        ht.insert(i)

    node = ht.bucket(4)
    seen: set[int] = set()

    while node is not None:
        seen.add(node.key)
        node = node.next
    assert seen == {4, 18, 25, 39, 333}

    for i in keys:
        assert ht.contains(i)

    present = set(keys)
    to_remove = [23, 25, 31, 33, 34, 35, 36,
                 0, 1, 2, 3, 4, 5, 6, 7, 8,
                 10, 12, 14, 16, 18, 20, 22,
                 39, 41, 44, 47, 50]

    for i in to_remove:
        for j in keys:
            assert ht.contains(j) == (j in present)
        ht.remove(i)
        present.remove(i)

    for i in range(40):
        assert not ht.contains(i)

    for i in keys:
        ht.insert(i)

    node = ht.bucket(4)
    assert node is not None
    assert ht.contains(4) and ht.contains(18)
    node.next = None
    assert not ht.contains(4) or not ht.contains(18)


if __name__ == "__main__":
    main()
