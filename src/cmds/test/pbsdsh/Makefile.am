PROG_ROOT = ../..

AM_CFLAGS = -g -DTEST_FUNCTION -I${PROG_ROOT}/ -I${PROG_ROOT}/${PBS_MACH} --coverage

lib_LTLIBRARIES = libpbsdsh.la

AM_LDFLAGS = @CHECK_LIBS@ ${lib_LTLIBRARIES}

check_PROGRAMS = test_pbsdsh

libpbsdsh_la_SOURCES = scaffolding.c ${PROG_ROOT}/pbsdsh.c
libpbsdsh_la_LDFLAGS = @CHECK_LIBS@ -shared

test_pbsdsh_SOURCES = test_pbsdsh.c

check_SCRIPTS = coverage_run.sh

TESTS = ${check_PROGRAMS} coverage_run.sh

coverage_run.sh:
	echo 'cp -p .libs/pbsdsh.gc* . >/dev/null 2>&1' > $@
	echo 'RESULTS=($$(gcov pbsdsh.gcda))' >> $@
	echo 'PARSED_RESULT="TOTALCOV -- $${RESULTS[1]}: Lines($${RESULTS[5]})- $${RESULTS[3]}"' >> $@
	echo 'echo -e "\033[40m\033[1;33m$$PARSED_RESULT\033[0m"' >> $@
	chmod +x $@

CLEANFILES = coverage_run.sh *.gcno *.gcda *.gcov core *.lo
