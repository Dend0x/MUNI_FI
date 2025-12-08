from ib111 import week_11  # noqa


# Napište čistou funkci, která na základě daného vzoru vytvoří
# množinu všech odpovídajících řetězců. Vzor je tvořený
# alfanumerickými znaky a navíc může obsahovat hranaté závorky –
# znaky ‹[› a ‹]›. Mezi těmito závorkami může stát libovolný počet
# přípustných znaků (krom samotných hranatých závorek) a na daném
# místě se ve výsledném řetězci může nacházet libovolný z těchto
# znaků. Například vzor ‹a[bc]d› reprezentuje řetězce ‹abd› a ‹acd›.


def resolve_template_rec(template: str, index: int,
                         result: set[str], current: str) -> None:
    if index >= len(template):
        result.add(current)
        return

    if template[index] == '[':
        end = index + 1
        while template[end] != ']':
            end += 1
        help_i = index + 1
        while help_i < end:
            resolve_template_rec(template, end + 1, result,
                                 current + template[help_i])
            help_i += 1
        return
    resolve_template_rec(template, index + 1, result,
                         current + template[index])


def resolve_template(template: str) -> set[str]:
    result: set[str] = set()
    resolve_template_rec(template, 0, result, "")
    return result


def main() -> None:
    assert resolve_template("[]") == set()
    assert resolve_template("a") == {"a"}
    assert resolve_template("[abc]") == {"a", "b", "c"}
    assert resolve_template("a[bc]d") == {"abd", "acd"}
    assert resolve_template("[Hh]ello, [Ww]orld") \
        == {"Hello, World", "Hello, world", "hello, World", "hello, world"}
    assert resolve_template("[ab]x[cd]y[ef]") \
        == {"axcye", "axcyf", "axdye", "axdyf",
            "bxcye", "bxcyf", "bxdye", "bxdyf"}
    assert resolve_template("[abc]abc[ef]") \
        == {"aabce", "aabcf", "babce", "babcf", "cabce", "cabcf"}
    assert resolve_template("[ab][a][b][c][d]") \
        == {"aabcd", "babcd"}


if __name__ == '__main__':
    main()
