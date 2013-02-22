#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
TESTFILESWORKING = testFiles/working/*
TESTFILESFAIL = testFiles/fail/*
OPTIONS = -r -a -t -z

clean:
	rm -f stutest.out *.pyc

stutest.out:
	touch stutest.out
	chmod 755 main.py
	./main.py $(OPTIONS) $(TESTFILESWORKING) $(TESTFILESFAIL)   >> stutest.out
	chmod 755 stutest.out

proftest.out: compiler
	cat $(PROFTEST)
	compiler $(PROFTEST) > proftest.out
	cat proftest.out
