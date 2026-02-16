; Napište program, který spočítá bitovou logickou operaci NOR ⟦↓⟧,
; která je zadaná následující tabulkou:
;
; │ ⟦a⟧ │ ⟦b⟧ │ ⟦a ↓ b⟧ │
; ├─────│─────│─────────┤
; │  1  │  1  │    0    │
; │  1  │  0  │    0    │
; │  0  │  1  │    0    │
; │  0  │  0  │    1    │
;
; Vstupní hodnoty ⟦a⟧, ⟦b⟧ naleznete v registrech ‹l5› a ‹l6›,
; výsledek uložte do registru ‹rv›.  Po skončení výpočtu proveďte
; skok na návěstí ‹check›. Hodnotu registru ‹l7› zachovejte.

main:
    ld   l7, data   → l5
    add  l7, 2      → l7
    ld   l7, data   → l6
    add  l7, 2      → l7
    eq   l5, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ;      l5,   l6  → rv
    .word       1,    0, 65534
    .word      22,   16, 65513
    .word      42,   69, 65424
    .word     315, 1234, 64004
    .word      -1,    0

check:
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení
