; Napište program, který určí, kolik je jedniček v binárním zápisu
; čísla uloženého v registru ‹l6›. Výsledek uložte do registru ‹rv›
; a poté proveďte skok na návěstí ‹check›. Hodnotu registru ‹l7›
; nijak neměňte.

main:
    ld   l7, data   → l6
    eq   l6, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; input, expect
    .word  0x00,      0
    .word  0x01,      1
    .word  0x02,      1
    .word  0x03,      2
    .word  0xf1,      5
    .word    -1,      0

check:
    add  l7, 2      → l7
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 5
.trigger inc _tc_

solution: ; zde začíná řešení
