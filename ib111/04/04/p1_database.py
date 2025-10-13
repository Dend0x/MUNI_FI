from ib111 import week_04  # noqa

# V této úloze budete pracovat s databázovou tabulkou. Tabulka je
# dvojice složená z «hlavičky» a seznamu «záznamů». «Hlavička»
# obsahuje seznam názvů sloupců. Jeden záznam je tvořen seznamem
# hodnot pro jednotlivé sloupce tabulky (pro jednoduchost uvažujeme
# jenom hodnoty typu řetězec). Ne všechny hodnoty v záznamech musí
# být vyplněny – v tom případě mají hodnotu ‹None›.


Header = list[str]
Record = list[str | None]
Table = tuple[Header, list[Record]]


# Vaším úkolem bude nyní otypovat a implementovat následující
# funkce. Funkce ‹get_header› vrátí hlavičku tabulky ‹table›.


def get_header(table: Table) -> Header:
    header, _ = table
    return header


# Funkce ‹get_records› vrátí seznam záznamů z tabulky ‹table›.


def get_records(table: Table) -> list[Record]:
    _, records = table
    return records


# Procedura ‹add_record› přidá záznam ‹record› na konec tabulky
# ‹table›. Můžete předpokládat, že záznam ‹record› bude mít stejný
# počet sloupců jako tabulka.


def add_record(record: Record, table: Table) -> None:
    _, records = table
    records.append(record)


# Predikát ‹is_complete› je pravdivý, neobsahuje-li tabulka ‹table›
# žádnou hodnotu ‹None›.


def has_none(record: Record) -> bool:
    for rec in record:
        if rec is None:
            return True

    return False


def is_complete(table: Table) -> bool:
    _, records = table

    for record in records:
        if has_none(record):
            return False

    return True


# Funkce ‹index_of_column› vrátí index sloupce se jménem ‹name›.
# Můžete předpokládat, že sloupec s jménem ‹name› se v tabulce
# nachází. První sloupec má index 0.


def index_of_column(name: str, header: Header) -> int:
    for i, column in enumerate(header):
        if name == column:
            return i

    assert False


# Funkce ‹values› vrátí seznam platných hodnot (tzn. takových, které
# nejsou ‹None›) v sloupci se jménem ‹name›. Můžete předpokládat, že
# sloupec se jménem ‹name› se v tabulce nachází.

def values(name: str, table: Table) -> list[str]:
    header, records = table
    column_index = index_of_column(name, header)
    result: list[str] = []

    for record in records:
        record_value = record[column_index]
        if record_value is not None:
            result.append(record_value)

    return result


# Procedura ‹drop_column› smaže sloupec se jménem ‹name› z tabulky
# ‹table›. Můžete předpokládat, že sloupec se jménem ‹name› se
# v tabulce nachází.


def pop_index_list_record(list_to_pop: Record, index: int) -> None:
    for i in range(index, len(list_to_pop) - 1):
        list_to_pop[i] = list_to_pop[i + 1]
    list_to_pop.pop()


def pop_index_list_header(list_to_pop: Header, index: int) -> None:
    for i in range(index, len(list_to_pop) - 1):
        list_to_pop[i] = list_to_pop[i + 1]
    list_to_pop.pop()


def drop_column(name: str, table: Table) -> None:
    header, records = table
    column_index = index_of_column(name, header)

    pop_index_list_header(header, column_index)

    for record in records:
        pop_index_list_record(record, column_index)


# Konečně otypujte následující dvě testovací funkce (jejich
# implementaci neměňte, pouze přidejte typové anotace).


def make_empty() -> tuple[Header, list[Record]]:
    return ["A", "B", "C", "D"], []


def make_table() -> Table:
    return (["A", "B", "C"],
            [["a1", "b1", None],
             ["a2", "b2", "c2"],
             ["a3", None, "c3"]])


def main() -> None:

    # header test
    assert get_header(make_empty()) == ['A', 'B', 'C', 'D']
    assert get_header(make_table()) == ['A', 'B', 'C']

    # records test
    assert get_records(make_empty()) == []
    assert get_records(make_table()) == [["a1", "b1", None],
                                         ["a2", "b2", "c2"],
                                         ["a3", None, "c3"]]

    # add_record test
    tab_1 = make_empty()
    add_record(["a", "b", "c", "d"], tab_1)
    assert tab_1 == (['A', 'B', 'C', 'D'], [['a', 'b', 'c', 'd']])

    tab_2 = make_table()
    add_record(["a4", None, None], tab_2)
    assert tab_2 == (['A', 'B', 'C'],
                     [['a1', 'b1', None], ['a2', 'b2', 'c2'],
                      ['a3', None, 'c3'], ['a4', None, None]])

    # is_complete test
    assert is_complete(make_empty())
    assert not is_complete(make_table())
    assert is_complete((["A", "B", "C"],
                        [["a1", "b1", "c1"], ["a2", "b2", "c2"]]))

    # index_of_column test
    header = ['A', 'C', 'B']
    assert index_of_column('A', header) == 0
    assert index_of_column('C', header) == 1
    assert index_of_column('B', header) == 2

    tab_v = make_table()
    assert values("A", tab_v) == ["a1", "a2", "a3"]
    assert values("B", tab_v) == ["b1", "b2"]
    assert values("C", tab_v) == ["c2", "c3"]
    assert values("B", make_empty()) == []

    # drop_column test
    tab_3 = make_table()
    drop_column("A", tab_3)
    assert tab_3 == (['B', 'C'],
                     [['b1', None], ['b2', 'c2'], [None, 'c3']])

    tab_4 = make_table()
    drop_column("B", tab_4)
    assert tab_4 == (['A', 'C'],
                     [['a1', None], ['a2', 'c2'], ['a3', 'c3']])

    tab_5 = make_empty()
    drop_column("D", tab_5)
    assert tab_5 == (['A', 'B', 'C'], [])


if __name__ == "__main__":
    main()
