from ib111 import week_02  # noqa


# Napište predikát, který ověří, zda je číslo ‹number› palindrom,
# zapíšeme-li jej v desítkové soustavě. Palindrom se vyznačuje tím,
# že je stejný při čtení zleva i zprava.

def get_digit(number, k):
    return (number // 10 ** k) % 10

def digit_count(number):
    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count


def is_palindrome(number):
    number_digit_count = digit_count(number)
    for i in range(number_digit_count // 2):
        if get_digit(number, i) != get_digit(number, number_digit_count - i - 1):
            return False

    return True


def main():
    assert is_palindrome(7)
    assert is_palindrome(1221)
    assert is_palindrome(12121)
    assert not is_palindrome(1212)
    assert not is_palindrome(12345)


if __name__ == "__main__":
    main()
