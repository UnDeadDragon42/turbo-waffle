import rooms

class Player():
	def __init__(self):
		self.__location = rooms.outside.name
		self.inventory = []

	def __str__(self):
		return self.__location

	#here is getter and setter for player location
	#although I dont think I need it
	@property
	def location(self):
		return self.__location
	def location(self, new):
		self.__location = new

	#moves the player to different rooms by checking there location and the open directions
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

	#This is the code that changes the players inventory, out and in
	#The first part is the use which uses an object from the palyers inventory
	#and the second is search
	def ChangeInventory(self, dir):
		for c in rooms.totalRooms:
			if self.__location == c.name:
				needList = c.needed
				if dir == 1: #use
					for i in self.inventory:
						for x in needList:
							if i == x:
								needList.remove(i)
								c.blockedDirections = ["none"]
								self.inventory.remove(i)
								print(f"You used {i}")
					if needList not in self.inventory:
						print("You don't have anything that would be of use here")
				elif dir == 2: #search
					if len(c.objects) > 0:
						for i in c.objects:
							c.objects.remove(i)
							self.inventory.append(i)
						print(f"You pciked up {i}")
					else:
						print("There isn't anything of use here")




