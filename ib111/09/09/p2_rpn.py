from ib111 import week_09  # noqa


# V tomto příkladě budeme opět pracovat s aritmetickými výrazy. Tyto
# mají následující strukturu:
#
#  • konstantu reprezentuje strom, který má oba podstromy prázdné,
#  • složený výraz je reprezentován stromem, který má v kořenu
#    uložen operátor (‹+› nebo ‹*›) a jeho neprázdné podstromy
#    reprezentují operandy.
#
# Žádné jiné uzly ve stromě přítomny nebudou.

class Tree:
    def __init__(self, value: str,
                 left: 'Tree | None',
                 right: 'Tree | None'):
        self.value = value
        self.left = left
        self.right = right


def leaf(value: str) -> Tree:
    return Tree(value, None, None)


# Napište čistou funkci, která dostane jako parametr instanci výše
# uvedeného stromu reprezentující nějaký aritmetický výraz, a vrátí
# seznam řetězců, ve kterém je tento výraz zapsán v postfixové (rpn)
# notaci. Každý prvek bude odpovídat právě jednomu uzlu vstupního
# stromu.

def to_rpn_rec(tree: Tree | None, result: list[str]) -> None:
    if tree is None:
        return

    to_rpn_rec(tree.left, result)
    to_rpn_rec(tree.right, result)
    result.append(tree.value)


def to_rpn(tree: Tree) -> list[str]:
    result: list[str] = []
    to_rpn_rec(tree, result)
    return result


def main() -> None:
    t1 = leaf("5")
    t2 = Tree("+", leaf("2"), leaf("4"))
    t3 = Tree("*", t1, t2)
    t4 = Tree("+", t3, leaf("0"))

    assert to_rpn(t1) == ["5"]
    assert to_rpn(t2) == ["2", "4", "+"]
    assert to_rpn(t3) == ["5", "2", "4", "+", "*"]
    assert to_rpn(t4) == ["5", "2", "4", "+", "*", "0", "+"]


if __name__ == '__main__':
    main()
