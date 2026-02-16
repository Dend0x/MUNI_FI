; Napište program, který určí, zda je zadané číslo sudé nebo liché.
; Vstupní hodnotu ⟦n⟧ naleznete v registru ‹l6›, výsledek uložte do
; registru ‹rv› (0 pro sudá, 1 pro lichá čísla). Po skončení výpočtu
; proveďte skok na návěstí ‹check›. Hodnotu registru ‹l7›
; zachovejte.

main:
    ld   l7, data   → l6
    eq   l6, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; input, expect
    .word     0,      0
    .word    25,      1
    .word   122,      0
    .word  2341,      1
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
