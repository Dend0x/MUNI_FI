; Vaším úkolem je tentokrát naprogramovat 32bitovou sčítačku.
; Vstupem jsou 4 16bitové hodnoty uložené v registrech ‹l1› až ‹l4›,
; kde ‹l1› a ‹l3› jsou nižší a ‹l2› a ‹l4› jsou vyšší slova
; sčítanců. Nižší slovo výsledku uložte do ‹rv›, to vyšší pak do
; ‹l6›. Hodnotu v registru ‹l7› neměňte.

main:
    ld   l7, data   → l2
    add  l7, 2      → l7
    ld   l7, data   → l1
    add  l7, 2      → l7
    ld   l7, data   → l4
    add  l7, 2      → l7
    ld   l7, data   → l3
    add  l7, 2      → l7
    eq   l2, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; (  l2  :   l1  ) + (  l4  :   l3  ) → (  l6  :   rv  )
    .word  0x0000, 0x0001,    0x0000, 0x0001,    0x0000, 0x0002
    .word  0x0001, 0x0001,    0x0000, 0x0001,    0x0001, 0x0002
    .word  0x0000, 0xf000,    0x0000, 0x1000,    0x0001, 0x0000
    .word  0xf00f, 0xf00f,    0x1001, 0x1001,    0x0011, 0x0010
    .word      -1,      0

check:
    ld   l7, data   → t1
    eq   l6, t1     → t1
    asrt t1
    add  l7, 2      → l7
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení
	put 0 -> rv
	put 0 -> l6
	add l1, l3 -> rv
	ult rv, l1 -> t1
	ult rv, l3 -> t2
	and t1, t2 -> t1
	jz t1, high
	add l6, 1 -> l6
high:
	add l2, l4 -> l2
	add l2, l6 -> l6
	jmp check