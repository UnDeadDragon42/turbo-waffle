rooms = ["outside", "entrance"]
playersLokation = "outside"

class Rooms():
	def __init__(self, name = 'room', number = 0):
		self.name = name
		self.number = number
		self.directions = {}
		self.objects = []
		self.objectDesriptions = []
		self.roomdescriptions = {}
		self.hints = []

outside = Rooms("outside", 1)
outside.directions = "forward"
outside.objects = "key"
outside.objectDesriptions = "Rusty circular key, it looks like it has been covered up for a very long time"
outside.roomdescriptions = {"You stand befor the tome of King Movieses. In front of you stands a door with an oddly shapped key hole, with the entrance steps covered in sand.", "You stand befor the tome of King Movieses, the door way now uncovered. The door is open now leading into darkness that has not been seen for centruies"}
outside.hints = ["I wonder where the key could be?", "There is a lot of sand", "If only I could move it out of the way."]

mainHall = Rooms("main hall", 2)
mainHall.directions = {"east", "backward", "west"}
mainHall.roomdescriptions = {"You stand in the main hall of the tomb. From here WRITE THE DIRECTIONS"}

watingR = Rooms("wating room", 3)
watingR.directions = {"north", "south"}

dinnH = Rooms("dinning hall", 4)
dinnH.directions{"north", "east", "south"}

hiddenR = Rooms("hidden room", 5)
hiddenR.directions("north")

obserR = Rooms("observertory", 6)

waterR = Rooms("water room", 7)

tomb = Rooms("tomb", 8)