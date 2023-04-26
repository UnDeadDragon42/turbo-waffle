import rooms

class Player():
	def __init__(self):
		self.__location = rooms.outside.name

	def __str__(self):
		return self.__location

	@property
	def location(self):
		return self.__location
	def location(self, new):
		self.__location = new

	#moves the player to different rooms
	def MovePlayer(self, direction):
		for c in rooms.totalRooms:
			if self.__location == c.name:
				if direction in c.directions:
					print(c.directions[0])






#	print(curLocat)
#	print(rooms.outside)
#	l = rooms.curLocat
#	avalibleMoves = l.directions
#	#print(avalibleMoves)
#	if curLocat in rooms.totalRooms:
#		print("AND I")
#		avalibleMoves = rooms.outside.directions
#		if direction in avalibleMoves:
#			print("You made it")