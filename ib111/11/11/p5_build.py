from ib111 import week_11  # noqa


# † V tomto příkladu budeme pracovat s n-árními stromy, které nemají
# v uzlech žádné hodnoty (mají pouze stromovou strukturu).
# Třídu Tree nijak nemodifikujte.

class Tree:
    def __init__(self) -> None:
        self.children: list[Tree] = []


# Napište (čistou) funkci, které na základě dobře uzávorkovaného
# řetězce tvořeného pouze znaky ‹(› a ‹)› vybuduje instanci výše
# popsaného stromu, a to tak, že každý pár závorek reprezentuje
# jeden uzel, a jejich obsah reprezentuje podstrom, který v tomto
# uzlu začíná. Ve vstupním řetězci bude vždy alespoň jeden pár
# závorek.


def build_tree_rec(brackets: list[str]) -> Tree:
    val = brackets.pop()
    if val == '(':
        tree: Tree = Tree()
        while val == '(':
            subtree = build_tree_rec(brackets)
            tree.children.append(subtree)
            val = brackets.pop()
    return tree


def reverse(lis: list[str]) -> None:
    for i in range(len(lis) // 2):
        lis[i], lis[len(lis) - i - 1] = lis[len(lis) - i - 1], lis[i]


def build_tree(brackets: str) -> Tree:
    help: Tree = Tree()
    brackets: list[str] = reverse(brackets)
    tree, _ = build_tree_rec(help, brackets)
    return tree.children[0]


def main() -> None:
    t2 = build_tree("()")
    assert len(t2.children) == 0

    t3 = build_tree("(()(()())(()))")
    print(len(t3.children))
    assert len(t3.children) == 3
    assert len(t3.children[0].children) == 0
    assert len(t3.children[1].children) == 2
    assert len(t3.children[1].children[0].children) == 0
    assert len(t3.children[1].children[1].children) == 0
    assert len(t3.children[2].children) == 1
    assert len(t3.children[2].children[0].children) == 0

    t4 = build_tree("(((())))")
    assert len(t4.children) == 1
    assert len(t4.children[0].children) == 1
    assert len(t4.children[0].children[0].children) == 1
    assert len(t4.children[0].children[0].children[0].children) == 0


if __name__ == '__main__':
    main()
