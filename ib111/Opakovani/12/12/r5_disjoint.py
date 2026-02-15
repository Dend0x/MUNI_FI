from ib111 import week_12  # noqa


# Napište čistou funkci ‹nearest_disjoint›, která pro vstup ⟦n⟧ nalezne
# číslo ⟦m⟧ takové, že:
#
#  • množiny cifer použitých v ⟦m⟧ a ⟦n⟧ jsou disjunktní,
#  • ⟦|m - n|⟧ je nejmenší možné.

def to_digits(n: int) -> list[int]:
    if n == 0:
        return [0]
    out = []
    while n > 0:
        out.append(n % 10)
        n //= 10
    return out


def from_digits(digits: list[int]) -> int | None:
    if not digits:
        return None
    out = 0
    for d in digits:
        out *= 10
        out += d
    return out


def nearest_disjoint(n: int) -> int | None:
    digits = to_digits(n)
    available = set(range(10)) - set(digits)
    tail_len = len(digits) - 1

    if not available:
        return None

    first = digits[-1]
    big_digit = max(available)
    small_digit = min(available)
    small_nonzero = 0 if available == {0} else min(available - {0})

    first_small = [x for x in available if x < first]
    first_big = [x for x in available if x > first]

    lead_small = [max(first_small)] if first_small else []
    lead_big = [min(first_big)] if first_big else [small_nonzero, small_digit]

    tail_big = [big_digit for i in range(tail_len)]
    tail_small = [small_digit for i in range(tail_len)]
    smaller = from_digits(lead_small + tail_big)
    bigger = from_digits(lead_big + tail_small)

    if smaller is not None and bigger is not None and n - smaller < bigger - n:
        return smaller
    return bigger


def main() -> None:
    assert nearest_disjoint(0) == 1
    assert nearest_disjoint(1) == 0 or nearest_disjoint(1) == 2
    assert nearest_disjoint(9) == 10 or nearest_disjoint(9) == 8
    assert nearest_disjoint(10) == 9
    assert nearest_disjoint(22) == 19
    assert nearest_disjoint(1234) == 999
    assert nearest_disjoint(1259) == 888
    assert nearest_disjoint(9988) == 10000
    assert nearest_disjoint(500) == 499
    assert nearest_disjoint(87451) == 90000
    assert nearest_disjoint(5555) == 6000
    assert nearest_disjoint(123456789) == 0
    assert nearest_disjoint(1023456789) is None


if __name__ == '__main__':
    main()
