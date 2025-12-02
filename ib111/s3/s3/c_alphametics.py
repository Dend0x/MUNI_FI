from ib111 import week_10  # noqa


# «Slovní aritmetika¹» (někdy též cryptarithm nebo algebrogram) je matematický
# hlavolam zadaný jako rovnice se slovy, např. „SEND + MORE = MONEY“.
# Cílem je přiřadit každému písmenu unikátní² číslici tak, aby po jejich
# nahrazení rovnost platila. Přitom zápis žádného z čísel nesmí začínat nulou.
# V tomto konkrétním případě (a v desítkové soustavě) je jediné možné
# řešení, a to S → 9, E → 5, N → 6, D → 7, M → 1, O → 0, R → 8, Y → 2.
# Po tomto nahrazení číslicemi skutečně platí ⟦9567 + 1085 = 10652⟧.
#
# ¹ ‹https://en.wikipedia.org/wiki/Verbal_arithmetic›
# ² „Unikátní“ znamená, že dvě různá písmena nemohou mít přiřazenu stejnou
#   číslici.
#
# Cílem této úlohy je napsat čistou funkci, která podobné hlavolamy řeší,
# a to v zadané poziční soustavě (základem bude vždy celé číslo mezi 2 a 26
# včetně). Omezíme se přitom pouze na sčítání, jiné aritmetické operace
# neuvažujeme. Rovnice na vstupu je zadána dvěma parametry. Levá strana rovnice
# ‹lhs› je seznam (alespoň dvou) slov, přičemž každé slovo je dáno jako seznam
# písmen (jednoznakových řetězců). Pravá strana rovnice je pak je vždy právě
# jedno slovo (seznam písmen).
#
# Funkce vrátí slovník, který každému písmenu hlavolamu přiřazuje unikátní
# hodnotu číslice. Pokud existuje více řešení, funkce vrátí libovolné
# z nich. Pokud neexistuje žádné řešení, funkce vrátí ‹None›.
#
# Nápověda: Použijte techniku backtrackingu. Vzpomeňte si na svá
# základoškolská léta – zejména na sčítání pod sebou, které začíná vždy
# zprava. I zde se k řešení hodí postupně zkoušet přiřazovat hodnoty
# číslicím, které jsou u jednotlivých sčítanců co nejvíce vpravo, a rekurzi
# včas ukončit, když už je jasné, že výsledku není možno dosáhnout.


def solve_rec(lhs: list[list[str]], rhs: list[str], base: int,
              result: dict[str, int], current_index: int,
              overflow: int, used: set[int],
              firsts: set[str], handled: set[int] | None) -> bool:
    if handled is None:
        handled = set()
    else:
        handled = set(handled)

    current_vars: list[str] = []
    for word in lhs:
        if current_index >= len(word):
            continue
        current_vars.append(word[len(word) - current_index - 1])

    if len(current_vars) == 0 and current_index >= len(rhs) and overflow == 0:
        all_letters = set()
        for word in lhs:
            for letter in word:
                all_letters.add(letter)
        for letter in rhs:
            all_letters.add(letter)

        return all_letters <= set(result.keys())

    sum_vars = overflow

    for idx, var in enumerate(current_vars):
        if idx in handled:
            continue

        if var in result:
            sum_vars += result[var]
            handled.add(idx)
            continue

        for i in range(base):
            if i == 0 and var in firsts:
                continue
            if i not in used:
                used.add(i)
                sum_vars += i
                result[var] = i
                handled.add(idx)
                if solve_rec(lhs, rhs, base, result,
                             current_index, sum_vars, used, firsts, handled):
                    return True
                handled.remove(idx)
                used.remove(i)
                result.pop(var)
                sum_vars -= i

    if current_index >= len(rhs):
        return False

    result_letter = rhs[len(rhs) - current_index - 1]

    if result_letter in result:
        if sum_vars % base != result[result_letter]:
            return False
        else:
            return solve_rec(lhs, rhs, base, result,
                             current_index + 1, sum_vars // base,
                             used, firsts, None)

    for j in range(base):
        if j in used or (j == 0 and result_letter in firsts):
            continue
        if sum_vars % base == j:
            result[result_letter] = j
            used.add(j)
            if solve_rec(lhs, rhs, base, result,
                         current_index + 1, sum_vars // base,
                         used, firsts, None):
                return True
            used.remove(j)
            result.pop(result_letter)

    return False


def solve(lhs: list[list[str]], rhs: list[str], base: int) \
        -> dict[str, int] | None:
    result: dict[str, int] = {}
    firsts: set[str] = {rhs[0]}

    for word in lhs:
        firsts.add(word[0])

    found = solve_rec(lhs, rhs, base, result, 0, 0, set(), firsts, None)
    return result if found else None


def main() -> None:
    # SEND + MORE = MONEY
    assert solve([['S', 'E', 'N', 'D'],
                  ['M', 'O', 'R', 'E']],
                 ['M', 'O', 'N', 'E', 'Y'], 10) \
        == {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

    for base in range(2, 27):
        # XY + XY = YX
        result = solve([['X', 'Y'], ['X', 'Y']], ['Y', 'X'], base)
        if base == 2 or base % 3 != 2:
            assert result is None
        else:
            x = base // 3
            y = 2 * x + 1
            assert result == {'X': x, 'Y': y}


if __name__ == '__main__':
    main()
