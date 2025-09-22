from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed


# Implementujte proceduru ‹spiral›, která vykreslí čtyřhrannou
# spirálu s ‹rounds› otočeními (počet otočení říká, kolik hran
# musíme překročit, vydáme-li se ze středu spirály po přímce
# libovolným směrem). Parametr ‹step› pak udává počet pixelů,
# o který se hrany postupně prodlužují.

def spiral(rounds, step):
    edge_length = step
    for i in range(rounds):
        forward(edge_length)
        edge_length += step
        left(90)



def main():
    speed(5)
    spiral(5, 10)
    done()


if __name__ == "__main__":
    main()
