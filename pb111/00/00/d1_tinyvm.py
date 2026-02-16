from ib111 import week_11

# Tento program implementuje kompletní sémantiku výpočetního stroje,
# který budeme v tomto kurzu používat. Je naprogramován v jazyce
# z 11. týdne kurzu IB111, měli byste tedy samotnému zápisu programu
# bez problémů rozumět. V komentářích je pak vysvětlena sémantika
# (jak stroj pracuje).

# Protože se jedná o spustitelný program, popisuje sémantiku
# výpočetního stroje velmi přesně – můžete jej tedy použít jako
# referenční příručku strojového kódu, který budeme používat.

# Doporučujeme Vám program si pozorně přečíst už nyní, na začátku
# semestru, ale je zcela v pořádku, pokud neporozumíte ihned všemu.
# Očekáváme, že se budete k programu minimálně několik následujících
# týdnů pravidelně vracet. Studium sémantiky nových operací na
# začátku několika příštích kapitol je k tomu ideální příležitostí.

# Jádro celého stroje tvoří procedura ‹step›, která načte, dekóduje
# a provede jednu instrukci. Vstupními parametry jsou:
#
#  1. ‹pc› je aktuální hodnota programového čítače,
#  2. ‹regs› je seznam 16 celých čísel, každé v rozsahu 0 až 65535,
#     jenž reprezentují hodnoty uložené v registrech,
#  3. ‹mem› je seznam 65536 celých čísel, každé v rozsahu 0 až 255,
#     přitom číslo uložené na indexu ‹i› reprezentuje paměťovou
#     buňku s adresou ‹i›.
#
# Návratovou hodnotou je dvojice celých čísel (nová hodnota
# programového čítače, příznak má-li výpočet pokračovat).

