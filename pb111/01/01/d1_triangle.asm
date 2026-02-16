; V této ukázce napíšeme jednoduchý program, který rozhodne
; zadává-li trojice vstupních čísel trojúhelník (tzn. určí, zda
; vstup splňuje potřebné trojúhelníkové nerovnosti).

; V Pythonu tento problém řeší výraz:
;
;     (a + b > c) and (b + c > a) and (c + a > b)
;

; Nejprve si nachystáme testovací kód a testovací data (tuto část
; můžete při čtení přeskočit – to bude platit i v dalších ukázkách).
; Testovací kód načte testovací data z paměti – jak tyto instrukce
; fungují si blíže ukážeme v dalších kapitolách.

; Vstup budeme očekávat v registrech ‹l1›, ‹l2› a ‹l3› a výsledek (0
; nebo 1) zapíšeme do registru ‹rv›.

main: ; driver
    ld   l7, data   → l1
    add  l7, 2      → l7
    ld   l7, data   → l2
    add  l7, 2      → l7
    ld   l7, data   → l3
    add  l7, 2      → l7
    eq   l1, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ;  l1  l2  l3  →  rv
    .word  3,  4,  5,     1
    .word  1,  1,  1,     1
    .word  1,  1,  3,     0
    .word  2,  3,  1,     0
    .word -1,  0

check:
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení

; Protože potřebujeme implementovat konjunkci, nastavíme do registru
; ‹rv› její neutrální hodnotu – ‹true›, tzn. 1. Každý ze tří testů
; pak bude implementovaný stejně – sečte dvě strany, srovná tento
; součet se stranou třetí a výsledek tohoto srovnání přidá do
; registru ‹rv› bitovou operací ‹and›.

    put 1      → rv

; Každý z následovných tří bloků realizuje jednu nerovnost.
; Mezivýsledky ukládáme do registrů ‹t1› (součet stran) a ‹t2›
; (výsledek srovnání součtu se zbývající stranou).

    add l1, l2 → t1
    sgt t1, l3 → t2
    and rv, t2 → rv

    add l1, l3 → t1
    sgt t1, l2 → t2
    and rv, t2 → rv

    add l2, l3 → t1
    sgt t1, l1 → t2
    and rv, t2 → rv

; Tím je výpočet ukončen a protože je již výsledek uložen ve
; správném registru, nezbývá než předat řízení zpátky do testovacího
; kódu.

    jmp check
