totalRooms = []
playersLokation = "outside"

class Rooms():
	def __init__(self, name = 'room', number = 0):
		self.__name = name
		self.number = number
		self.directions = {}
		self.objects = []
		self.objectDesriptions = []
		self.roomdescriptions = {}
		self.hints = []
		
	@property
	def name(self):
		return self.__name

outside = Rooms("outside", 1)
outside.directions = {"N"}
outside.objects = "key"
outside.objectDesriptions = "Rusty circular key, it looks like it has been covered up for a very long time"
outside.roomdescriptions = {"You stand befor the tome of King Movieses. In front of you stands a door with an oddly shapped key hole, with the entrance steps covered in sand.", "You stand befor the tome of King Movieses, the door way now uncovered. The door is open now leading into darkness that has not been seen for centruies"}
outside.hints = ["I wonder where the key could be?", "There is a lot of sand", "If only I could move it out of the way."]
totalRooms.append(outside)

mainHall = Rooms("main hall", 2)
mainHall.directions = {"E", "S", "W"}
mainHall.roomdescriptions = {"You stand in the main hall of the tomb. From here WRITE THE DIRECTIONS"}
totalRooms.append(mainHall)

watingR = Rooms("wating room", 3)
watingR.directions = {"N", "S"}
totalRooms.append(watingR)

dinnH = Rooms("dinning hall", 4)
dinnH.directions = {"N", "E", "S"}
totalRooms.append(dinnH)

hiddenR = Rooms("hidden room", 5)
hiddenR.directions = {"N"}
totalRooms.append(hiddenR)

obserR = Rooms("observertory", 6)
totalRooms.append(obserR)

waterR = Rooms("water room", 7)
totalRooms.append(waterR)

tomb = Rooms("tomb", 8)
totalRooms.append(tomb)
