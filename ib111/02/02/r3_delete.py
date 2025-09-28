from ib111 import week_02  # noqa


# Napište funkci ‹delete_to_maximal›, která pro dané číslo ‹number›
# najde největší možné číslo, které lze získat smazáním jedné
# desítkové cifry.


def digit_count(number):
    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count


def get_digit(number, k):
    
    for i in range(k):
        number //= 10
    
    return number % 10


def modify_number(number, i):
    right_number_part = 0
    for j in range(i):
        right_number_part += (number % 10) * 10 ** j
        number //= 10
    
    number //= 10
    number *= 10 ** i
    return number + right_number_part


def delete_to_maximal(number):
    count = digit_count(number)

    for i in range(count - 1, 0, -1):
        if get_digit(number, i) < get_digit(number, i - 1):
            return modify_number(number, i)

    return number // 10


# Napište funkci ‹delete_k_to_maximal›, která pro dané číslo
# ‹number› najde největší možné číslo, které lze získat smazáním
# (vynecháním) ‹k› desítkových cifer.

def delete_k_to_maximal(number, k):
    for i in range(k):
        number = delete_to_maximal(number)
    return number


def main():
    assert delete_to_maximal(54) == 5
    assert delete_to_maximal(45) == 5
    assert delete_to_maximal(100) == 10
    assert delete_to_maximal(123) == 23
    assert delete_to_maximal(4312) == 432
    assert delete_to_maximal(1231) == 231
    assert delete_to_maximal(2331) == 331

    assert delete_k_to_maximal(2331, 2) == 33
    assert delete_k_to_maximal(22331, 2) == 331
    assert delete_k_to_maximal(12345, 4) == 5
    assert delete_k_to_maximal(1234554321, 8) == 55
    assert delete_k_to_maximal(123123123123, 4) == 33123123
    assert delete_k_to_maximal(123321123321, 4) == 33223321
    assert delete_k_to_maximal(11181118111, 9) == 88


if __name__ == "__main__":
    main()
