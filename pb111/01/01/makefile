UNIT = 01
SRC_D = d1_triangle.asm d2_factorial.asm
SRC_E = e1_isodd.asm e2_nor.asm
SRC_P = p1_fib.asm p2_adder.asm p3_gcd.asm p4_prime.asm p5_popcnt.asm p6_abundant.asm
SRC_R = r1_reverse.asm r2_hamming.asm r3_packed.asm r4_bitswap.asm r5_collatz.asm r6_shift.asm
SRC_T =

TCC      = tinycc
TVM      = tinyvm

-include ../local.mk

BIN_T   := ${SRC_T:.asm=.bin}
BIN_D   := ${SRC_D:.asm=.bin}
BIN_E   := ${SRC_E:.asm=.bin}
BIN_P   := ${SRC_P:.asm=.bin}
BIN_R   := ${SRC_R:.asm=.bin}

BIN_T   := ${BIN_T:.c=.bin}
BIN_D   := ${BIN_D:.c=.bin}
BIN_E   := ${BIN_E:.c=.bin}
BIN_P   := ${BIN_P:.c=.bin}
BIN_R   := ${BIN_R:.c=.bin}

BIN      = $(BIN_T) $(BIN_D) $(BIN_E) $(BIN_P) $(BIN_R)
SRC      = $(SRC_T) $(SRC_D) $(SRC_E) $(SRC_P) $(SRC_R)
DEP      = ${BIN_D:%.bin=.%.d} ${BIN_P:%.bin=.%.d} ${BIN_T:%.bin=.%.d} ${BIN_E:%.bin=.sol.%.d}

.SUFFIXES: .asm .c .bin

all: $(BIN)

clean:
	@rm -f $(BIN) $(DEP)
	@rm -f *.core core *~ a.out .check.*.out valgrind.out a.out

.asm.bin:
	@echo $(@): $(<) makefile > $(@:%.bin=.%.d)
	$(TCC) --no-prolog -o $(@) $(<)
	$(TVM) $(@)

.c.bin:
	@echo $(@): $(<) makefile > .$(@:%.bin=.%.d)
	$(TCC) -o $(@) $(<)
	$(TVM) $(@)

.c:
	@echo did you mean $(@).bin?

-include $(DEP)

.PHONY: all clean
