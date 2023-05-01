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
				currList = list(c.directions)
				blockedList = list(c.blockedDirections)
				if direction in c.directions:
					for i in currList:
						numb += 1
						if direction == i:
							try:
								if currList[numb] not in blockedList:
									print(f"From {self.__location} to {currList[numb]}")
									self.__location = currList[numb]
								else:
									print("There might be a way though but not right now")
							except IndexError:
								print(f"You mest up with the location code")
				else:
					print(f"You can't go that way from here.")
					for i in range(0, len(currList)):
						if i%2 != 0:
							print(f"From here you can go {currList[i]}")







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