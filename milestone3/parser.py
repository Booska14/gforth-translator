#!/usr/bin/python
import sys
import scanner
import shlex
import tokenizer
from parserException import *
from options import *

#end of file token

inputStack = []
symbolTable = {}
options = []

#file constants
EOF = "$"
F = "F"
T = "T"
S = "S"
A = "A"
B = "B"
LEFTPAREN = "("
RIGHTPAREN = ")"
ATOM = "atom"
TerminalTypeList = [LEFTPAREN, RIGHTPAREN, ATOM, EOF]

FTable = dict([(LEFTPAREN, [T,F]), (RIGHTPAREN, None), (ATOM, None), (EOF, [])])
TTable = dict([(LEFTPAREN, [LEFTPAREN,S,RIGHTPAREN]), (RIGHTPAREN, None), (ATOM, None), (EOF, None)])
STable = dict([(LEFTPAREN, [LEFTPAREN,A]), (RIGHTPAREN, None), (ATOM, [ATOM, B]), (EOF, None)])
ATable = dict([(LEFTPAREN, [S,RIGHTPAREN,B]), (RIGHTPAREN, [RIGHTPAREN,B]), (ATOM, [S,RIGHTPAREN,B]), (EOF,None)])
BTable = dict([(LEFTPAREN, [S]), (RIGHTPAREN, []), (ATOM, [S]), (EOF, None)])

predictiveParseTable = dict([(F, FTable), (T, TTable), (S, STable), (A, ATable), (B, BTable)])

def parse(files, options, symbol_table):
    for fileName in files:
        print "parsing for file: " + fileName
        file_content = fileToString(fileName, options)
        global inputStack
        inputStack = shlexToList(tokenizer.parseWords(file_content))
        global symbolTable
        symbolTable = symbol_table
        try:
            parseF()
        except ParserException as e:
            print "message: " + e.value
            print "file: " + fileName
            if(optionParseAll not in options):
                raise ParserException("Parsing not correct")

def shlexToList(sList):
    nextToken = sList.read_token()
    newList = []

    while (nextToken != ''):
        newList.insert(0,nextToken)
        nextToken = sList.read_token()
    return newList

def fileToString(fileName, options):
    file_content = ""
    with open(fileName, 'r') as file:
        for line in file:
            if scanner.isComment(line):
                continue
            else:
                file_content += line.replace('\n', ' ')
    file_content += EOF
    return file_content

def parseF():

    character = 1
    symStack = []
    symStack.append(EOF)
    symStack.append(F)
    currentStack = symStack[-1]
    currentToken = getNextToken()
    terminalType = getTerminalType(currentToken)
    while(currentStack != EOF):
        if currentStack == terminalType:
            symStack.pop()
            currentToken = getNextToken()
            terminalType = getTerminalType(currentToken)
            character += 1
        #if current stack is a terminal symbol
        elif currentStack in TerminalTypeList:
            raise ParserException("Terminal Symbol reached with no match for: " + currentStack)
        else:

            newStackTop = predictiveParseTable[currentStack][terminalType]
            if newStackTop is not None:
                printProduction(currentStack, newStackTop)
                symStack = replaceTopStack(symStack, newStackTop)
            else:
                raise ParserException("ProductionRuleError, the " + str(character) + " '" + currentToken + "' failed production rule for " + currentStack)

        currentStack = symStack[-1]

def getNextToken():
    return inputStack.pop()

def replaceTopStack(stack, newTop):
    stack.pop()
    newTop.reverse()
    stack.extend(newTop)
    newTop.reverse()
    return stack

def printProduction(production, ruleList):
    rule = " ".join(ruleList)
    print production + " -> " + rule

def getTerminalType(token):
    if token == LEFTPAREN:
        return LEFTPAREN
    if token == RIGHTPAREN:
        return RIGHTPAREN
    if token == EOF:
        return EOF
    if token in symbolTable:
        return ATOM
    else:
        raise ParserException("The following token was not accepted by the parser: " + token)
