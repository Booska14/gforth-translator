#!/usr/bin/python
import sys
import string
import 

options = []
files = []
symbolTable = {}
syntax = []


def main(argv):
	parseInput(argv)
	symbolTable = tokenizer.tokenize(files, options)
	syntax = parser.parse(files, options, symbolTable)
	
	printInfo()

def parseInput(argv):
	for i in range(1, len(argv) - 1): 				
		if argv[i][0] == '-':
			options.append(comArg)
		else:
			files.append(comArg)

def printInfo():
	print "Syntax list"
	print syntaxList

if __name__ == "__main__":
	main(sys.argv)
