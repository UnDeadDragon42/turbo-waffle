import rooms

class Player():
	def __init__(self):
		self.__location = "outside"

	@property
	def location(self):
		return self.__location
	def location(self, new):
		self.__location = new