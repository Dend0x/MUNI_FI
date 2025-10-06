from ib111 import week_03  # noqa


# V tomto domácím úkolu si naprogramujete zjednodušenou variantu hry «2048¹».
# Na rozdíl od původní hry budeme uvažovat jen jednorozměrný hrací plán,
# tj. jeden řádek.
#
# ¹ ‹https://play2048.co/›
#
# Hrací plán budeme reprezentovat pomocí seznamu nezáporných celých čísel;
# nuly budou představovat prázdná místa.
# Například seznam ‹[2, 0, 0, 2, 4, 8, 0]› reprezentuje následující situaci:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │ 2 │   │   │ 2 │ 4 │ 8 │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#
# Základním krokem hry je posun doleva nebo doprava. Při posunu se všechna
# čísla „sesypou“ v zadaném směru, přičemž dvojice stejných číslic se sečtou.
# Posunem doleva se tedy uvedený seznam změní na ‹[4, 4, 8, 0, 0, 0, 0]›.
#
# Abyste si hru mohli vyzkoušet (poté, co úlohu vyřešíte), je vám k dispozici
# soubor ‹game_2048.py›, který vložte do stejného adresáře, jako je soubor
# s vaším řešením, případně jej upravte dle komentářů na jeho začátku
# a spusťte. Hra se ovládá šipkami doleva a doprava, ‹R› hru resetuje
# a ‹Q› ukončí.
#
# Napište proceduru ‹slide›, která provede posun řádku reprezentovaného
# seznamem ‹row›, a to buď doleva (pokud má parametr ‹to_left› hodnotu ‹True›)
# nebo doprava (pokud má parametr ‹to_left› hodnotu ‹False›). Procedura přímo
# modifikuje parametr ‹row› a vrací ‹True›, pokud posunem došlo k nějaké
# změně; v opačném případě vrací ‹False›.


def rotate(row):
    for i in range(len(row) // 2):
        row[i], row[len(row) - i - 1] = row[len(row) - i - 1], row[i]


# Vrací posunutou hlavu když je potřeba, druhý Bool
# když dojde k přepisu

def slide_number(current_index, working_index, row):

    cur_number = row[current_index]
    work_number = row[working_index]

    if current_index == working_index:
        return working_index, False

    if work_number == 0 or work_number == cur_number:
        row[working_index] += cur_number
        row[current_index] = 0
        return working_index + (work_number == cur_number), True

    working_index += 1

    if working_index == current_index:
        return working_index, False

    row[working_index] += cur_number
    row[current_index] = 0

    return working_index, True


def slide(row, to_left):
    if not to_left:
        rotate(row)

    working_index = 0
    changed = False

    for i, number in enumerate(row):
        if number > 0:
            working_index, has_changed = slide_number(i, working_index, row)
            changed = changed or has_changed

    rotate(row) if not to_left else row
    return changed


def main():
    row = [0, 2, 2, 0]
    assert slide(row, True)
    assert row == [4, 0, 0, 0]

    row = [2, 2, 2, 2, 2]
    assert slide(row, False)
    assert row == [0, 0, 2, 4, 4]

    row = [2, 0, 0, 2, 4, 2, 2, 2]
    assert slide(row, True)
    assert row == [4, 4, 4, 2, 0, 0, 0, 0]

    row = [3, 0, 6, 3, 3, 3, 6, 0, 6]
    assert slide(row, False)
    assert row == [0, 0, 0, 0, 3, 6, 3, 6, 12]

    row = [16, 8, 4, 2, 0, 0, 0]
    assert not slide(row, True)
    assert row == [16, 8, 4, 2, 0, 0, 0]


if __name__ == '__main__':
    main()
