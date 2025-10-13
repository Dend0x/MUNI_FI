from ib111 import week_04  # noqa


# Do programu (který si možná pamatujete z druhého týdne) doplňte
# typové anotace tak, aby prošel kontrolou nástrojem ‹mypy› bez
# chyb.

Vector = tuple[float, float]

# Pomocné funkce.

def find_slope(points: list[Vector], avg_x: float, avg_y: float) -> float | None:
    dividend: float = 0.0
    divisor: float = 0

    for i, (x, y) in enumerate(points):
        dividend += ((x - avg_x) * (y - avg_y))
        divisor += (x - avg_x) ** 2

    if divisor == 0:
        return None

    return dividend / divisor


def find_intercept(avg_x: float, avg_y: float, beta: float) -> float:
    return avg_y - beta * avg_x


# První verze má jako vstup dva vektory (seznamy), jeden se
# souřadnicemi ⟦x⟧ a druhý se souřadnicemi ⟦y⟧. Výsledkem nechť je
# dvojice ⟦(α, β)⟧.

def regress_vectors(x: list[float], y: list[float]) -> tuple[float, float] | None:
    return regress_points([(x[i], y[i]) for i in range(len(x))])


# Druhá verze má jako parametr seznam dvojic, kde každá dvojice
# popisuje jeden bod.

def regress_points(points: list[Vector]) -> tuple[float, float] | None:
    avg_x = sum([x for x, _ in points]) / len(points)
    avg_y = sum([y for _, y in points]) / len(points)

    slope: float | None = find_slope(points, avg_x, avg_y)

    if slope is None:
        return None

    intercept: float = find_intercept(avg_x, avg_y, slope)
    return (intercept, slope)


# Výpočet residuí z dvojice seznamů.

def residuals_vectors(x: list[float], y: list[float], alpha: float, beta: float) -> list[float]:
    points: list[Vector] = [(x[i], y[i]) for i in range(len(x))]
    return residuals_points(points, alpha, beta)


# Výpočet residuí ze seznamu dvojic.

def residuals_points(points: list[Vector], alpha: float, beta: float) -> list[float]:
    res: list[float] = []
    for i, (x, y) in enumerate(points):
        res.append(abs(y - beta * x - alpha))
    return res


def main() -> None:
    from math import isclose

    points = [(1.0, 3.0), (2.0, 4.0)]
    points_x = [1.0, 2.0]
    points_y = [3.0, 4.0]
    expect_alpha = 2.0
    expect_beta = 1.0
    expect_ra = 0.0
    expect_rb = 0.0

    result = regress_vectors(points_x, points_y)
    assert result is not None
    alpha, beta = result
    assert isclose(expect_alpha, alpha)
    assert isclose(expect_beta, beta)

    result = regress_points(points)
    assert result is not None
    alpha, beta = result
    assert isclose(expect_alpha, alpha)
    assert isclose(expect_beta, beta)

    ra, rb = residuals_vectors(points_x, points_y, alpha, beta)
    assert isclose(ra, expect_ra)
    assert isclose(rb, expect_rb)

    ra, rb = residuals_points(points, alpha, beta)
    assert isclose(ra, expect_ra)
    assert isclose(rb, expect_rb)


if __name__ == "__main__":
    main()  # mypy-only exercise, this should already pass
