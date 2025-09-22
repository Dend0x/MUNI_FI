from ib111 import week_00  # noqa
from turtle import forward, right, penup, pendown, setheading, \
    done, speed


# Tato (pro tento týden poslední) ukázka předvede použití příkazu
# ‹if›, který slouží k podmíněnému vykonání nějaké akce.  Nejprve si
# ale definujeme pomocnou proceduru ‹triangle›, která by nás již
# neměla překvapit: vykresluje tupoúhlý, rovnoramenný trojúhelník,
# který bude sloužit jako lupínek květiny. Důležitou vlastností této
# procedury je, že zachová pozici i orientaci želvy.

def triangle():
    forward(100)
    right(165)
    forward(52)
    right(30)
    forward(52)
    right(165)


# Vykreslíme nyní stylizovanou květinu, které ale chybí některé
# lupínky: konkrétně ty, jejichž pořadové číslo je dělitelné třemi
# nebo pěti. Květinu budeme vykreslovat v cyklu, jak už je zvykem.
# To, čím se tato ukázka liší od předchozích, je, že samotná
# posloupnost akcí, které se v těle cyklu provedou, se bude iteraci
# od iterace lišit. Parametr nám zadává původní počet lupínků (kolik
# by jich bylo, kdyby žádný nechyběl).

def flower(petals):
    for i in range(petals):

        # Podmínku zapisujeme klíčovým slovem ‹if›, následovaným
        # ‹výrazem›, který se vyhodnotí na booleovskou hodnotu (tzn.
        # ‹True› nebo ‹False›) a za dvojtečkou seznamem příkazů,
        # které se provedou «pouze», vyhodnotil-li se předaný výraz
        # na hodnotu ‹True› (tzn. byl pravdivý).

        # V tomto případě se dotazujeme, zda má indexová proměnná
        # ‹i› nenulový zbytek po dělení jak číslem 3 tak číslem 5:
        # znamená to, že ani jeden z nich není dělitelem. Všimněte
        # si, že podmínku pro „chybějící“ lupínek jsme negovali:
        # lupínek vykreslíme, je-li tato (negovaná) podmínka
        # splněna, tedy bude chybět v případě, že byla splněna
        # původní podmínka ze zadání.

        # Budete-li srovnávat zápis programu s obrázkem,
        # který kreslí, je důležité si uvědomit, že první index je 0
        # (a je tedy dělitelný například i 3), nultý lupínek bude
        # tedy chybět. Kdyby nechyběl, „ukazoval“ by směrem doprava.

        if i % 3 != 0 and i % 5 != 0:
            triangle()

        # Bez ohledu na to, zda jsme lupínek vykreslili nebo
        # nikoliv, musíme se pootočit k vykreslení (nebo přeskočení)
        # dalšího lupínku: tento příkaz se provede v každé iteraci.
        # Protože se pootočíme doprava, lupínky vykreslujeme ve
        # směru hodinových ručiček (přičemž nultý by ukazoval
        # 3 hodiny) – ve stejném směru, kterým ukazují vrcholy
        # trojúhelníků, které lupínky reprezentují.

        right(360.0 / petals)


def main():  # demo
    speed(10)
    flower(15)

    penup()
    setheading(0)
    forward(220)
    pendown()

    flower(30)
    done()


if __name__ == "__main__":
    main()
