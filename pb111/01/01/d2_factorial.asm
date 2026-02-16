; V této ukázce naprogramujeme jeden z nejjednodušších číselných
; algoritmů vůbec – iterativní výpočet faktoriálu celého kladného
; čísla. Novým prvkem bude tedy «cyklus» – opakované spuštění
; stejného segmentu kódu.

; Testovací kód můžete opět přeskočit, řešení začíná návěstím
; ‹solution›. Vstupní hodnota bude v registru ‹l6›, výsledek pak
; v registru ‹rv›.

main: ; driver
    ld   l7, data   → l6
    eq   l6, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; input, expect
    .word     1,      1
    .word     2,      2
    .word     3,      6
    .word     4,     24
    .word    -1,      0

check:
    add  l7, 2      → l7
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení

; Registr ‹rv› budeme používat jako střadač (akumulátor) – před
; vstupem do cyklu jej nastavíme na neutrální hodnotu 1 a v každé
; iteraci jej vynásobíme počítadlem iterací.

; Jako řídící proměnnou použijeme přímo ‹l6› – protože na pořadí
; násobení nezáleží, můžeme hodnoty násobit sestupně v pořadí ⟦n⋅(n
; - 1)⋅(n - 2) … 1⟧. Jakmile řídící proměnná dosáhne hodnoty nula,
; cyklus ukončíme (musíme si pouze dát pozor, abychom nulou již
; nenásobili).

    put 1 → rv
loop:
    mul rv, l6 → rv
    sub l6, 1  → l6
    jnz l6, loop

    jmp check
