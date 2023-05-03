import rooms

class Player():
	def __init__(self):
		self.__location = rooms.outside.name
		self.inventory = []

	def __str__(self):
		return self.__location
	
	def PrintInventory(self):
		word = ""
		for i in range(0, len(self.inventory)):
			word += self.inventory[i]
		if word == "":
			word = "Your bag is empty"
		return word

	#here is getter and setter for player location
	#although I dont think I need it
	@property
	def location(self):
		return self.__location
	def location(self, new):
		self.__location = new

	#moves the player to different rooms by checking there location and the open directions
	def MovePlayer(self, direction):
		numb = 0
		found = False
		for c in rooms.totalRooms:
			if self.__location == c.name and found == False:
				currList = c.directions
				blockedList = c.blockedDirections
				if direction in c.directions:
					for i in currList:
						if direction == i:
							try:
								if currList[numb] not in blockedList:
									if currList[numb] in ("N", "E", "S", "W"):
										numb += 1
									print(f"Moved from {self.__location} to {currList[numb]}")
									self.__location = currList[numb]
									#This is just to describe the new room
									for wah in rooms.totalRooms:
										if self.__location == wah.name:
											roomDe = list(wah.roomdescriptions)
											print(f"{roomDe[0]}")
									found = True
								else:
									print("There might be a way though but not right now")
							except IndexError:
								print(f"You mest up with the location code")
								print(f"currently accesing {numb} from {currList} of a length of {len(currList) - 1}")
						numb += 1
				else:
					print(f"You can't go that way from here.")
		

	#This is the code that changes the players inventory, out and in
	#The first part is the use which uses an object from the palyers inventory
	#and the second is search
	def ChangeInventory(self, dir):
		used = False
		for c in rooms.totalRooms:
			if self.__location == c.name:
				needList = c.needed
				if dir == 1: #use
					for i in self.inventory:
						if i in needList:
							needList.remove(i)
							c.blockedDirections = ["none"]
							self.inventory.remove(i)
							print(f"You used {i}")
							used = True
							#this is the speical case for the observertory room,
							#As a lever is pulled in this room that affects another
							if self.__location == "observertory":
								self.inventory.append("Part of a lever")
								rooms.waterR.blockedDirections.remove("N")
					if used == False:
						print("You don't have anything that would be of use here")
				elif dir == 2: #search
					if len(c.objects) > 0:
						for i in c.objects:
							c.objects.remove(i)
							self.inventory.append(i)
						print(f"You pciked up {i}")
						print(f"{i}: {c.objectDesriptions}")
					else:
						print("There isn't anything of use here")

