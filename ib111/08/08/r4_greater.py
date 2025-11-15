from ib111 import week_08  # noqa


# † Napište funkci ‹next_greater›, která vrátí nejmenší větší číslo
# se stejnými ciframi jaké má číslo ‹number›. Pokud větší číslo
# neexistuje, funkce vrací ‹None›. Nezkoušejte všechny permutace
# cifer, existuje efektivnejší řešení.

def next_greater(number: int) -> int | None:
    num: list[int] = []
    pivot = -1

    while number > 0:
        num.append(number % 10)
        number //= 10

    for i in range(1, len(num)):
        if num[i] < num[i - 1]:
            pivot = i
            break

    if pivot == -1:
       return None

    minimum = -1
    for i in range(0, pivot):
        if num[i] >  num[pivot] and (minimum == -1 or num[i] <= num[minimum]):
            minimum = i

    if minimum == -1:
        return None

    num[minimum], num[pivot] = num[pivot], num[minimum]

    left = 0
    right = pivot - 1
    while left < right:
        num[left], num[right] = num[right], num[left]
        left += 1
        right -= 1

    number = 0
    for i in range(len(num) - 1, -1, -1):
        number = 10 * number + num[i]
    return number

def main() -> None:
    assert next_greater(12) == 21
    assert next_greater(513) == 531
    assert next_greater(2017) == 2071
    assert next_greater(9) is None
    assert next_greater(111) is None
    assert next_greater(531) is None
    assert next_greater(351) == 513


if __name__ == "__main__":
    main()
