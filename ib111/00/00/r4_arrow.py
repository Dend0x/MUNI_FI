from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, done, speed
import math


# Nakreslete obrys šipky zadaných rozměrů (celková šířka ‹width› a
# celková výška ‹height›) a s úhlem špičky ‹angle›. Šipka by měla
# ukazovat v původním směru želvy. Želva nechť je po konci procedury
# ve stejné pozici a orientaci jako před jejím začátkem.

def arrow(width, height, angle):
    left_width = (height / 2.0) / math.tan(math.radians(angle))
    hypotenuse = math.sqrt(left_width ** 2 + (float(height) / 2) ** 2)

    forward(width - left_width)
    left(angle)
    forward(hypotenuse)
    left(180 - 2 * angle)
    forward(hypotenuse)
    if angle == 90:
        left(angle)
    else:
        left(90 - angle)
    forward(width - left_width)
    left(90)
    forward(height)
    left(90)


def main():
    speed(5)
    arrow(150, 100, 90)
    penup()
    forward(200)
    pendown()
    arrow(150, 100, 45)
    done()


if __name__ == "__main__":
    main()
