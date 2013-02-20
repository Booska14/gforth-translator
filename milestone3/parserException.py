class ParserException(Exception):
    def __init__(self, value, character = 0):
        self.value = value
        self.character = character

    def __str__(self):
        return repr(self.value)
