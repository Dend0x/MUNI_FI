from ib111 import week_03  # noqa


# Napište (čistou) funkci, která jako parametr dostane seznam
# obdélníků a vrátí seznam obdélníků, které se překrývají s nějakým
# jiným. Obdélník samotný je reprezentovaný dvěma body (levým dolním
# a pravým horním rohem, a má nenulovou výšku i šířku). Obdélníky
# budeme zapisovat jako dvojice dvojic – ‹((0, 0), (1, 2))›
# například reprezentuje tento obdélník:
#
#           ┌───┐(1, 2)
#           │   │
#           │   │
#     (0, 0)└───┘
#
# Mohl by se Vám hodit predikát, který je pravdivý, když se dva
# obdélníky překrývají:

def has_overlap(a, b):
    fa, sa = a
    fb, sb = b
    xfa, yfa = fa
    xsa, ysa = sa
    xfb, yfb = fb
    xsb, ysb = sb

    return ((xsa > xfb) and (ysa > yfb)) or ((xfa < xsb) and (ysb  < yfa))


def is_in(a, list):
    for elem in list:
        if elem == a:
            return True

    return False


def filter_overlapping(rectangles: list[tuple[tuple[int, int]]]) -> list[tuple[tuple[int, int]]]:
    result = []

    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if has_overlap(rectangles[i], rectangles[j]):
                if rectangles[i] == rectangles[j]:
                    result.append(rectangles[i])
                    result.append(rectangles[j])
                    continue
                if not is_in(rectangles[i], result):
                    result.append(rectangles[i])
                if not is_in(rectangles[j], result):
                    result.append(rectangles[j])
    return result


def main():
    r1 = ((1, 1), (2, 2))
    r2 = ((0, 0), (2, 2))
    r3 = ((-2, -2), (-1, -1))
    r4 = ((10, 15), (25, 35))

    assert filter_overlapping([]) == []
    assert filter_overlapping([r1]) == []
    assert filter_overlapping([r1, r1]) == [r1, r1]
    assert filter_overlapping([r1, r2]) == [r1, r2]
    assert filter_overlapping([r2, r1]) == [r2, r1]

    assert filter_overlapping([r3, r2, r1, r4]) == [r2, r1]
    assert filter_overlapping([r2, ((1, 10), (10, 20))]) == []
    assert filter_overlapping([((15, 0), (17, 8)),
                               ((1, 10), (10, 20))]) == []
    l2 = [((0, 0), (2, 2)),
          ((1, 1), (10, 10)),
          ((9, 9), (11, 11))]
    assert filter_overlapping(l2) == l2


if __name__ == "__main__":
    main()