def step( pc: int, regs: list[ int ],
          mem: list[ int ] ) -> tuple[ int, int ]:

    # Následující tvrzení popisují základní vstupní podmínky.

    assert 0 <= pc < 65536
    assert len( regs ) == 16
    assert len( mem ) == 65536

    # Abychom mohli instrukci co nejsnadněji provést, dekódujeme ji
    # na několik pojmenovaných hodnot. Hodnota ‹opcode› je číslo
    # operace, složené ze dvou půlslabik – kategorie ‹cat› a
    # konkrétní operace z dané kategorie ‹op›. V šestnáctkovém
    # zápisu tedy ‹opcode = 0x12› značí operaci 2 z kategorie 1.

    opcode  = mem[ pc ]
    cat     = opcode // 16
    op      = opcode % 16

    # Druhá slabika popisuje vstupní a výstupní registr – tyto se
    # uplatní u většiny operací (výjimky tvoří zejména operace
    # z kategorie 0 – speciální instrukce, a kategorie 15 – řízení
    # toku). Je-li šestnáctkový zápis druhé slabiky ‹0x82›, je
    # výstupním registrem ten s číslem 8 (‹t1›) a (prvním) vstupním
    # registrem je registr číslo 2, totiž ‹l2›.

    r_out   = mem[ pc + 1 ] // 16
    r_1     = mem[ pc + 1 ] %  16

    # Třetí a čtvrtá slabika pak popisují buď tzv. přímý (immediate)
    # operand (číselnou hodnotu, která je přímo součástí instrukce)
    # nebo druhý vstupní registr (pro binární operace nad registry,
    # např. ty dobře známé aritmetické). Nemá-li instrukce přímý
    # operand, je poslední slabika nevyužitá.

    imm     = mem[ pc + 3 ] + mem[ pc + 2 ] * 256
    r_2     = mem[ pc + 2 ] // 16
    addr    = imm

    # Než instrukci vykonáme, vypíšeme dekódovanou instrukci a
    # aktuální stav stroje – procedura ‹print_state› nemá na výpočet
    # stroje žádný vliv, není tedy nutné ji blíže zkoumat. Můžete si
    # ji ale přizpůsobit dle vlastního vkusu nebo potřeby.

    print_state( pc, regs, cat, op, imm, r_out, r_1, r_2 )

    # Nyní již následuje samotné vykonání instrukce. První dvě
    # operace jsou z kategorie 14 – řízení stroje. Instrukce ‹asrt›
    # ukončí výpočet s chybou, je-li ve vstupním registru hodnota
    # nula, jinak pokračuje ve výpočtu další instrukcí. Instrukce
    # ‹halt› výpočet zastaví vždy (nikoliv ale chybou).

    if opcode == 0xee and regs[ r_1 ] == 0: # asrt
        return pc, ERROR
    if opcode == 0xef: # halt
        return pc, HALT

    # Následují speciální operace z kategorie 0. Operace ‹copy›
    # uloží do výstupního registru hodnotu registru vstupního,
    # operace ‹put› uloží přímý operand do výstupního registru a
    # konečně ‹sext› provede znaménkové rozšíření spodní slabiky
    # vstupního registru a výsledek uloží do toho výstupního.

    if opcode == 0x0c: # copy
        regs[ r_out ] = regs[ r_1 ]
    if opcode == 0x0d: # put
        regs[ r_out ] = imm
    if opcode == 0x0e: # sext
        regs[ r_out ] = as_signed( regs[ r_1 ], 8 ) % 65536

    # Dále do kategorie 0 patří operace pro obecnou práci s pamětí.
    #
    # Operace ‹st› (store):
    #
    #  • uloží slovo ze vstupního registru
    #  • na adresu, která vznikne jako součet přímého operandu a
    #    hodnoty ve «výstupním» registru (jedná se zde o výjimečné
    #    použití výstupního registru jako vstupní hodnoty).
    #
    # Varianta ‹stb› zapíše pouze spodní slabiku vstupního registru
    # a přepíše tedy jedinou buňku paměti.

    if opcode in [ 0x03, 0x04 ]: # st, stb
        addr = ( addr + regs[ r_out ] ) % 65536

    if opcode == 0x03: # stb
        mem[ addr ] = regs[ r_1 ]  % 256

    if opcode == 0x04: # st
        mem[ addr + 0 ] = regs[ r_1 ] // 256
        mem[ addr + 1 ] = regs[ r_1 ]  % 256

    # Operace ‹ld› analogicky:
    #
    #  • vypočte adresu jako součet přímého operandu a hodnoty ve
    #    «vstupním» registru,
    #  • z vypočtené adresy načte slovo a uloží ho do «výstupního»
    #    registru.
    #
    # Varianta ‹ldb› přečte z paměti pouze jednu slabiku a na celé
    # slovo ji doplní levostrannými nulami.

    if opcode in [ 0x01, 0x02 ]: # ld, ldb
        addr = ( addr + regs[ r_1 ] ) % 65536

    if opcode == 0x01: # ldb
        regs[ r_out ] = mem[ addr ]

    if opcode == 0x02: # ld
        regs[ r_out ] = mem[ addr ] * 256 + mem[ addr + 1 ]

    # Konečně jsou v kategorii 0 operace ‹push› a ‹pop› pro práci se
    # zásobníkem. Jejich efekt je implementován pomocnými
    # procedurami ‹push› a ‹pop› níže, protože stejný efekt budeme
    # potřebovat i při implementaci některých dalších operací.
    #
    # Operace ‹push› sníží hodnotu uloženou v registru ‹sp› o dvě a
    # na výslednou adresu uloží slovo ze vstupního registru.
    #
    # Operace ‹pop› analogicky nejprve přečte slovo uložené na
    # adrese dané registrem ‹sp›, uloží ho do výstupního registru a
    # konečně hodnotu registru ‹sp› o dvě zvýší.

    if opcode == 0x0a: # push
        push( regs, mem, regs[ r_1 ] )
    if opcode == 0x0b: # pop
        regs[ r_out ] = pop( regs, mem )

    # Tím je kategorie 0 vyřešena. Dále pokračujeme kategorií 15,
    # která obsahuje operace pro řízení toku. Operace ‹call› uloží
    # hodnotu programového čítače na zásobník (podobně jako operace
    # ‹push›) – jedná se o tzv. návratovou adresu. Dále nastaví ‹pc›
    # na hodnotu přímého operandu, čím předá řízení podprogramu na
    # této adrese uloženému.

    if opcode == 0xfe: # call
        push( regs, mem, pc )
        return imm, CONT

    # Operace ‹ret› ukončí vykonávání podprogramu a řízení vrátí
    # volajícímu – návratovou adresu načte ze zásobníku podobně jako
    # operace ‹pop›. Tuto adresu nezapomeneme zvýšit, protože adresa
    # na uložená zásobníku ukazuje na instrukci ‹call›, která volání
    # způsobila.

    if opcode == 0xff: # ret
        return pop( regs, mem ) + 4, CONT

    # Konečně operace skoků – nepodmíněné ‹jmp› a podmíněné ‹jz› a
    # ‹jnz› – pouze nastaví programový čítač na hodnotu přímého
    # operandu. Podmíněný skok se provede v případě, že je hodnota
    # vstupního registru nulová (‹jz›) nebo naopak nenulová (‹jnz›).
    # Není-li podmínka splněna, tyto operace nemají žádný efekt a
    # výpočet pokračuje další instrukcí.

    if cat == 0xf and ( op == 0 or # jmp
                        op == 1 and regs[ r_1 ] == 0 or # jz
                        op == 2 and regs[ r_1 ] != 0 ): # jnz
        return imm, CONT

    # Kategorie 1 až 3 obsahují binární aritmetické operace
    # v několika variantách:
    #
    # • operace z kategorie 1 použije přímý operand jako levý a
    #   vstupní registr jako pravý,
    # • v kategorii 2 je tomu naopak, levý operand je vstupní
    #   registr a pravý operand je přímý,
    # • konečně kategorie 3 pracuje se dvěma vstupními registry
    #   (přímý operand nemá).
    #
    # Implementace aritmetických operací naleznete v čisté funkci
    # ‹arith› definované níže.

    if cat == 1:
        regs[ r_out ] = arith( op, imm, regs[ r_1 ] )
    if cat == 2:
        regs[ r_out ] = arith( op, regs[ r_1 ], imm )
    if cat == 3:
        regs[ r_out ] = arith( op, regs[ r_1 ], regs[ r_2 ] )

    # Konečně kategorie 10 a 11 provádí aritmetické srovnání dvou
    # hodnot – buď ve variantě se dvěma registry, nebo srovnání
    # vstupního registru s přímým operandem.

    if cat == 0xa:
        regs[ r_out ] = compare( op, regs[ r_1 ], regs[ r_2 ] )
    if cat == 0xb:
        regs[ r_out ] = compare( op, regs[ r_1 ], imm )

    # Tím je implementace kompletní. S výjimkou několika málo
    # operací pokračuje výpočet další instrukcí, tzn. té, která je
    # uložena na adrese o 4 vyšší, než byla ta aktuální (každá
    # instrukce je kódována čtyřmi slabikami).

    return pc + 4, CONT

