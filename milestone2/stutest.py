import re
import string
import scanner
import symbolTable

def parseFile(fileName):
	source_file = open(filename, 'r')
	line_number = 1
	for line in source_file:
		line = line.replace("\n", "")
		#print(line)
		if scanner.isComment(line):
			continue
		tokens = string.split(line, ' ')
		for token in tokens:
			t = (scanner.getToken(token))
			prin
		line_number += 1
