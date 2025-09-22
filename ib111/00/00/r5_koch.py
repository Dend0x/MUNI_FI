from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, \
    pendown, done, speed, delay


# ‡ Pozor! Tento a následující příklad jsou založeny na rekurzi,
# kterou budeme probírat až na konci kurzu. Nemusíte si tedy lámat
# hlavu, pokud je neumíte vyřešit.

# Nakreslete Kochovu vločku, která má stranu o délce ‹size›.
# Parametr ‹depth› udává kolikrát se má provést dělení strany
# vločky. Konstrukce začíná rovnostranným trojúhelníkem, přičemž
# vločka vzniká opakovanou aplikací následovného postupu na všechny
# úsečky, které v daném okamžiku tvoří obrazec:

#  1. vybranou stranu rozdělte na třetiny a prostřední část
#     odstraňte,
#  2. nad prostřední částí sestrojte rovnostranný trojúhelník bez
#     základny: danou stranu jste tak nahradili sekvencí 4 úseček:
#     2 zbývající krajní třetiny původní strany a 2 ramena přidaného
#     trojúhelníku,

# Daná iterace končí rozdělením poslední úsečky, která vznikla
# v iteraci předchozí. Proveďte celkem ‹depth› iterací. Testy
# vykreslují vločku hloubky dělení (počet iterací) 0 až 3.

def koch_one_side(size, depth):
    if(depth == 0):
        forward(size)
        return
    koch_one_side(size / 3.0, depth - 1)
    right(60)
    koch_one_side(size / 3.0, depth - 1)
    left(120)
    koch_one_side(size / 3.0, depth - 1)
    right(60)
    koch_one_side(size / 3.0, depth - 1)

def koch_snowflake(size, depth):
    for i in range(6):
        koch_one_side(size, depth)
        left(60)



def main():
    speed(1)
    delay(0)
    koch_snowflake(70.0, 4)
    penup()
    forward(100)
    pendown()

    #koch_snowflake(70.0, 1)
    #penup()
    #forward(100)
    #pendown()

    #koch_snowflake(70.0, 2)
    #penup()
    #forward(100)
    #pendown()

    #koch_snowflake(70.0, 3)
    done()


if __name__ == "__main__":
    main()