# Následující dva podprogramy realizují operace se zásobníkem –
# adresa vrcholu zásobníku je uložena v registru ‹sp› (registr číslo
# 15).

def push( regs: list[ int ], mem: list[ int ], val: int ) -> None:
    regs[ 15 ] = ( regs[ 15 ] - 2 ) % 65536
    mem[ regs[ 15 ] + 0 ] = val // 256
    mem[ regs[ 15 ] + 1 ] = val  % 256


def pop( regs: list[ int ], mem: list[ int ] ) -> int:
    rv = mem[ regs[ 15 ] ] * 256 + mem[ regs[ 15 ] + 1 ]
    regs[ 15 ] = ( regs[ 15 ] + 2 ) % 65536
    return rv

# Čistá funkce ‹as_signed› bijektivně zobrazí celé číslo ⟦n⟧
# z rozsahu ⟦⟨0, 2ᵇ)⟧ na číslo v rozsahu ⟦⟨-2ᵇ⁻¹, 2ᵇ⁻¹)⟧, metodou
# známou jako dvojkový doplňkový kód. Opačné zobrazení lze v Pythonu
# provést velmi jednoduše, jako ‹m % 2 ** b›. Protože stejný výraz
# popisuje zkrácení výsledku, které se používá při bezznaménkové
# aritmetice s pevnou šířkou slova, budeme jej níže zapisovat přímo,
# bez použití pomocné funkce. Zobrazení realizované funkcí
# ‹as_signed› budeme níže značit ⟦t(n)⟧.

