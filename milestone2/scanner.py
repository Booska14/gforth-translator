import symbolTable
import Token

#+ 1 2

# word1 = Token("Operator","+")
# wordList.add(word1)
# dic[word1.word] = word1
#dic[1] = {["+", word1], ["Integer", "1"], ["Integer", "1"]}

def getToken(word):
	if isOperator(word):
		return(t = Token("Operator", word))
	if isBoolean(word):
		return(t = Token("Boolean", word))
	if isInteger(word):
		return(t = Token("Integer", word))
	if isReal(word):
		return(t = Token("Boolean", word))
	if isString(word):
		return(t = Token("String", word))
	if isType(word):
		return(t = Token("String", word))
	if isStatement(word):
		return(t = Token("String", word))
	#TODO: Might have to worry about tab characters
	
	
		
def isComment(line):
	regex = "^//"
	return regex.match(word)

def isOperator(word):
	operators = ['+', '-', '*', '/', '%', '^', 'and', 'or', 'not', 'iff']
	return word in operators

def isBoolean(word):
	bools = ['true', 'false']
	return word in bools

def isInteger(word):
	regex = re.compile("^((-?[1-9]\d*)|0)$")
	return regex.match(word)

def isReal(word):
	regex = re.compile("^[1-9]\d*[.]$")
	return regex.match(word)

def isString(word):
	regex = re.compile("^\"\"$")
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
