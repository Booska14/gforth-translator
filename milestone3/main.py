#!/usr/bin/python
import sys
import string
import parser
import tokenizer
from options import *

options = []
files = []
symbolTable = {}
syntaxList = []


def main(argv):
    parseInput(argv)
    symbolTable = tokenizer.tokenize(files, options)
    syntax = parser.parse(files, options, symbolTable)
    printInfo()

def parseInput(argv):
    for i in range(1, len(argv)):
        comArg = argv[i]
        if comArg[0] == '-':
            if comArg not in optionList:
                print comArg + "is an illegal option, use `--help` to see a list of options"
            else:
                options.append(comArg)
        else:
            files.append(comArg)

def printInfo():
    print "Syntax list"
    print syntaxList

if __name__ == "__main__":
    main(sys.argv)
