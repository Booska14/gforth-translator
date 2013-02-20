#--------------------------------------------
# INSTRUCTION
# Quoted strings are to be filled in by student
#
CCFLAGS = -t
OBJS = "list of obj files"
SOURCE = "list of source files"
RUNFLAGS = "info for runtime flags"
TESTFILES = test1.in test2.in test3.in test4.in test5.in test6.in test7.in test8.in

#$(OBJS): $(SOURCE)
	#$(CCC) $(CCFLAGS) -c $(SOURCE)

#compiler: $(OBJS)
	#$(CCC) $(CCFLAGS) -o compiler $(OBJS)

clean:
	rm -f "stutest.out"

stutest.out:
	chmod 755 main.py
	./main.py -a $(TESTFILES)
	chmod 755 stutest.out
# Notice the next line. The `-' says to ignore the return code. This
# is a way to have multiple tests of errors that cause non-zero return
# codes.
	#cat stutest2.in
	#-compiler stutest2.in > stutest2.out
	#cat stutest2.out

proftest.out: compiler
	cat $(PROFTEST)
	compiler $(PROFTEST) > proftest.out
	cat proftest.out
