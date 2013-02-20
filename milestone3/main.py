#!/usr/bin/python
import sys
import string
import parser
import tokenizer
from options import *

user_options = []
files = []
symbolTable = {}
syntaxList = []


def main(argv):
    parseInput(argv)
    symbolTable = tokenizer.tokenize(files, user_options)
    parser.parse(files, user_options, symbolTable)
    print "Done"

def parseInput(argv):
    for i in range(1, len(argv)):
        comArg = argv[i]
        if comArg[0] == '-':
            if comArg not in optionList:
                print comArg + "is an illegal option, use `--help` to see a list of options"
            elif comArg == optionhelp:
                print "usage:"
                print argv[0] + " [options] files"
                print "options: "
                for option in sorted(optionList.iterkeys()):
                    print "  " + option + "   :   " + optionList[option]
                exit(0)
            else:
                user_options.append(comArg)
        else:
            files.append(comArg)

def printInfo():
    print "Syntax list"
    print syntaxList

if __name__ == "__main__":
    main(sys.argv)
