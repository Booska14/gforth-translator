class Token:
	def __init__(self, Type, Word):
		self.Type = Type
		self.Word = Word

	def __str__(self):
		print ("< " + self.Type + " , " + self.Word + " >")
	
	def __repr__(self):
		return self.__str__()


