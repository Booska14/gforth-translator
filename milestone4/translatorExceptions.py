class ParserException(Exception):
    def __init__(self, value, character = 0):
        self.value = value
        self.character = character

    def __str__(self):
        return repr(self.value)


class TokenizerException(Exception):
    def __init__(self, lexeme, line, lineNumber):
        self.lexeme = lexeme
        self.line = line
        self.lineNumber = lineNumber

    def __str__(self):
        print self.lexeme + " is not a token"
        print self.line
        print "line # " + str(self.lineNumber)
        return ""
