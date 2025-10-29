from ib111 import week_06  # noqa


# Napište (čistou) funkci, která na vstupu dostane signál ‹data›
# reprezentovaný seznamem celočíselných amplitud (vzorků).
# Výsledkem bude statistika tohoto signálu, kterou vytvoří
# následujícím způsobem:

#  1. funkce signál nejdříve očistí od všech vzorků s amplitudou
#     větší než ‹max_amplitude› a menších než ‹min_amplitude›,
#  2. následně jej převzorkuje tak, že sloučí každých ‹bucket›
#     vzorků (poslední vzorek může být nekompletní) do jednoho
#     vypočtením jejich průměru a jeho následným zaokrouhlením
#     (pomocí vestavěné funkce ‹round›),
#  3. nakonec spočítá, kolikrát se v upraveném signálu objevují
#     jednotlivé amplitudy, a vrátí slovník, kde klíč bude amplituda
#     a hodnota bude počet jejích výskytů.

def histogram(data: list[int], max_amplitude: int,
              min_amplitude: int, bucket: int) -> dict[int, int]:
    done_data: list[int] = []
    i = 0

    while i < len(data):
        j = 0
        sum_data = 0
        while j < bucket:
            if i >= len(data):
                break
            if data[i] <= max_amplitude and data[i] >= min_amplitude:
                sum_data += data[i]
                j += 1
            i += 1
        if j != 0:
            done_data.append(round(sum_data / float(j)))

    hist: dict[int, int] = {}
    for item in done_data:
        if item in hist:
            hist[item] += 1
        else:
            hist[item] = 1
    return hist


def main() -> None:
    data = [1, 1, 1]
    assert histogram(data, 5, 0, 1) == {1: 3}
    assert data == [1, 1, 1]

    assert histogram([1, 1, 1, 1], 5, 0, 2) == {1: 2}
    assert histogram([1, 2, 3, 4, 5], 5, 2, 2) == {2: 1, 4: 1}
    assert histogram([1, 2, 9, 2, 10, 1, 1, 1, 1], 8, 1, 3) == {2: 1, 1: 2}

    data = []
    assert histogram([], 1, 2, 5) == {}
    assert data == []

    assert histogram([1, 1, 1, 8, 8, 8], 5, 3, 10) == {}
    assert histogram([1, 2, 3, 4], 2, 5, 3) == {}
    assert histogram([1, 2, 3, 4, 5], 10, 1, 7) == {3: 1}


if __name__ == '__main__':
    main()