def as_signed( num: int, bits: int ) -> int:
    mod = 2 ** bits
    num = num % mod
    return num if num < mod // 2 else num - mod


# Čistá funkce ‹arith› realizuje základní aritmetické a logické
# operace – sčítání, odečítání, násobení a dělení se zbytkem, bitové
# logické operace a bitové posuvy. Vstupem jsou dvě celá čísla
# ‹op_1› a ‹op_2› v rozsahu ⟦⟨0, 2¹⁶)⟧, výsledek je v témže rozsahu.

def arith( op: int, op_1: int, op_2: int ) -> int:

    # Užitečnou vlastností dvojkového doplňkového kódu je, že
    # operace sčítání (odečítání) a násobení se provádí zcela
    # stejně, jako jejich bezznaménkové verze – platí:
    #
    #  ⟦ t(a) + t(b) = t(a + b)
    #    t(a) - t(b) = t(a - b)
    #    t(a) ⋅ t(b) = t(a ⋅ b) ⟧
    #
    # Pro dělení podobná rovnost žel neplatí, proto musíme
    # rozlišovat operace ‹sdiv›/‹udiv› a ‹smod›/‹umod›.

    if op == 0x1: return ( op_1 + op_2 ) % 65536
    if op == 0x2: return ( op_1 - op_2 ) % 65536
    if op == 0x3: return ( op_1 * op_2 ) % 65536
    if op == 0x4: return op_1 // op_2
    if op == 0x6: return op_1 %  op_2

    # Pro jednoduchost budeme při dělení dodržovat znaménkovou
    # konvenci, která se používá v jazyce C, a která je žel odlišná
    # od té, která se používá v jazyce Python.

    if op == 0x5 or op == 0x7: # signed div/rem
        dividend = as_signed( op_1, 16 )
        divisor = as_signed( op_2, 16 )
        quot, rem = divmod( dividend, divisor )

        if ( dividend > 0 ) != ( divisor > 0 ) and rem != 0:
            rem -= divisor
        if quot < 0 and rem != 0:
            quot += 1

        return ( quot if op == 0x5 else rem ) % 65536

    # Bitové logické operace se provádí po jednotlivých bitech
    # (číslicích ve dvojkovém zápisu). Každá operace provede na
    # odpovídajících bitech v operandech příslušnou logickou operaci
    # (‹and›, ‹or› nebo ‹xor›), čím získá odpovídající bit výsledku.
    # Operandy jsou vždy 16bitové.

    if op in [ 0xa, 0xb, 0xc ]:
        result = 0
        for idx in range( 16 ):
            bit_1 = op_1 // 2 ** idx % 2
            bit_2 = op_2 // 2 ** idx % 2

            if op == 0xa:
                bit_r = bit_1 == 1 and bit_2 == 1
            if op == 0xb:
                bit_r = bit_1 == 1 or  bit_2 == 1
            if op == 0xc:
                bit_r = ( bit_1 == 1 ) != ( bit_2 == 1 )

            result += bit_r * 2 ** idx

        return result

    # Bitové posuvy jsou jednoduché – posuv doleva odpovídá násobení
    # a posuv doprava dělení příslušnou mocninou dvojky. Při pravých
    # posuvech (dělení) musíme opět rozlišit bezznaménkovou (‹shr›)
    # a znaménkovou (‹sar›) verzi. Znaménkový (tzv. aritmetický)
    # posuv pak lze chápat i jako operaci, která posouvá jednotlivé
    # bity doprava, ale zleva doplňuje místo nul kopie znaménkového
    # bitu.

    if op == 0xd:
        return ( op_1 * 2 ** op_2 ) % 65536
    if op == 0xe:
        return ( op_1 // 2 ** op_2 ) % 65536
    if op == 0xf:
        return ( as_signed( op_1, 16 ) // 2 ** op_2 ) % 65536

    assert False


# Čistá funkce ‹compare› realizuje aritmetická srovnání. Krom
# rovnosti (⟦=, ≠⟧) jsou všechny operace závislé na tom, pracujeme-li
# se znaménkovou reprezentací – v dvojkovém doplňkovém kódu jsou
# kódy záporných čísel větší, než kódy čísel kladných, např.
# 16bitové kódování -1 je ‹0xffff›, přitom 16bitové kódování +1 je
# ‹0x0001›, výsledek ‹0xffff < 0x0001› ale jistě v tomto kontextu
# nedává smysl.

def compare( op: int, arg_1: int, arg_2: int ) -> int:

    sig_1 = as_signed( arg_1, 16 )
    sig_2 = as_signed( arg_2, 16 )

    if op == 0x0: result = arg_1 == arg_2
    if op == 0xf: result = arg_1 != arg_2

    if op == 0x1: result = arg_1 <  arg_2
    if op == 0x2: result = arg_1 <= arg_2
    if op == 0x3: result = arg_1 >  arg_2
    if op == 0x4: result = arg_1 >= arg_2

    if op == 0xa: result = sig_1 <  sig_2
    if op == 0xb: result = sig_1 <= sig_2
    if op == 0xc: result = sig_1 >  sig_2
    if op == 0xd: result = sig_1 >= sig_2

    return 1 if result else 0


# Tím je implementace ‹step› a jejích pomocných funkcí hotova. Za
# pomoci ‹step› je již velmi jednoduché implementovat podprogram
# ‹run›, který provede celý výpočet. Program je uložen od adresy 0.

CONT = 0
HALT = 1
ERROR = 2


def run( regs: list[ int ], mem: list[ int ] ) -> bool:
    print( "  pc inst op_1 op_2  out │ " +
           "  rv   l1   l2   l3   l4   l5   l6   l7 " +
           "  t1   t2   t3   t4   t5   t6   sp   bp" )
    status = CONT
    pc = 0

    while status == CONT:
        pc, status = step( pc, regs, mem )

    return status == HALT


# Další částí je podprogram ‹read_program›, který ze vstupního
# souboru přečte počáteční stav paměti (kterému můžeme také říkat
# «program»).

def write_nibble( mem: list[ int ], index: int, nibble: int ) -> None:
    mem[ index // 2 ] += nibble * 16 if index % 2 == 0 else nibble

def read_program( filename: str ) -> list[ int ]:
    mem = [ 0 for i in range( 65536 ) ]
    index = 0

    with open( filename, 'r' ) as file:
        for line in file.readlines():
            if line[ 0 ] == ';':
                break
            for word in line.rstrip().replace( "'", '' ).split( ' ' ):
                for hex_nibble in word:
                    write_nibble( mem, index, FROM_HEX[ hex_nibble ] )
                    index += 1

    return mem

# Zbývá vstupní bod (podprogram ‹main›) a procedury pro výpis
# aktuálního stavu výpočetního stroje. Zbývající kód není pro
# pochopení funkčnosti výpočetního stroje ‹tiny› nijak podstatný.

def main() -> None:
    from sys import argv
    filename = argv[ 1 ] if len( argv ) >= 2 else 'tiny.out'
    mem = read_program( filename )
    regs = [ 0 for i in range( 16 ) ]
    ok = run( regs, mem )

    if not ok:
        print( "program aborted" )
        assert False


# Poslední část tvoří výpis jednotlivých kroků výpočtu (resp. stavů
# mezi nimi) na obrazovku – již zmiňovaná procedura ‹print_state› a
# k ní náležící pomocné podprogramy.

# Čistá funkce ‹op_name› ze zadaného čísla operace (rozděleného na
# kategorii a podoperaci) získá její název. Tabulky zde uvedené
# můžete využít jako referenci při čtení podprogramu ‹step›, nebo
# jako pomůcku pro přímé čtení strojového kódu.

def op_name( cat: int, op: int ) -> str:

    names = {}

    if cat in [ 1, 2, 3 ]:
        names = { 0x1: 'add ', 0x2: 'sub ', 0x3: 'mul ',
                  0x4: 'udiv', 0x5: 'sdiv', 0x6: 'urem', 0x7: 'srem',
                  0xa: 'and ', 0xb: 'or  ', 0xc: 'xor ',
                  0xd: 'shl ', 0xe: 'shr ', 0xf: 'sar ' }

    if cat == 0:
        names = { 0xa: 'push', 0xb: 'pop ',
                  0xc: 'copy', 0xd: 'put ', 0xe: 'sext',
                  0x1: 'ldb ', 0x2: 'ld  ', 0x3: 'stb ', 0x4: 'st  ' }

    if cat == 0xf:
        names = { 0x0: 'jmp ', 0x1: 'jz  ', 0x2: 'jnz ',
                  0xe: 'call', 0xf: 'ret ' }

    if cat in [ 0xa, 0xb ]:
        names = { 0x0: 'eq  ', 0xf: 'ne  ',
                  0x1: 'ult ', 0x2: 'ule ', 0x3: 'ugt ', 0x4: 'uge ',
                  0xa: 'slt ', 0xb: 'sle ', 0xc: 'sgt ', 0xd: 'sge ' }

    if cat == 0xe:
        names = { 0xe: 'asrt', 0xf: 'halt' }

    return names.get( op, '????' )


# Analogicky čistá funkce ‹reg_name› přiřadí danému číslu registru
# odpovídající jméno.

def reg_name( idx: int ) -> str:
    names = [ 'rv', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7',
              't1', 't2', 't3', 't4', 't5', 't6', 'bp', 'sp' ]
    return names[ idx ]


def print_state( pc: int, regs: list[ int ],
                 cat: int, op: int, imm: int,
                 r_out: int, r_1: int, r_2: int ) -> None:
    opcode  = cat * 16 + op
    imm_1   = cat in [ 0x1, 0xf ] or opcode == 0x0d
    imm_2   = cat in [ 0x0, 0x2, 0xb ]

    str_out  = "→ " + reg_name( r_out )
    str_op_1 = to_hex( imm ) if imm_1 else "  " + reg_name( r_1 )
    str_op_2 = to_hex( imm ) if imm_2 else "  " + \
               reg_name( r_1 if imm_1 else r_2 )

    ign_out = cat == 0xf or opcode == 0x0a
    ign_1   = opcode in [ 0x0b, 0xff ]
    ign_2   = cat == 0x0 and op in [ 0xa, 0xb, 0xc, 0xd ] or \
              cat == 0xf and op in [ 0x0, 0xe, 0xf ]

    if cat == 0xe:
        ign_1   = op == 0xf
        ign_2   = True
        ign_out = True

    if opcode in [ 0x05, 0x07 ]:
        str_op_2, str_out = str_out, str_op_2

    if ign_out: str_out  = "    "
    if ign_1:   str_op_1 = "    "
    if ign_2:   str_op_2 = "    "

    print( to_hex( pc ), op_name( cat, op ), str_op_1, str_op_2, str_out,
           "│ " + ' '.join( [ to_hex( v ) for v in regs ] ) )

# Konečně pomocné funkce pro konverzi čísel z/do šestnáctkového
# zápisu.

FROM_HEX = { '0':  0, '1':  1, '2':  2, '3':  3,
             '4':  4, '5':  5, '6':  6, '7':  7,
             '8':  8, '9':  9, 'a': 10, 'b': 11,
             'c': 12, 'd': 13, 'e': 14, 'f': 15 }

TO_HEX = dict( [ ( v, k ) for k, v in FROM_HEX.items() ] )

def to_hex( num: int ) -> str:
    out = ''
    for i in range( 4 ):
        out = TO_HEX[ num % 16 ] + out
        num //= 16
    return out


if __name__ == '__main__':
    main()
