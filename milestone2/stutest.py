#!/usr/bin/python
import re
import string
import scanner
import symbolTable
import sys
import shlex
import Token

symbol_table = []
def parseFile(fileName):
    source_file = open(fileName, 'r')
    line_number = 1
    for line in source_file:
        lexeme_number = 1
        if scanner.isComment(line):
            continue
        words = parseWords(line)
        for word in words:
            t = (scanner.getToken(word))
            if t is not None:
                symbol_table.append(t)
                lexeme_number += 1
        line_number += 1
    for entry in symbol_table:
        print(entry)

def parseWords(line):
    line = line.replace("\n", "")
    line = line.replace("\t", " ")
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")
    words = shlex.shlex(line)
    words.wordchars += '.'
    words.wordchars += '-'
    return words

if __name__ == "__main__":
    parseFile(sys.argv[1])
