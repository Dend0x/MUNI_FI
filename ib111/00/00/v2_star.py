from ib111 import week_00  # noqa
from turtle import forward, penup, pendown, done, setheading, left, right
from math import sin, radians

# Nakreslete hvězdu (viz obrázky níže) s ‹points› paprsky.  (Počet
# paprsků je kladné celé číslo větší než 2). Paprsky hvězdy jsou
# tvořeny rovnoramennými trojúhelníky bez základny, jejichž výška je
# ‹size› (kladné číslo) a úhel svíraný rameny je ‹angle› (v rozsahu
# 1 až 179). Paprsky jsou rovnoměrně rozmístěny do kruhu. Jeden
# z paprsků vždy směřuje na sever.
#
# Poznámka: S extrémními hodnotami parametrů může výsledná „hvězda“
# spíše připomínat zakulacený mnohoúhelník nebo ozubené kolo.

def star_point(angle, size):
    bottom_angle = (180 - angle) / 2.0
    point_side = size - sin(radians(bottom_angle))

    left(bottom_angle)
    forward(point_side)
    right(180 - angle)
    forward(point_side)
    left(bottom_angle)


def star(points, angle, size):
    rotation_angle = 360.0 / points

    for i in range(points):
        star_point(angle, size)
        right(rotation_angle)


def main():
    star(5, 72, 50)

    penup()
    setheading(0)
    forward(200)
    pendown()

    star(6, 30, 50)
    done()


if __name__ == "__main__":
    main()
