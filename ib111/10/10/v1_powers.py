from ib111 import week_10  # noqa
from math import isqrt


# Napište čistou funkci ‹sum_different_powers›, která pro zadané kladné celé
# číslo ‹num› a celé číslo ‹k› ≥ 2 rozhodne, zda se dá ‹num› napsat jako součet
# druhé, třetí, ... až ‹k›té mocniny «různých» kladných celých čísel.
#
# Funkce musí rozumně fungovat pro ‹num› v řádech milionů a pro ‹k› do 10.
#
# Příklad:
# Volání ‹{fun}(17, 3)› vrátí ‹True›, protože ⟦17 = 4^2 + 1^3⟧.
# Volání ‹{fun}(80, 3)› vrátí ‹False›, protože není žádný způsob, jak číslo
# 80 zapsat jako součet druhé a třetí mocniny různých kladných celých čísel.
# Volání ‹{fun}(365, 5)› vrátí ‹True›, protože ⟦365 = 10^2 + 2^3 + 4^4 + 1^5⟧.
# Volání ‹{fun}(1000, 4)› vrátí ‹True›, protože ⟦1000 = 24^2 + 7^3 + 3^4⟧.
# Volání ‹{fun}(1002, 4)› vrátí ‹False›, protože 1002 se nedá zapsat jako
# součet druhé, třetí a čtvrté mocniny různých kladných celých čísel.


def sum_different_powers_rec(num: int, k: int, current_sum: int, used: set[int]) -> bool:
    if current_sum == num and k == 1:
        return True

    if current_sum > num:
        return False

    if k < 2:
        return False

    for i in range(1, isqrt(num - current_sum) + 1):
        if i in used:
            continue
        used.add(i)
        if sum_different_powers_rec(num, k - 1, current_sum + i ** k, used):
            return True
        used.remove(i)

    return False


def sum_different_powers(num: int, k: int) -> bool:
    return sum_different_powers_rec(num, k, 0, set())


def main() -> None:
    assert sum_different_powers(17, 3)
    assert not sum_different_powers(80, 3)
    assert sum_different_powers(365, 5)
    assert sum_different_powers(1000, 4)
    assert not sum_different_powers(1002, 4)
    assert sum_different_powers(1, 2)
    assert not sum_different_powers(50, 2)


if __name__ == '__main__':
    main()
