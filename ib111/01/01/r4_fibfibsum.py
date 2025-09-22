from ib111 import week_01  # noqa


# † Nechť ⟦A⟧ je Fibonacciho posloupnost s členy ⟦aₙ⟧ a ⟦B⟧ je
# posloupnost taková, že má na ⟦i⟧-té pozici ⟦aᵢ⟧-tý prvek
# posloupnosti ⟦A⟧, tj. prvek s indexem ⟦aᵢ⟧ (nikoliv prvek
# s indexem ⟦i⟧). Napište funkci, která sečte prvních ‹count› prvků
# posloupnosti ⟦B⟧ (t.j. ty prvky posloupnosti ⟦A⟧, kterých «indexy»
# jsou po sobě jdoucí Fibonacciho čísla).

# Například ‹fibfibsum(6)› se vypočte takto:
#
#  ⟦ a₁ + a₁ + a₂ + a₃ + a₅ + a₈ = 1 + 1 + 1 + 2 + 5 + 21 = 31 ⟧

def n_fib(n):
    a = 1
    b = 1

    for i in range(n - 2):
        c = a + b
        a = b
        b = c

    return b

def fibfibsum(count):
    a = 1
    a_last = 1
    result = 2

    if count == 1 or count == 2:
        return count

    for i in range(count - 2):
        c = a + a_last
        result += n_fib(c)
        a = a_last
        a_last = c
        
    return result


def main():
    assert fibfibsum(3) == 3
    assert fibfibsum(5) == 10
    assert fibfibsum(6) == 31
    assert fibfibsum(7) == 264
    assert fibfibsum(10) == 139589576542


if __name__ == "__main__":
    main()
