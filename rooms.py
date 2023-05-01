totalRooms = []
playersLokation = "outside"

class Rooms():
	def __init__(self, name = 'room', number = 0):
		self.__name = name
		self.number = number
		self.directions = {}
		self.blockedDirections = []
		self.needed = []
		self.objects = []
		self.objectDesriptions = []
		self.roomdescriptions = {}
		self.hints = []
		self.use = []
		
	@property
	def name(self):
		return self.__name

outside = Rooms("outside", 1)
outside.directions = {"N", "main hall"}
outside.blockedDirections = ["N"]
outside.needed = ["key"]
outside.objects = "key"
outside.objectDesriptions = "Rusty circular key, it looks like it has been covered up for a very long time"
outside.roomdescriptions = {"You stand befor the tome of King Movieses. In front of you stands a door with an oddly shapped key hole, with the entrance steps covered in sand.", "You stand befor the tome of King Movieses, the door way now uncovered. The door is open now leading into darkness that has not been seen for centruies"}
outside.hints = ["I wonder where the key could be?", "There is a lot of sand", "If only I could move it out of the way."]
outside.use = "You dig around the steps through the sand and find a key"
totalRooms.append(outside)

mainHall = Rooms("main hall", 2)
mainHall.directions = {"E", "dinning hall", "S", "outside", "W", "wating room"}
mainHall.roomdescriptions = {'''You stand in the main hall of the tomb. From here there are two brantching paths going East and West. 
Looking around the room you see the hall leading East having signs depicting feasts and to the West signs depicting a checking area'''}
mainHall.objects = "There is nothing of note in this room"
mainHall.objectDesriptions = "Cool breez"
mainHall.hints = ["I think more could be found in the checking area"]
mainHall.use = "You sit on one of the chairs in the room. It is nice to take a break"
totalRooms.append(mainHall)

watingR = Rooms("wating room", 3)
watingR.directions = {"N", "water room", "S", "main hall"}
watingR.roomdescriptions = {"You stand in a room split in two from your side to the other side, blocked by a booth and a gate. The gate is open, and there is no door on the other side"}
watingR.objects = 'hammer'
watingR.objectDesriptions = "The hammer is big enough that you therioz that it was used for demolition"
watingR.use = "You look around the room for something of use, behind the counter you find an old hammer. Properbly confinscated a long time ago"

totalRooms.append(watingR)

dinnH = Rooms("dinning hall", 4)
dinnH.directions = {"N", "observertory", "S", "hidden room", "W", "main hall"}
dinnH.blockedDirections = ["S"]
dinnH.needed = ["hammer"]
dinnH.roomdescriptions = {"You stand in a large room decotracted with long tables and broken chairs. After a long look you can tell that the walls used to be bueatufly decrated, but they have fadded with time along with some of the walls as well that have now showen bear brick"}
dinnH.objects = "Nothing of value is in this room"
dinnH.objectDesriptions = "The breez dosen't reach hear"
dinnH.hints = ["One of the walls looks like it needs a breez to knock it down", "or a hammer"]
dinnH.use = "Looking at one of the walls you see that it leads to another room, so you use the hammer to knock down the wall opeing up another room."
totalRooms.append(dinnH)

hiddenR = Rooms("hidden room", 5)
hiddenR.directions = {"N", "dinning hall"}
hiddenR.roomdescriptions = {"This room is quite small and dosen't have much in it except what appers to be part of a lever"}
hiddenR.objects = ["Part of a lever", "Used part of a lever"]
hiddenR.objectDesriptions = "The object is a metal rod with a handel on top, holes in the bottom of it looks like it needs to be instreded in something"
hiddenR.use = "You grab what looks like the top part of a lever"
hiddenR.hints = ["If nothing else the level part will look good on your mantal"]
totalRooms.append(hiddenR)

obserR = Rooms("observertory", 6)
obserR.directions = {"S", "dinning hall"}
obserR.roomdescriptions = {"You stand on a platform that is inside a glass ball. Looking around the room the ball is in shows a huge cave that has a water fall flowing into a big lake with a rasied bridge. In the room you see a botom part of where you would expect a lever to go", "Still in the glass ball looking out to the water fall and river, you see a path across the lowered bridge"}
obserR.use = "You attach the lever to the other part on the ground. Afterward you give it a pull and see the brige in the room with the river lower, providing a way to the other side."

totalRooms.append(obserR)

waterR = Rooms("water room", 7)
waterR.directions = {"N", "tomb", "S", "wating room"}
waterR.blockedDirections = ["N"]
waterR.needed = ["Used part of a lever"]
waterR.roomdescriptions = {"You are in a large open room, that looks like it was built into a cave. Looking around you see a huge water fall feed into a rapidly flowing river that goes under the moutian this place was built into. The only way across is a bridge that is currently rasied.", "You are in a large open room, that looks like it was built into a cave. Looking around you see a huge water fall feed into a rapidly flowing river that goes under the moutian this place was built into. The bridge is lowered you can now go across into the most interectly carved door you have come across."}
waterR.hints = ["There must be a way to lower that bridge."]
totalRooms.append(waterR)

tomb = Rooms("tomb", 8)
totalRooms.append(tomb)
