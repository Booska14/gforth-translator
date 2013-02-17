import symbolTable
import Token
import re
import string

def getToken(word):
	if isOperator(word):
		t = ["Operator", word]
		return t
	if isBoolean(word):
		t = ["Boolean", word]
		return t
	if isInteger(word):
		t = ["Integer", word]
		return t
	if isReal(word):
		t = ["Real", word]
		return t
	if isString(word):
		word = word.replace('"', '')
		t = ["String", word]
		return t
	if isType(word):
		t = ["Type", word]
		return t
	if isStatement(word):
		t = ["Statement", word]
		return t
	if isLeftParen(word):
		t = ["LeftParen", word]
		return t
	if isRightParen(word):
		t = ["RightParen", word]
		return t
			
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

def isWhitespace(word):
	words = ['\t', '\n']
	return word in words
