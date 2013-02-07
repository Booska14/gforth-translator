import TokenClass
import re
import string
import Type

def getToken(word):
    if isOperator(word):
        t = TokenClass.Token("Operator", word)
        return t
    if isBoolean(word):
        t = TokenClass.Token("Boolean", word)
        return t
    if isInteger(word):
        t = TokenClass.Token("Integer", word)
        return t
    if isReal(word):
        t = TokenClass.Token("Real", word)
        return t
    if isString(word):
        word = word.replace('"', '')
        t = TokenClass.Token("String", word)
        return t
    if isType(word):
        t = TokenClass.Token("Type", word)
        return t
    if isStatement(word):
        t = TokenClass.Token("Statement", word)
        return t
    if isLeftParen(word):
        t = TokenClass.Token("LeftParen", word)
        return t
    if isRightParen(word):
        t = TokenClass.Token("RightParen", word)
        return t
    if isIdentifier(word):
        t = TokenClass.Token("Identifier", word)
        return t
    return None

def isComment(line):
    regex = re.compile("^//")
    return regex.match(line)

def isLeftParen(word):
    return word == '('

def isRightParen(word):
    return word == ')'

def isOperator(word):
    #TODO: Should math functions be in here?
    operators = ['+', '-', '*', '/', '%', '^', 'and', 'or', 'not', 'iff', '<', '=', 'sin', 'cos', 'tan', 'logn']
    return word in operators

def isBoolean(word):
    bools = ['true', 'false']
    return word in bools

def isInteger(word):
    regex = re.compile("^((-?[1-9]\d*)|0)$")
    return regex.match(word)

def isReal(word):
    #TODO: allow zeroes
    regex = re.compile("^((-?[1-9]\d*)|0)[.]\d+$")
    return regex.match(word)

def isString(word):
    regex = re.compile("^\".*\"$")
    return regex.match(word)

def isType(word):
    types = ['bool', 'int', 'real', 'string']
    return word in types

def isStatement(word):
    statements = ['println', 'if', 'while', 'let', 'assign']
    return word in statements

def isIdentifier(word):
    regex = re.compile("^[a-zA-Z_]+$")
    return regex.match(word)

def isWhitespace(word):
    words = ['\t', '\n']
    return word in words

