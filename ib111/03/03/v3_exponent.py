from ib111 import week_03  # noqa


# Čistá funkce ‹largest_exponent› dostane na vstup neprázdný seznam
# kladných čísel ‹numbers› a prvočíslo ‹prime› a vrátí to ze
# zadaných čísel, které má v prvočíselném rozkladu největší mocninu
# zadaného prvočísla (pokud se tam zadané prvočíslo nevyskytuje, má
# mocninu 0). Pokud je v seznamu více čísel se stejnou mocninou
# zadaného prvočísla v rozkladu, vrátí to nejmenší z nich.

def largest_exponent(numbers, prime):
    isStillDivisible = [True for i in range(len(numbers))]
    numberscop = numbers.copy()

    while sum(isStillDivisible) > 0:
        copyDiv = isStillDivisible.copy()
        for index in range(len(numbers)):
            if isStillDivisible[index]:
                if numbers[index] % prime == 0:
                    numbers[index] //= prime
                else:
                    isStillDivisible[index] = False
        if sum(isStillDivisible) == 0:
            isStillDivisible = copyDiv
            break
    
    result = []

    for index, num in enumerate(isStillDivisible):
        if num:
            result.append(numberscop[index])

    return min(result)


# Příklad: Volání ‹largest_exponent([24, 36, 54], 2)› vrátí ‹24›.
# Volání ‹largest_exponent([625, 1375, 1250], 5)› vrátí ‹625›.

def main() -> None:
    assert largest_exponent([24, 36, 54], 2) == 24
    assert largest_exponent([625, 1375, 1250], 5) == 625
    assert largest_exponent([2 ** 20, 2 ** 17, 2 ** 17 * 9], 2) == 2 ** 20
    assert largest_exponent([1029, 1225, 1715, 1323, 686], 7) == 686


if __name__ == '__main__':
    main()
