from ib111 import week_11  # noqa


# Napište čistou funkci, která vrátí množinu všech slov, tvořených
# znaky ‹{"0", "1", "2"}› s danou délkou ‹length› a váhou ‹weight›.
# Váhou myslíme počet nenulových číslic v daném slově.


def weighted_words_rec(length: int, weight: int, index: int, non_zeros_used: int, result: set[str], current: str) -> None:
    if index == length:
        if weight == non_zeros_used:
            result.add(current)
        return

    weighted_words_rec(length, weight, index + 1, non_zeros_used, result, current + '0')
    weighted_words_rec(length, weight, index + 1, non_zeros_used + 1, result, current + '1')
    weighted_words_rec(length, weight, index + 1, non_zeros_used + 1, result, current + '2')

def weighted_words(length: int, weight: int) -> set[str]:
    result: set[str] = set()
    weighted_words_rec(length, weight, 0, 0, result, "")
    return result


def main() -> None:
    assert weighted_words(1, 2) == set()
    assert weighted_words(0, 0) == {""}
    assert weighted_words(2, 2) == {"11", "12", "21", "22"}
    assert weighted_words(3, 1) == {"001", "002", "010", "020", "100", "200"}


if __name__ == '__main__':
    main()
