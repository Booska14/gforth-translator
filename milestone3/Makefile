#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
TESTFILESWORKING = testFiles/working/*
TESTFILESFAIL = testFiles/fail/*
OPTIONS = -a -r -z
TRANSLATOR = ./translator.py

help:
	$(TRANSLATOR) -h

clean:
	rm -f stutest.out *.pyc

stutest.out:
	touch stutest.out
	chmod 755 $(TRANSLATOR)
	$(TRANSLATOR) $(OPTIONS) $(TESTFILESWORKING) $(TESTFILESFAIL)   >> stutest.out
	chmod 755 stutest.out

proftest.out: compiler
	touch proftest.out
	chmod 755 $(TRANSLATOR)
