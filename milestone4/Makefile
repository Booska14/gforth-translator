#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
TESTFILES = testFiles/*
OPTIONS =
TRANSLATOR = ./translator.py

help:
	$(TRANSLATOR) -h

clean:
	rm -f stutest.* *.pyc

stutest.out:
	touch stutest.out
	chmod 755 $(TRANSLATOR)
	$(TRANSLATOR) $(OPTIONS) $(TESTFILES) > stutest.out
	chmod 755 stutest.out
	touch stutest.fs
	chmod 755 stutest.fs
	cat stutest.out > stutest.fs
	gforth stutest.fs

proftest.out: compiler
	touch proftest.out
	chmod 755 $(TRANSLATOR)
