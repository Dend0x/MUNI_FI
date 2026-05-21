#!/usr/bin/env python3

# Povolené knihovny: typing, math

from typing import TextIO

# IB002 Domácí úloha 7
#
# V tomto úkolu budeme pracovat s binárními stromy, kterým budeme říkat
# „levé minimové stromy“. Levé minimové stromy mají následující vlastnosti:
#
# * všechny listy levého minimového stromu jsou ve stejné hloubce;
# * levý minimový strom je zarovnaný doleva, což znamená, že:
#    a) pokud má některý uzel jen jednoho potomka, pak je to levý potomek;
#    b) pokud má některý uzel oba potomky, pak ten levý je kořenem perfektního
#       stromu (tj. úplného stromu se zaplněným posledním patrem);
# * klíče vnitřních uzlů jsou minima jejich podstromů
#   (skutečné hodnoty jsou tedy uloženy pouze v listech).
#
# Příklady levých minimových stromů:
#
#           1
#         /   \
#        2     1
#       / \   /
#      2   3 1
#
#         1
#      /     \
#     1       3
#    / \     /
#   2   1   3
#   ∧   ∧   ∧
#  2 3 1 4 3 5
#
# Příklady binárních stromů, které nejsou levými minimovými stromy:
#
#           1
#         /   \
#        2     1
#       / \
#      2   3
#  (porušuje první podmínku)
#
#           1
#         /   \
#        2     1
#       / \     \
#      2   3     1
#  (porušuje odrážku a) z druhé podmínky)
#
#           1
#         /   \
#        2     1
#       /     /
#      2     1
#  (porušuje odrážku b) z druhé podmínky)
#
#           1
#         /   \
#        2     0
#       / \   /
#      2   3 1
#  (porušuje třetí podmínku)
#
# Do následujících definic tříd nijak nezasahujte.
# Pro vykreslování stromů máte na konci tohoto souboru k dispozici
# funkci draw_tree.


class Node:
    """Třída Node reprezentuje uzel binárního stromu.

    Atributy:
        key     klíč uzlu
        left    odkaz na levý potomek uzlu nebo ‹None›
        right   odkaz na pravý potomek uzlu nebo ‹None›
    """
    __slots__ = "key", "left", "right"

    def __init__(self, key: int,
                 left: 'Node | None' = None,
                 right: 'Node | None' = None):
        self.key = key
        self.left = left
        self.right = right


class BinTree:
    """Třída BinTree reprezentuje binární strom.

    Atributy:
        root    odkaz na kořenový uzel stromu nebo ‹None›
    """
    __slots__ = "root"

    def __init__(self, root: Node | None = None):
        self.root = root


# Část 1.
# Implementujte funkci build_min_tree, která vybuduje levý minimový strom
# se zadanými hodnotami v listech. Strom musí být co nejnižší.

def build_min_tree(leaves: list[int]) -> BinTree:
    """
    vstup: ‹leaves› – pole celých čísel
    výstup: korektní levý minimový strom, který má co nejmenší výšku
            a v listech obsahuje hodnoty z pole ‹leaves› ve stejném pořadí
            zleva doprava; funkce nijak nemodifikuje zadaný vstup
    časová složitost: O(n), kde n je délka pole ‹leaves›

    Příklad: Pro vstupy [2, 3, 1] a [2, 3, 1, 4, 3, 5] mají odpovídajícími
    výstupy být stromy uvedené výše.
    """

    if leaves == []:
        return BinTree(None)

    nodes: list[Node] = []

    for leaf in leaves:
        nodes.append(Node(leaf))

    while len(nodes) > 1:
        new_nodes: list[Node] = []

        i = 0
        while i < len(nodes):
            if i + 1 < len(nodes):
                parent: Node = Node(min(nodes[i].key, nodes[i + 1].key))
                parent.left = nodes[i]
                parent.right = nodes[i + 1]
                new_nodes.append(parent)
                i += 2
            else:
                parent: Node = Node(nodes[i].key)
                parent.left = nodes[i]
                parent.right = None
                new_nodes.append(parent)
                i += 1

        nodes = new_nodes.copy()

    return BinTree(nodes[0])

# Část 2.
# Implementujte následující tři predikáty, které reprezentují výše uvedené tři
# podmínky levého minimového stromu. Každý predikát má jako vstupní podmínku
# platnost předchozích predikátů. Predikáty nemodifikují vstupní stromy.


def is_leaf(node: Node):
    return node.left is None and node.right is None


