from ib111 import week_02  # noqa


def is_valid_card(number):
    result = number % 10
    number //= 10
    i = 0

    while number > 0:
        digit = number % 10
        number //= 10

        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9

        result += digit
        i += 1

    return result % 10 == 0


def digit_count(number):
    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count

def return_prefix(number, prefix_digit_count):
    for i in range(digit_count(number) - prefix_digit_count):
        number //= 10
    return number


def visa_prefix(number):
    return return_prefix(number, 1) == 4


def visa_count(number):
    count = digit_count(number)
    return count == 13 or count == 16 or count == 19


# Napište predikát ‹is_visa›, který je pravdivý, reprezentuje-li
# číslo ‹number› platné číslo platební karty VISA, tj. začíná
# cifrou 4, má 13, 16, nebo 19 cifer a zároveň je platným číslem
# platební karty (viz příklad ‹credit›).

def is_visa(number):
    return visa_prefix(number) and visa_count(number) and is_valid_card(number)


# Dále napište predikát ‹is_mastercard›, který je pravdivý,
# reprezentuje-li číslo ‹number› platné číslo platební karty
# MasterCard, tj. začíná prefixem 50–55, nebo 22100–27209, má 16
# cifer a zároveň je platným číslem platební karty.


def mastercard_prefix(number):
    prefix = return_prefix(number, 2)
    if prefix > 49 and prefix < 56:
        return True

    prefix = return_prefix(number, 5)
    return prefix > 22099 and prefix < 27210


def mastercard_count(number):
    return digit_count(number) == 16


def is_mastercard(number):
    return mastercard_prefix(number) and mastercard_count(number) and is_valid_card(number)


def main():
    assert is_visa(4111111111111111)
    assert is_visa(4012888888881881)
    assert is_visa(4988438843884305)
    assert is_visa(4646464646464644)
    assert is_visa(4199350000000002)
    assert is_visa(4222222222222)
    assert is_visa(4111111111111111110)

    assert not is_visa(411111111111116)
    assert not is_visa(5500000000000004)
    assert not is_visa(4929300836739328)

    assert is_mastercard(5500000000000004)
    assert is_mastercard(5555555555554444)
    assert is_mastercard(5105105105105100)
    assert is_mastercard(5424000000000015)
    assert is_mastercard(2223520443560010)
    assert is_mastercard(5101180000000007)
    assert is_mastercard(2222400070000005)

    assert not is_mastercard(4012888888881881)
    assert not is_mastercard(22004000700000003)
    assert not is_mastercard(5624000000000013)
    assert not is_mastercard(2721000030000016)
    assert not is_mastercard(5101180000000000003)


if __name__ == "__main__":
    main()
