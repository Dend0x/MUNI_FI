from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, pendown, done


# Zobecněte řešení z příkladu ‹pentagon› tak, abyste byli schopni
# vykreslit libovolný pravidelný mnohoúhelník. Toto obecné řešení
# implementujte jako proceduru ‹polygon› s parametry:
#
#  • ‹sides› je počet stran kresleného mnohoúhelníku, a
#  • ‹length› je délka každé z nich.

def polygon(sides, length):
    for i in range(sides):
        forward(length)
        left(360.0 / sides)


def main():
    polygon(7, 40)

    penup()
    forward(120)
    pendown()

    polygon(6, 60)

    penup()
    forward(100)
    pendown()

    polygon(3, 80)

    done()


if __name__ == "__main__":
    main()