def check_leaf_depth_rec(node: Node | None, depth: int) -> int:
    if node is None:
        return -1

    if is_leaf(node):
        return depth

    left = check_leaf_depth_rec(node.left, depth + 1) if node.left else None
    right = check_leaf_depth_rec(node.right, depth + 1) if node.right else None

    if left == -1 or right == -1:
        return -1

    if left is None:
        return right
    if right is None:
        return left

    if left != right:
        return -1
    return left


def check_leaf_depth(tree: BinTree) -> bool:
    """
    vstup: ‹tree› – binární strom
    výstup: ‹True›, pokud mají všechny listy stromu stejnou hloubku;
            ‹False› jinak
    časová složitost: O(n), kde ‹n› je počet uzlů stromu
    extra prostorová složitost: O(h), kde ‹h› je výška stromu
        (Do extra prostorové složitost nepočítáme velikost vstupu, ale
         počítáme do ní zásobník rekurze.)
    """
    if tree.root is None:
        return True

    return check_leaf_depth_rec(tree.root, 0) != -1


def is_full(node: Node | None) -> bool:
    if node is None:
        return True
    if (node.left is None) != (node.right is None):
        return False
    return is_full(node.left) and is_full(node.right)


def check_left_align_rec(node: Node | None) -> tuple[bool, bool, int]:
    if node is None:
        return True, True, -1

    l_valid, l_perfect, l_height = check_left_align_rec(node.left)
    r_valid, r_perfect, r_height = check_left_align_rec(node.right)

    if node.right is not None and node.left is None:
        return False, False, 0

    if node.left is not None and node.right is not None:
        if not l_perfect:
            return False, False, 0

    is_valid = l_valid and r_valid

    is_perfect = (
        l_perfect and r_perfect and l_height == r_height
    )

    height = max(l_height, r_height) + 1

    return is_valid, is_perfect, height


def check_left_align(tree: BinTree) -> bool:
    """
    vstup: ‹tree› – binární strom, jehož všechny listy mají stejnou hloubku
                    (tj. předpokládáme, že platí ‹check_leaf_depth(tree)›)
    výstup: ‹True›, pokud je strom zarovnaný doleva (dle popisu nahoře);
            ‹False› jinak
    časová složitost: O(n), kde ‹n› je počet uzlů stromu
    extra prostorová složitost: O(h), kde ‹h› je výška stromu
        (Do extra prostorové složitost nepočítáme velikost vstupu, ale
         počítáme do ní zásobník rekurze.)
    """
    valid, _, _ = check_left_align_rec(tree.root)
    return valid


def check_min_rec(node: Node | None) -> bool:
    if node is None:
        return True

    if node.left is None and node.right is None:
        return True

    if node.left is not None:
        if node.right is not None:
            return (
                node.key == min(node.left.key, node.right.key)
                and check_min_rec(node.left)
                and check_min_rec(node.right)
            )
        return node.key == node.left.key and check_min_rec(node.left)


def check_min(tree: BinTree) -> bool:
    """
    vstup: ‹tree› – binární strom, jehož všechny listy mají stejnou hloubku
                    a který je doleva zarovnaný dle podmínek nahoře
                    (tj. předpokládáme, že platí ‹check_leaf_depth(tree)›
                     i ‹check_left_align(tree)›)
    výstup: ‹True›, pokud je klíčem každého vnitřního uzlu minimum
                    jeho podstromu;
            ‹False› jinak
    časová složitost: O(n), kde ‹n› je počet uzlů stromu
    extra prostorová složitost: O(h), kde ‹h› je výška stromu
        (Do extra prostorové složitost nepočítáme velikost vstupu, ale
         počítáme do ní zásobník rekurze.)
    """
    return check_min_rec(tree.root)


# Následující funkci můžete použít pro vykreslení stromu při vlastním
# testování. Použití: draw_tree(strom, název souboru).
# Výstupem je soubor ve formátu GraphViz.

def draw_tree(tree: BinTree, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write("digraph BinTree {\n"
                   "node [color=lightblue2, style=filled]\n")
        if tree.root is not None:
            draw_node(tree.root, file)
        file.write("}\n")


def draw_node(node: Node, file: TextIO) -> None:
    file.write(f'"{id(node)}" [label="{node.key}"]\n')
    for child, side in (node.left, 'L'), (node.right, 'R'):
        if child is None:
            nil = f"{side}{id(node)}"
            file.write(f'"{nil}" [label="", color=white]\n'
                       f'"{id(node)}" -> "{nil}"\n')
        else:
            file.write(f'"{id(node)}" -> "{id(child)}"\n')
            draw_node(child, file)
