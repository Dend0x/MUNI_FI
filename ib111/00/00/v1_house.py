from ib111 import week_00  # noqa
from turtle import forward, penup, pendown, done, setheading, left, right
from math import cos, radians, sqrt

# Nakreslete domeček „jedním tahem“ (viz obrázky níže). Obdélníková
# část domečku má šířku ‹width› a výšku ‹height› (kladná reálná
# čísla), úhel špičky střechy je ‹roof_angle› stupňů (v rozsahu 1 až
# 179).

def house(width, height, roof_angle):
    side_roof_angle = (180 - roof_angle) / 2.0
    roof_side = (width / 2.0) / cos(radians(side_roof_angle))
    for i in range(4):
        if i % 2 == 0:
            forward(width)
        else:
            forward(height)
        right(90)

    left(side_roof_angle)
    forward(roof_side)
    right(180 - roof_angle)
    forward(roof_side)



def main():
    house(150, 100, 75)

    penup()
    setheading(0)
    forward(100)
    pendown()

    house(100, 150, 30)
    done()


if __name__ == "__main__":
    main()
