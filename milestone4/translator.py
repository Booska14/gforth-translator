#!/usr/bin/python
import sys
import string
import parser
import tokenizer
from options import *
from translatorExceptions import *
import buildTree
import treeTraversal
from node import *

user_options = []
files = []
symbolTable = {}
syntaxList = []
#Used to construct the parse tree
stack = []

def main(argv):
    parseInput(argv)
    try:
        symbolTable = tokenizer.tokenize(files, user_options)
        parser.parse(files, user_options, symbolTable)
        for file in files:
            tree = buildTree.createTree(parser.fileToString(file))
            print "\\ gforth code for file: " + file
            treeTraversal.printTreeTraversal(tree)
            print ""
    except TokenizerException as e:
        exit(0)
    except ParserException as e:
        exit(0)

    #print "y'all code is translated"
    print "bye"


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
    if len(files) == 0:
        print "no files to parse"
        exit(0)

if __name__ == "__main__":
    main(sys.argv)
