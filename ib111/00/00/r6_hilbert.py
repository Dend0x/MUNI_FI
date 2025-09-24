from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, \
    pendown, speed, delay, done


# ‡ Nakreslete Hilbertovu křivku se stranou délky ‹size› a počtem
# dělení ‹iterations›. Hilbertova křivka vzniká, podobně jako
# Kochova vločka, opakovaným dělením stávajícího obrazce na zmenšené
# kopie sebe sama. Podrobnější návod, jak křivku nakreslit (na
# papír), naleznete na adrese ‹https://is.muni.cz/go/9fh9k4›.

def hilbert(size, iterations):
    if iterations == 0:
        forward(size)
        return

    hilbert(size / 2.0, iterations - 1)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)

    


def main():
    speed(1)
    delay(0)
    hilbert(100.0, 3)

    penup()
    forward(20)
    pendown()

    hilbert(100.0, 0)

    penup()
    forward(20)
    pendown()

    hilbert(100.0, 0)

    penup()
    forward(20)
    pendown()

    hilbert(100.0, 0)

    done()


if __name__ == "__main__":
    main()
