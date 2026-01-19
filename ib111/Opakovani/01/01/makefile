SRC_D = d1_triangle.py d2_sum.py d3_fibonacci.py d4_cycle.py d5_converge.py
SRC_E = e1_divisors.py e2_powers.py e3_multiples.py
SRC_P = p1_sequence.py p2_nested.py p3_triples.py p4_geometry.py p5_fibsum.py p6_next.py
SRC_R = r1_even.py r2_prime.py r3_coins.py r4_fibfibsum.py r5_abundant.py r6_amicable.py
SRC_T = v1_lvseq.py v2_dnsum.py v3_path.py

CXX      = /packages/run.64/gcc-12.2/bin/c++
TIDY     = /packages/run.64/llvm-15.0.7/bin/clang-tidy
VALGRIND = valgrind
CXXFLAGS = -std=c++20 -Wall -Wextra -Werror
TDYFLAGS = -std=c++20

-include ../local.mk

BIN_T    = ${SRC_T:.cpp=}
BIN_D    = ${SRC_D:.cpp=}
BIN_E    = ${SRC_E:.cpp=}
BIN_P    = ${SRC_P:.cpp=}
BIN_R    = ${SRC_R:.cpp=}

BIN      = $(BIN_T) $(BIN_D) $(BIN_E) $(BIN_P) $(BIN_R)
SRC      = $(SRC_T) $(SRC_D) $(SRC_E) $(SRC_P) $(SRC_R)
DEP      = ${BIN_D:%=.%.d} ${BIN_E:%=.%.d} ${BIN_T:%=.%.d} ${BIN_E:%=.sol.%.d}

_ENV   = CXX="$(CXX)" CXXFLAGS="$(CXXFLAGS)" TDYFLAGS="$(TDYFLAGS)" TIDY="$(TIDY)" VALGRIND="$(VALGRIND)"

all: $(BIN)

clean:
	@rm -f $(BIN) $(DEP)
	@rm -f *.core core *~ a.out .check.*.out valgrind.out a.out

.cpp: makefile .helper.sh
	@env $(_ENV) sh .helper.sh cxx    $< -o $@
	@env $(_ENV) sh .helper.sh tidy   $<
	@env $(_ENV) sh .helper.sh grind ./$@

$(BIN_T): makefile .helper.sh
	@echo building and testing $@
	@env $(_ENV) sh .helper.sh cxx    $@.cpp -o $@
	@env $(_ENV) sh .helper.sh tidy   $@.cpp
	@env $(_ENV) sh .helper.sh grind ./$@

-include $(DEP)

.PHONY: all clean
