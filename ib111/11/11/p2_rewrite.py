from ib111 import week_11  # noqa


# Napište predikát, jehož hodnota bude ‹True› pokud lze požadované slovo
# ‹wanted› utvořit z iniciálního slova ‹initial› pomocí přepisovacích pravidel
# ‹rules› a ‹False› jinak. Slova vytváříme tak, že kterékoli písmeno z již
# vytvořených slov nacházející se mezi klíči slovníku pravidel ‹rules›
# můžeme nahradit za kterékoli písmeno z příslušné hodnoty. (Pro zjednodušení
# možnost zacyklení procesu vytváření slov nemusíte vůbec řešit.)

#Mypy and internet had to help with [str, ...]

def is_creatable_rec(wanted: list[str], initial: list[str], rules: dict[str, list[str]], seen: set[tuple[str, ...]]) -> bool:
    current = tuple(initial)
    if current in seen:
        return False
    seen.add(current)

    if initial == wanted:
        return True

    for index, ch in enumerate(initial):
        if ch in rules:
            for rule in rules[ch]:
                initial[index] = rule
                if is_creatable_rec(wanted, initial, rules, seen):
                    return True
                initial[index] = ch

    return False


def is_creatable(wanted: str, initial: str,
                 rules: dict[str, list[str]]) -> bool:
    wanted_word: list[str] = []
    initial_word: list[str] = []

    for ch in wanted:
        wanted_word.append(ch)

    for ch in initial:
        initial_word.append(ch)

    return is_creatable_rec(wanted_word, initial_word, rules, set())


def main() -> None:
    assert is_creatable("abc", "abc", {})
    assert not is_creatable("bc", "abc", {})
    assert is_creatable("abc", "abc", {"a": ["c", "d"]})
    assert not is_creatable("bbc", "abc", {"a": ["c", "d"]})
    assert is_creatable("aec", "abc",
                        {"a": ["e", "f"], "b": ["a", "f"]})
    assert is_creatable("fec", "abc",
                        {"a": ["e", "f"], "b": ["a", "f"]})
    assert is_creatable("bbb", "aaa", {"a": ["c"], "c": ["b"]})
    assert is_creatable("bcb", "aaa", {"a": ["c"], "c": ["b"]})
    assert is_creatable("ccc", "aaa", {"a": ["c"], "c": ["b"]})
    assert is_creatable("abcd", "aaaa",
                        {"a": ["b", "c", "d", "e"], "c": ["b"]})
    assert is_creatable("a", "a", {"a": ["b", "c"]})
    assert not is_creatable("aa", "bb",
                            {"b": ["c", "d", "e", "f"],
                             "c": ["d", "e", "f"],
                             "d": ["e", "f"],
                             "e": ["f"]})
    assert is_creatable("fd", "bc",
                        {"b": ["c", "d", "e"],
                         "c": ["d"],
                         "d": ["f"],
                         "e": ["f"]})
print(is_creatable('bcc', 'abb', {'a': ['b', 'c'], 'b': ['c', 'd'], 'c': ['d', 'e'], 'd': ['e', 'f']}))

if __name__ == '__main__':
    main()
