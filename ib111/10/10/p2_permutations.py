from ib111 import week_10  # noqa


# Napište čistou funkci, která ze vstupního seznamu vytvoří seznam
# všech jeho permutací (tedy seznamů takových, že jsou tvořena
# stejnými hodnotami v libovolném pořadí). Výsledný seznam permutací
# nechť je uspořádán lexikograficky.

# Nápověda: řešení se znatelně zjednoduší, budete-li celou dobu
# pracovat se seřazenou verzí vstupního seznamu (seřazení je nakonec
# také jen permutace). Dobré řešení pak vytvoří každou permutaci
# pouze jednou a také je vytvoří rovnou ve správném pořadí.


def permutations_rec(word: list[int], count: int, seen: set[int],
                     current: list[int], result: list[list[int]]) -> None:
    if count == len(word):
        result.append(current.copy())
        return

    last: int | None = None

    for j, part in enumerate(word):
        if j in seen:
            continue

        value = part

        if value == last:
            continue

        seen.add(j)
        current.append(value)

        permutations_rec(word, count + 1, seen, current, result)

        current.pop()
        seen.remove(j)
        last = value


def permutations(word: list[int]) -> list[list[int]]:
    sorted_word = sorted(word)
    result: list[list[int]] = []
    permutations_rec(sorted_word, 0, set(), [], result)
    return result


def main() -> None:
    assert permutations([]) == [[]]
    assert permutations([1, 1]) == [[1, 1]]
    assert permutations([1, 2]) == [[1, 2], [2, 1]]
    assert permutations([3, 1, 2]) == [[1, 2, 3],
                                       [1, 3, 2],
                                       [2, 1, 3],
                                       [2, 3, 1],
                                       [3, 1, 2],
                                       [3, 2, 1]]


if __name__ == '__main__':
    main()
