#!/usr/bin/env python3

# Povolené knihovny: typing, math

# IB002 Domácí úloha 4
#
# Trojková (ternární) soustava je poziční číselná soustava o základu 3,
# která používá číslice 0, 1, 2. Tedy např. číslo 42 ve trojkové soustavě
# zapíšeme jako (1120)₃.
#
# Vaším úkolem bude implementovat funkci, která pro zadané parametry
# ‹length› a ‹total› vrátí vzestupně seřazený Pythonovský seznam všech
# kladných celých čísel, která mají ve trojkové soustavě právě ‹length›
# číslic a jejichž součet trojkových číslic je právě ‹total›. Přitom
# uvažujeme pouze zápis čísla bez zbytečných levostranných nul, tedy
# např. číslo 42 má ve trojkové soustavě právě čtyři číslice, ne více.
#
# Příklady:
# Pro vstup ‹length = 3› a ‹total = 5› bude výstupem seznam:
#   [17, 23, 25]
# ve trojkové soustavě bychom totiž tato čísla zapsali jako:
#   (122)₃, (212)₃, (221)₃
#
# Pro vstup ‹length = 4› a ‹total = 2› bude výstupem seznam:
#   [28, 30, 36, 54]
# ve trojkové soustavě bychom totiž tato čísla zapsali jako:
#   (1001)₃, (1010)₃, (1100)₃, (2000)₃
#
# Počty čísel splňujících zadanou podmínku se dají zapsat do takovéto
# tabulky:
#
#          │                    total
#   length │  1   2   3   4   5   6   7   8   9  10  11  ...
#   ───────┼────────────────────────────────────────────
#      1   │  1   1   0   0   0   0   0   0   0   0   0
#      2   │  1   2   2   1   0   0   0   0   0   0   0
#      3   │  1   3   5   5   3   1   0   0   0   0   0
#      4   │  1   4   9  13  13   9   4   1   0   0   0
#      5   │  1   5  14  26  35  35  26  14   5   1   0
#     ...
#
# Při podrobnějším zkoumání této tabulky si můžete všimnout jisté
# pravidelnosti; snadno pak dopočítáte další řádky. Hodnoty v tabulce
# jednak můžete využít pro částečnou kontrolu toho, že vaše řešení
# počítá správně, jednak budou hrát roli v časové složitosti řešení.
#
# Smyslem tohoto úkolu je procvičit si rekurzi. Vstupy v testech budou
# takové, aby rozumně použitá rekurze nenarazila na žádný limit.
#
# Kritickou částí tohoto úkolu je časová složitost řešení. Pro splnění
# požadavků je třeba si jednak dobře rozmyslet, ve kterých chvílích
# je vhodné rekurzi ukončit, jednak si dát pozor na to, co přesně
# děláte s Pythonovskými seznamy a jakou mají tyto operace složitost.
#
# Při analýze časové složitosti jako obvykle zanedbáváme přesnou složitost
# aritmetických operací s čísly, tj. považujeme ji za konstantní.
#
# Nezapomeňte, že si můžete definovat pomocné funkce. V tomto úkolu je
# to určitě velmi vhodné.


def ternary_sum_rec(length: int, cur_length: int, total: int, cur_total: int, number: int, result: list[int]):
    if cur_length == length:
        if cur_total == total:
            result.append(number)
        return

    if cur_total > total:
        return

    if cur_total + 2 * (length - cur_length) < total:
        return

    for i in range(min(3, total - cur_total + 1)):
        ternary_sum_rec(length, cur_length + 1, total, cur_total + i, number * 3 + i, result)
        


def ternary_sum(length: int, total: int) -> list[int]:
    """
    vstup: ‹length› – kladné celé číslo
           ‹total› – kladné celé číslo
    výstup: vzestupně seřazený seznam všech kladných celých čísel,
            která mají ve trojkové soustavě právě ‹length› číslic
            a součet jejichž trojkových číslic je právě ‹total›
    časová složitost: O(T(length, total) · length),
        kde T(length, total) je hodnota z tabulky naznačené výše
    """
    result: list[int] = []

    ternary_sum_rec(length, 1, total, 1, 1, result)
    ternary_sum_rec(length, 1, total, 2, 2, result)

    return result


def main() -> None:
    # příklady ze zadání
    assert ternary_sum(3, 5) == [17, 23, 25]
    assert ternary_sum(4, 2) == [28, 30, 36, 54]

    # jednoduché malé případy
    assert ternary_sum(1, 1) == [1]        # (1)₃
    assert ternary_sum(1, 2) == [2]        # (2)₃
    assert ternary_sum(1, 3) == []         # nemožné

    # length = 2
    assert ternary_sum(2, 1) == [3]        # (10)₃
    assert ternary_sum(2, 2) == [4, 6]     # (11)₃ (20)₃
    assert ternary_sum(2, 3) == [5, 7]     # (12)₃ (21)₃
    assert ternary_sum(2, 4) == [8]        # (22)₃

    # kontrola počtu výsledků podle tabulky
    assert len(ternary_sum(3, 1)) == 1
    assert len(ternary_sum(3, 2)) == 3
    assert len(ternary_sum(3, 3)) == 5
    assert len(ternary_sum(3, 4)) == 5
    assert len(ternary_sum(3, 5)) == 3
    assert len(ternary_sum(3, 6)) == 1

    print("All tests passed.")


if __name__ == "__main__":
    main()