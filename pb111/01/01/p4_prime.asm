; Napište program, který rozhodne, je-li hodnota uložená v registru
; ‹l6› prvočíslem (hodnotu interpretujte jako číslo bez znaménka).
; Výsledek (1 pokud prvočíslem je, 0 jinak) uložte do registru ‹rv›
; a proveďte skok na návěstí ‹check›. Hodnotu registru ‹l7› nijak
; neměňte. Provedete-li test na dělitelnost hodnotou ‹x›, přebytečný
; test na dělitelnost hodnotou ‹l6/x› už neprovádějte.

main:
    ld   l7, data   → l6
    eq   l6, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; input, expect
    .word     1,      0
    .word     2,      1
    .word     3,      1
    .word     4,      0
    .word    11,      1
    .word    33,      0
    .word    -1,      0

check:
    add  l7, 2      → l7
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 6
.trigger inc _tc_

solution: ; zde začíná řešení
