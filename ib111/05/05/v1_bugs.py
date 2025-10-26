from ib111 import week_05  # noqa


# Budeme zkoumat řadu vedle sebe sedících světlušek. Každá světluška
# má energii, která se vyjadřuje nezáporným celým číslem. Bude nás zajímat
# vývoj této energie v čase, přičemž v každém kroku dojde k následujícímu:
#
# • Energie všech světlušek se zvětší o 1.
# • Světlušky, které mají energii větší než 3, se rozsvítí. To způsobí,
#   že se energie jejich sousedních světlušek zvýší o další 1.
#   To může způsobit jejich rozsvícení (pokud dosud nebyly rozsvícené) atd.
# • Energie všech světlušek, které se v tomto kroku rozsvítily, se sníží
#   na 0. Všechny rozsvícené světlušky zhasnou.
#
# Máme-li tedy na začátku světlušky ve stavu ‹[0, 2, 0, 2, 0]›,
# v následujícím kroku budou ve stavu ‹[1, 3, 1, 3, 1]› a dále pak
# ‹[3, 0, 0, 0, 3]›.

# Čistá funkce ‹light_bugs› vrátí seznam seznamů reprezentujících
# prvních ‹time› kroků pozorování světlušek, jejichž počáteční
# energie je daná parametrem ‹start›.  Předpokládejte, že se ‹start›
# skládá jen z čísel od 0 do 3 včetně, má délku alespoň dvě a že
# ‹time› je kladné celé číslo.

def is_light(start, i, was_ligthed):
    if start[i] > 3 and i not in was_ligthed:
        was_ligthed.add(i)
        start[i] = 0
        if i - 1 >= 0:
            if i - 1 not in was_ligthed:
                start[i - 1] += 1
                is_light(start, i - 1, was_ligthed)
        if i + 1 < len(start):
            if i + 1 not in was_ligthed:
                start[i + 1] += 1
                is_light(start, i + 1, was_ligthed)

def light_bugs(start, time):
    result = [start.copy()]

    for j in range(time - 1):
        was_lighted = set()
        aux = result[j].copy()
        i = 0
        while i < len(aux):
            if i not in was_lighted:
                aux[i] += 1
            is_light(aux, i, was_lighted)
            i += 1
        result.append(aux)

    return result


# Příklad: pro vstup ‹([0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0], 7)›
# funkce vrátí následující seznam:

example = [[0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 2, 0, 2, 1, 1, 1, 1],
           [2, 2, 2, 2, 3, 1, 3, 2, 2, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]


def main() -> None:
    bugs = [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
    assert light_bugs(bugs, 7) == example
    assert bugs == [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]

    assert light_bugs([0, 1], 8) \
        == [[0, 1], [1, 2], [2, 3], [0, 0], [1, 1], [2, 2], [3, 3], [0, 0]]

    assert light_bugs([1, 0, 1], 4) \
        == [[1, 0, 1], [2, 1, 2], [3, 2, 3], [0, 0, 0]]

    assert light_bugs([1, 2, 3], 5) \
        == [[1, 2, 3], [3, 0, 0], [0, 2, 1], [1, 3, 2], [3, 0, 0]]

    assert light_bugs([0, 1, 2, 3, 2, 1, 0, 1, 2, 3], 2) \
        == [[0, 1, 2, 3, 2, 1, 0, 1, 2, 3], [1, 3, 0, 0, 0, 3, 1, 3, 0, 0]]

    assert light_bugs([3, 3, 3, 0, 0, 0, 3, 3, 3], 1) \
        == [[3, 3, 3, 0, 0, 0, 3, 3, 3]]

    bugs = [0, 1, 2, 3]
    assert light_bugs(bugs, 100) \
        == [[0, 1, 2, 3], [1, 3, 0, 0], [3, 0, 2, 1], [0, 2, 3, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2],
            [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0],
            [3, 1, 1, 1], [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1],
            [0, 3, 2, 2], [2, 0, 0, 0], [3, 1, 1, 1], [0, 3, 2, 2]]
    assert bugs == [0, 1, 2, 3]


if __name__ == '__main__':
    main()
