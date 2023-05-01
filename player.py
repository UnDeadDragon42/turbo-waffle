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
		numb = -1
		for c in rooms.totalRooms:
			if self.__location == c.name:
				if direction in c.directions:
					currList = list(c.directions)
					for i in currList:
						numb += 1
						print(f"{numb} this is numb")
						if direction == i:
							print(f"{numb} this is numb 2")
							try:
								print(f"From {self.__location} to {currList[1]}")
								self.__location = currList[numb]
							except IndexError:
								print(f"You mest up with the location code")







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