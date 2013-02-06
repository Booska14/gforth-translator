import TokenClass

class symbolTable(object):
    def __init__(self):
        self.dict = {}


    def add(self, token):
        self.dict[token.Word] = token

    def getByWord(self, word):
        return dict[word]
