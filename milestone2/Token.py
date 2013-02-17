class Token():
    def __init__(self, t_Type, t_Word):
        self.Type = t_Type
        self.Word = t_Word
    def __str__(self):
        return "< " + self.Type + " , " + self.Word + " >"
    def __repr__(self):
        return self.__str__(self)
