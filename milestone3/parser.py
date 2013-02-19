#!/usr/bin/python
import sys
import scanner
import shlex
import tokenizer

#end of file token
eof = "<endoffile>"

def parse(files, options, symbol_table):
	for fileName in files:
		file_content = fileToString(fileName, options)
		parseF(file_content)

def fileToString(fileName, options):
	file_content = ""
	with open(fileName, 'r') as file:
		for line in file:
			if scanner.isComment(line):
				continue
			else:
				file_content += line.replace('\n', ' ')
	file_content += eof
	
def parseF(file_content):
	

def parseT(file_content):
	 
			
	
