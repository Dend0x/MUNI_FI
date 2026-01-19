from ib111 import week_03  # noqa


# Napište čistou funkci ‹least_squares›, která dostane na vstupu dva
# stejně dlouhé seznamy čísel. Hodnoty na odpovídajících pozicích
# v těchto seznamech udávají souřadnice jednoho vstupního bodu.
#
# Výsledkem funkce nechť je trojice ⟦(α, β, r)⟧ kde ⟦y = α + βx⟧
# udává přímku, která nejlépe aproximuje zadané body, a ⟦r⟧ je seznam
# tzv. residuí (vertikálních vzdáleností jednotlivých bodů od
# vypočtené přímky). Označíme-li souřadnice jednotlivých bodů ⟦(xᵢ,
# yᵢ)⟧ a ⟦x̄⟧, ⟦ȳ⟧ aritmetické průměry příslušných seznamů,
# hledané koeficienty získáte použitím těchto vzorců:

#  ⟦ βₛ = ∑ ( xᵢ - x̄ )( yᵢ - ȳ )
#    βₓ = ∑ ( xᵢ - x̄ )²
#    β  = βₛ / βₓ
#    α  = ȳ - βx̄ ⟧

# V případě, že body leží na vertikální přímce (a tedy ⟦β⟧ není
# definovaná), vraťte místo trojice hodnotu ‹None›.

def least_squares(x: list[float], y: list[float]) -> tuple[float, float, list[float]] | None:
    mean_x: float = 0
    mean_y: float = 0
    beta_s: float = 0
    beta_x: float = 0
    r = []

    for one_x in x:
        mean_x += one_x
    mean_x /= float(len(x))

    for one_y in y:
        mean_y += one_y
    mean_y /= float(len(y))

    for i in range(len(x)):
        beta_s += (x[i] - mean_x) * (y[i] - mean_y)
        beta_x += (x[i] - mean_x) ** 2
    if beta_x == 0:
        return None
    beta = beta_s / beta_x
    alfa = mean_y - beta * mean_x

    for index, one_x in enumerate(x):
        r.append(abs(y[index] - (beta*one_x + alfa)))
    return (alfa, beta, r)


def main():
    assert check([1, 2], [3, 4], (2, 1, [0, 0]))
    assert check([1, 2, 3], [3, 4, 5], (2, 1, [0, 0, 0]))
    assert least_squares([1, 1, 1], [3, 4, 5]) is None
    assert check([1, 2, 3], [2, 2, 2], (2, 0, [0, 0, 0]))
    assert check([1, 2, 3], [1, 4, 1], (2, 0, [1, 2, 1]))
    assert check([1, 2, 3], [1, 2, 4],
                 (-2.0 / 3.0, 3.0 / 2.0, [1.0 / 6.0, 1.0 / 3.0, 1.0 / 6.0]))


def check(x, y, expect):
    from math import isclose
    (alpha1, beta1, r1) = least_squares(x, y)
    (alpha2, beta2, r2) = expect
    if not isclose(alpha1, alpha2) or not isclose(beta1, beta2):
        return False
    for i in range(len(r1)):
        if not isclose(r1[i], r2[i]):
            return False
    return True


if __name__ == "__main__":
    main()
