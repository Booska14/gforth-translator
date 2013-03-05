#!/usr/bin/python
import sys
import scanner
import shlex
import tokenizer
from translatorExceptions import *
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

def parse(files, user_options, symbol_table):
    """Parses the files using the symbol_table to determine what are atoms

    files -- the files to be parsed
    options -- the options specified by the user
    symbol_table -- the symbol table defined by the tokenizer

    """
    global options
    options = user_options

    global symbolTable
    symbolTable = symbol_table

    for fileName in files:
        print "parsing for file: " + fileName
        file_content = fileToString(fileName, options)
        global inputStack
        inputStack = shlexToList(tokenizer.parseWords(file_content))
        try:
            parseF()
            print "All syntax OK for " + fileName
        except ParserException as e:
            print "message: " + e.value
            print file_content
            printCharacterException(file_content, e.character)
            print "file: " + fileName
            if(optionParseAll not in options):
                raise ParserException("Parsing not correct")

def shlexToList(sList):
    """Takes a shlex object of the tokens and returns them as a list in stack order
    """
    nextToken = sList.read_token()
    newList = []

    while (nextToken != ''):
        newList.insert(0,nextToken)
        nextToken = sList.read_token()
    return newList

def printCharacterException(file_content, character):
    """
    prints the location of the error in the file
    """
    stack = shlexToList(tokenizer.parseWords(file_content))
    stack.reverse()
    stack.insert(character - 1, ">>>>>")
    stack.insert(character + 1, "<<<<<")
    file = " ".join(stack)
    print file

def fileToString(fileName, options):
    """
    takes a file and converts it into a string while replacing newline character with a space. Adds a EOF symbol at the end
    """
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
    """
    Parse the input string starting with the production rule F
    """

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
            raise ParserException("Terminal Symbol reached with no match for: " + currentStack, character)
        else:

            newStackTop = predictiveParseTable[currentStack][terminalType]
            if newStackTop is not None:
                printProduction(currentStack, newStackTop)
                symStack = replaceTopStack(symStack, newStackTop)
            else:
                raise ParserException("ProductionRuleError, the " + str(character) + " '" + currentToken + "' failed production rule for " + currentStack, character)

        currentStack = symStack[-1]

def getNextToken():
    """
    return the next token on the top of the stack
    """

    return inputStack.pop()

def replaceTopStack(stack, newTop):
    """
    pops the top symbol and replaces it with the appropiate production rule. the new stack is then returned
    """

    stack.pop()
    newTop.reverse()
    stack.extend(newTop)
    newTop.reverse()
    return stack

def printProduction(production, ruleList):
    """
    Print out a formatted prodcution rule that was used. only used if the printProductionRules option is used
    """
    if(optionPrintProductionRules in options):
        if len(ruleList) == 0:
             rule = "EPSILON"
        else:
            rule = " ".join(ruleList)
        print production + " -> " + rule

def getTerminalType(token):
    """
    return the Terminal type from the token
    """
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
