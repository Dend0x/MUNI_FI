from ib111 import week_00  # noqa
from turtle import forward, left, penup, pendown, done, speed


# Procedura, kterou jsme definovali v předchozí ukázce, totiž
# taková, která provede fixní (pokaždé stejnou) posloupnost akcí,
# není příliš zajímavá. Naštěstí lze procedury «parametrizovat».
# Podobně jako u knihovních procedur ‹forward› nebo ‹left› si
# můžeme sami definovat proceduru, které pak při použití
# předáme nějaké číslo (obecněji «hodnotu»). Konkrétní předaná
# hodnota pak bude mít vliv na chování takto definované procedury.

# Zde si definujeme proceduru ‹square›, která se nápadně podobá na
# proceduru ‹square_loop› z první ukázky, s jedním rozdílem: délka
# strany již není pevně daná, ale je nyní proceduře předána jako
# «parametr».

def square(size):
    for i in range(4):
        left(90)
        forward(size)


# Takto definovanou proceduru můžeme opět používat zcela analogicky
# k těm zabudovaným – nyní včetně předání parametru, který diktuje,
# jak velký čtverec si přejeme vykreslit.

def main():  # demo
    speed(5)
    square(100)

    # Připomínáme, že následující tři příkazy slouží pouze k přesunu
    # želvy na jinou pozici na plátně.

    penup()
    forward(100)
    pendown()

    square(50)

    penup()
    forward(200)
    pendown()

    square(170)

    done()


if __name__ == "__main__":
    main()
