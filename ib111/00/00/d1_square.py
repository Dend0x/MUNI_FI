from ib111 import week_00  # noqa
from turtle import forward, right, done, penup, pendown, setheading


# Smyslem první ukázky je předvést základní „příkazy“ (procedury –
# tento pojem si přesněji vysvětlíme v dalších ukázkách) pro
# kreslení obrázků. Tyto procedury ovládají „želvu“, která se
# pohybuje po plátně a kreslí přitom čáru. Procedura ‹forward› želvě
# poručí, aby se posunula o danou vzdálenost vpřed (a nakreslila
# u toho úsečku ze své původní polohy do své nové polohy). Procedury
# ‹left› a ‹right› nic nekreslí, pouze želvou otočí o daný úhel
# (zadaný v stupních) doleva, resp. doprava.

# Dovolíme-li želvě vracet se „po vlastních stopách“, stačí nám tyto
# 3 procedury na vykreslení libovolného spojitého obrazce. Pro
# začátek zkusíme nakreslit čtverec:

def square():

    # Čtverec lze nakreslit jednoduše jako 4 navazující úsečky
    # stejné délky, přičemž každé dvě po sobě jdoucí svírají
    # pravý úhel.

    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)


# Předchozí definice ‹square› nás ale příliš neuspokojuje: k čemu
# máme počítač, když jsme museli každý krok explicitně popsat?
# Zejména je na první pohled vidět, že příkazy se opakují. Jistě by
# bylo dobré, abychom mohli počítači sdělit, že má nějakou akci
# provést 4×, místo abychom ji zapsali 4× pod sebe – to je v
# podstatě základní mechanismus, kterým nám počítač šetří práci.

def square_loop():

    # Základní formou tzv. «cyklu» (angl. «loop») je příkaz „proveď
    # akci ‹n› krát“, který se v Pythonu zapisuje jako ‹for i in
    # range(n)› – v našem případě bude ‹n = 4›:

    for i in range(4):

        # Následuje tzv. tělo cyklu, které je tvořeno (odsazeným)
        # seznamem příkazů, které se budou opakovat.

        forward(100)
        right(90)

    # Pozorný čtenář si jistě všiml, že definice ‹square› a
    # ‹square_loop› nejsou zcela ekvivalentní: ta druhá obsahuje
    # jedno použití procedury ‹right› navíc. Pro tuto chvíli je nám
    # to jedno, protože není-li volání ‹right› následováno žádným
    # použitím ‹forward›, nebude mít na výsledný obrázek dopad.
    # Nicméně obecně toto neplatí a je potřeba si na podobné
    # «okrajové případy» dávat pozor.


# Následuje definice ‹main›, smyslem které je demonstrovat funkčnost
# dříve definovaných ‹square› a ‹square_loop›.

def main():  # demo

    # Nejprve necháme želvu vykreslit čtverec „naivním“ způsobem,
    # bez použití cyklu (první z definic výše).

    square()

    # Dále želvu požádáme, aby se přesunula na jiné místo plátna,
    # aniž by nakreslila čáru: tento kus kódu pro nás není příliš
    # podstatný, jeho smyslem je pouze vykreslit dva obrázky na jedno
    # plátno, abychom je mohli lehce srovnat.

    penup()
    setheading(0)
    forward(200)
    pendown()

    # Na novém místě plátna požádáme želvu o vykreslení čtverce
    # druhou metodou (cyklem). Jestli jsme se nespletli, budou oba
    # obrázky identické.

    square_loop()

    # Příkazem (procedurou) ‹done› želvě oznámíme, že máme vše
    # vykresleno a program má vyčkat na ukončení uživatelem.

    done()


if __name__ == "__main__":
    main()
