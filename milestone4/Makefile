#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
TESTFILES = test1.in
OPTIONS =
TRANSLATOR = ./translator.py

help:
	$(TRANSLATOR) -h

clean:
	rm -f stutest.fs *.pyc

stutest.out:
	touch stutest.fs
	chmod 755 $(TRANSLATOR)
	$(TRANSLATOR) $(OPTIONS) $(TESTFILES) > stutest.fs
	chmod 755 stutest.fs
	gforth stutest.fs

proftest.out: compiler
	touch proftest.out
	chmod 755 $(TRANSLATOR)
