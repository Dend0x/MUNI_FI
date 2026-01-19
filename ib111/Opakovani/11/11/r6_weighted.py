from ib111 import week_11  # noqa


# Napište čistou funkci, která vrátí množinu všech slov, tvořených
# znaky ‹{"0", "1", "2"}› s danou délkou ‹length› a váhou ‹weight›.
# Váhou myslíme počet nenulových číslic v daném slově.


def weighted_rec(length: int, weight: int, cur_length: int, cur_weight, result: set[str], current: str):
    if cur_weight > weight or cur_length > length:
        return

    if length == cur_length and weight == cur_weight:
        result.add(current)
        return

    if cur_weight < weight:
        weighted_rec(length, weight, cur_length + 1, cur_weight + 1, result, current + "1")
        weighted_rec(length, weight, cur_length + 1, cur_weight + 1, result, current + "2")
    weighted_rec(length, weight, cur_length + 1, cur_weight, result, current + "0")


def weighted_words(length: int, weight: int) -> set[str]:
    result: set[str] = set()
    weighted_rec(length, weight, 0, 0, result, "")
    return result


def main() -> None:
    assert weighted_words(1, 2) == set()
    assert weighted_words(0, 0) == {""}
    assert weighted_words(2, 2) == {"11", "12", "21", "22"}
    assert weighted_words(3, 1) == {"001", "002", "010", "020", "100", "200"}


if __name__ == '__main__':
    main()
