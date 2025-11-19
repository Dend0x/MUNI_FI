from ib111 import week_08  # noqa
from d1_countsort import all_lists, is_permutation, is_sorted


# † Implementujte algoritmus řazení haldou. Základní myšlenka
# algoritmu je podobná algoritmu řazení výběrem:
#
#  • vstupní seznam rozdělíme na dvě pomyslné části, neseřazenou
#    (na začátku) a seřazenou (na konci);
#  • v každé iteraci najdeme největší prvek v neseřazené části,
#    přesuneme ho na její konec, a pomyslnou dělící čáru posuneme
#    o jeden prvek doleva.
#
# To, čím se algoritmus od řazení výběrem liší je metoda „hledání“
# onoho největšího prvku. Seznam totiž před samotným začátkem řazení
# přeuspořádáme do formy tzv. haldy, která má tyto vlastnosti:
#
#  • největší prvek je na nulté pozici,
#  • pro prvek na pozici ⟦i⟧ platí, že je větší než prvky na
#    pozicích ⟦2i + 1⟧ a ⟦2i + 2⟧ (existují-li).
#
# Je zřejmé, že nahrazením největšího prvku tuto vlastnost můžeme
# lehce pokazit. Klíčové pozorování je, že její obnovení je snadné
# (a zejména rychlé). Začneme od indexu ‹i = 0› a opakovaně (tak
# dlouho, dokud index ‹i› ukazuje dovnitř neuspořádané části pole):
#
#  • vybereme index největšího prvku z možností ‹i›, ‹2*i + 1› nebo
#    ‹2*i + 2› – pokud jsme vybrali ‹i›, jsme hotovi;
#  • v opačném případě vyměníme vybraný prvek s tím na indexu ‹i›
#    a ‹i› nastavíme na index vybraný v předchozím kroku.
#
# Mělo by být vidět, že za předpokladu, že před výměnou největšího
# prvku měl seznam vlastnosti haldy, uvedenou procedurou je opět
# získá (její obvyklý název je ‹sift_down›). Zbývá tedy zajistit,
# aby mělo vstupní pole tyto vlastnosti i před samotným začátkem
# řazení.
#
# Toho dosáhneme například tak, že budeme opakovaně spouštět
# proceduru ‹sift_down› s počáteční hodnotou ‹i› nastavenou postupně
# na hodnoty ⟦n/2, n/2 - 1, …, 0⟧ kde ⟦n⟧ je délka vstupního
# seznamu. Proč tato procedura funguje se dozvíte například v článku
# „Heapsort“ v anglické wikipedii.

def max_index(records: list[int], i_1: int, i_2: int, i_3: int) -> int:
    if records[i_1] > records[i_2]:
        if records[i_1] > records[i_3]:
            return i_1
        else:
            return i_3
    else:
        if records[i_2] > records[i_3]:
            return i_2
        else:
            return i_3


def sift_down(records: list[int], i: int, n: int) -> None:
    
    while True:
        l_i = 2 * i + 1
        if l_i >= n:
            return
        swap = i
        if records[swap] < records[l_i]:
            swap = l_i
        r_i = 2 * i + 2
        if r_i < n and records[swap] < records[r_i]:
            swap = r_i
        if swap == i:
            return
        records[i], records[swap] = records[swap], records[i]
        i = swap


def heapsort(records: list[int]) -> None:
    for i in range(len(records)//2, -1, -1):
        sift_down(records, i, len(records))

    n = len(records)
    while n > 1:
        records[0], records[n - 1] = records[n - 1], records[0]
        n -= 1
        sift_down(records, 0, n)
        print(records)
    


def test_parameters() -> list[tuple[int, int, int]]:
    result = []
    for high in range(10):
        for low in range(high):
            for count in range(1, 5):
                result.append((low, high, count))
    return result


def main() -> None:
    heapsort([])  # should not crash
    for low, high, count in test_parameters():
        for records in all_lists(low, high, count, True, []):
            original = records.copy()
            heapsort(records)
            assert is_permutation(original, records)
            assert is_sorted(records)


if __name__ == "__main__":
    #main()
    i = [5,1,8,9,4]
    heapsort(i)
    print(i)
