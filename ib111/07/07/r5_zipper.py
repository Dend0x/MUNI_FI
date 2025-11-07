from ib111 import week_07, except_data_structures  # noqa


# † Naprogramujte datovou strukturu ‘zipper’: jedná se o strukturu
# podobnou zřetězenému seznamu, s jedním důležitým rozdílem: přesto,
# že používá jednoduché zřetězení (nikoliv dvojité), lze se v něm
# efektivně pohybovat oběma směry. Nicméně na rozdíl od dvojitě
# zřetězeného seznamu nám zipper umožňuje udržovat pouze jediný
# kurzor.
#
# Jak zipper funguje? Používá následující strukturu:
#
#  ┌───────────┐  ┌───┐  ┌────────┐  ┌───┐  ┌────────────┐
#  │ left tail │◀─│ … │◀─│ cursor │─▶│ … │─▶│ right tail │
#  └───────────┘  └───┘  └────────┘  └───┘  └────────────┘
#
# Jak efektivně kurzor posunout o jednu pozici doleva nebo doprava
# si pravděpodobně dovedete představit. Pro jednoduchost budeme
# uvažovat pouze neprázdný zipper.
#
# Pro zajímavost: zipper lze implementovat také pomocí dvojice
# zásobníků, a tato implementace je typicky efektivnější. V tomto
# cvičení ale preferujeme použití zřetězených struktur.
#
# V tomto příkladu je zakázáno použití Pythonovských datových struktur
# seznam, množina, slovník.

class Node:
    def __init__(self, num: int) -> None:
        self.value = num
        self.next = None

class Zipper:
    def __init__(self, num: int) -> None:
        self.left: Node = None
        self.right: Node = None
        self.actual = Node(num)

    # Vrátí aktuální hodnotu kurzoru.

    def cursor(self) -> int:
        return self.actual.value

    # Vloží prvek nalevo od kurzoru.

    def insert_left(self, num: int) -> None:
        new = Node(num)
        new.next = self.left
        self.left = new

    # Smaže prvek nalevo od kurzoru, existuje-li takový, a vrátí
    # jeho hodnotu. Jinak vrátí ‹None›.

    def delete_left(self) -> int | None:
        if self.left is None:
            return
        val = self.left.value
        self.left = self.left.next
        return val

    # Posune kurzor o jednu pozici doleva. Není-li se kam posunout,
    # metoda neudělá nic.

    def shift_left(self) -> None:
        if self.left is None:
            return

        new_right = Node(self.actual.value)
        new_right.next = self.right
        self.right = new_right

        self.actual = self.left
        self.left = self.actual.next

    # Posune kurzor o jednu pozici doprava. Není-li se kam posunout,
    # metoda opět neudělá nic.

    def shift_right(self) -> None:
        if self.right is None:
            return

        new_left = Node(self.actual.value)
        new_left.next = self.left
        self.left = new_left

        self.actual = self.right
        self.right = self.actual.next


def main() -> None:
    zipper = Zipper(1)  # [1]
    assert zipper.cursor() == 1
    assert zipper.delete_left() is None
    zipper.insert_left(1)  # 1 [1]
    zipper.insert_left(2)  # 1 2 [1]
    assert zipper.cursor() == 1
    assert zipper.delete_left() == 2  # 1 [1]
    zipper.insert_left(3)  # 1 3 [1]
    zipper.insert_left(3)  # 1 3 3 [1]
    assert zipper.cursor() == 1
    zipper.shift_left()    # 1 3 [3] 1
    zipper.shift_right()   # 1 3 3 [1]
    assert zipper.cursor() == 1
    zipper.shift_left()   # 1 3 [3] 1
    assert zipper.delete_left() == 3  # 1 [3] 1
    assert zipper.delete_left() == 1  # [3] 1
    assert zipper.cursor() == 3
    zipper.insert_left(2)  # 2 [3] 1
    zipper.insert_left(3)  # 2 3 [3] 1
    assert zipper.cursor() == 3
    zipper.shift_right()  # 2 3 3 [1]
    assert zipper.cursor() == 1
    zipper.shift_right()  # no change
    assert zipper.cursor() == 1
    zipper.shift_left()  # 2 3 [3] 1
    assert zipper.cursor() == 3
    assert zipper.delete_left() == 3  # 2 [3] 1
    zipper.shift_left()  # [2] 3 1
    assert zipper.delete_left() is None
    zipper.shift_right()  # 2 [3] 1
    assert zipper.cursor() == 3
    assert zipper.delete_left() == 2
    zipper.shift_right()  # 3 [1]
    assert zipper.cursor() == 1
    assert zipper.delete_left() == 3
    assert zipper.delete_left() is None
    zipper.shift_right()
    assert zipper.cursor() == 1
    assert zipper.delete_left() is None


if __name__ == '__main__':
    main()
