import re
import string

def isOperator(token):
	operators = ['+', '-', '*', '/', '%', '^', 'and', 'or', 'not', 'iff']
	return token in operators

def isBoolean(token):
	bools = ['true', 'false']
	return token in bools

def isInteger(token):
	regex = re.compile("^[1-9]\d*$")
	return regex.match(token)

def isReal(token):
#TODO: Implement

def isString(token):
	regex = re.compile("^\"\"$")
	return regex.match(token)

def isType(token):
	types = ['bool', 'int', 'real', 'string']
	return token in types

def isStatement(token):
	statements = ['println', 'if', 'while', 'let', 'assign']
	return token in statements
