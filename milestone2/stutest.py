#!/usr/bin/python
import re
import string
import scanner
import symbolTable
import sys
import shlex

symbol_table = []
def parseFile(fileName):
	source_file = open(fileName, 'r')
	line_number = 1
	for line in source_file:
		line = line.replace("\n", "")
		line = line.replace("\t", " ")
		if scanner.isComment(line):
			continue
		#tokens = string.split(line, ' ')
		tokens = shlex.shlex(line)
		tokens.wordchars += '.'
		tokens.wordchars += '-'
		for token in tokens:
			t = (scanner.getToken(token))
			symbol_table.append(t)
		line_number += 1
	for entry in symbol_table:
		print(entry)
	

if __name__ == "__main__":
	parseFile(sys.argv[1])
