totalRooms = []
playersLokation = "outside"

#Creats Rooms class that has many different atributes
class Rooms():
	def __init__(self, name = 'room', number = 0):
		self.__name = name
		self.number = number
		self.directions = ["none"]
		self.blockedDirections = ["none"]
		self.needed = ["none"]
		self.objects = ["none"]
		self.objectLoc = ["none"]
		self.use = ["none"]
		self.objectDesriptions = ["none"]
		self.roomdescriptions = {"none"}
		self.hints = ["none"]

	@property
	def name(self):
		return self.__name


#Here are all the created rooms and there specified attributes

outside = Rooms("outside", 1)
outside.directions = ["N", "main hall"]
outside.blockedDirections = ["N"]
outside.needed = ["key"]
outside.objects = ["key"]
outside.objectLoc = ["You dig around the steps through the sand and find a key"]
outside.use = ['''You insert the weird key into the weird lock. Perfect fit. 
After you turn the key the door opens on its own. Now you can enter''']
outside.objectDesriptions = ["Rusty circular key, it looks like it has been covered up for a very long time"]
outside.roomdescriptions = {"You stand befor the tome of King Movieses. To the north, in front of you, stands a door with an oddly shapped key hole, with the entrance steps covered in sand.", "You stand befor the tome of King Movieses, the door way now uncovered. The door is open now leading into darkness that has not been seen for centruies"}

outside.hints = ["I wonder where the key could be?", "There is a lot of sand", "If only I could move it out of the way."]
totalRooms.append(outside)

mainHall = Rooms("main hall", 2)
mainHall.directions = ["E", "dinning hall", "S", "outside", "W", "wating room"]
mainHall.objectLoc = ["There is nothing of note in this room"]
mainHall.use = ["You sit on one of the chairs in the room. It is nice to take a break"]
mainHall.objectDesriptions = ["Cool breez"]
mainHall.roomdescriptions = {'''You stand in the main hall of the tomb. From here there are two brantching paths going East and West. 
Looking around the room you see the hall leading East having signs depicting feasts 
and to the West signs depicting a checking area'''}

mainHall.hints = ["I think more could be found in the checking area"]
totalRooms.append(mainHall)

watingR = Rooms("wating room", 3)
watingR.directions = ["N", "water room", "W", "main hall"]
watingR.objects = ['hammer']
watingR.objectLoc = ['''You look around the room for something of use, behind the counter you find an old hammer. Properbly confinscated a long time ago''']
watingR.objectDesriptions = ["The hammer is big enough that you therioz that it was used for demolition"]
watingR.roomdescriptions = {'''You stand in a room split in two from your side to the other side, blocked by a booth and a gate. 
The gate is open, and there is no door on the other side leading north. 
To the west behind you leads back to the main hall
Hopfully something was left here that can be of use'''}

totalRooms.append(watingR)

dinnH = Rooms("dinning hall", 4)
dinnH.directions = ["N", "observertory", "S", "hidden room", "W", "main hall"]
dinnH.blockedDirections = ["S"]
dinnH.needed = ["hammer"]
dinnH.objects = ["Nothing of value is in this room"]

dinnH.use = ['''Looking at one of the crumbiling walls you see through the bricks that it leads to another room. 
Knowing that there are better things lying ahead, 
you use the hammer to open the way to a hidden room.''']
dinnH.objectDesriptions = ["The breez dosen't reach hear"]
dinnH.roomdescriptions = {'''You stand in a large room decotracted with long tables and broken chairs. 
After a long look you can tell that the walls used to be bueatufly decrated, 
but they have fadded with time along with some of the walls as well. 
One section is particualry woren, to the point that it looks like it could be knocked down
There is another hall way heading nothwards, and the path back heading west'''}

dinnH.hints = ["One of the walls looks like it needs a breez to knock it down", "or a hammer"]
totalRooms.append(dinnH)

hiddenR = Rooms("hidden room", 5)
hiddenR.directions = ["N", "dinning hall"]
hiddenR.roomdescriptions = {'''This room is quite small and dosen't have much in it except what appers to be scrap metal,
 with the only exit back to the dinning hall, north'''}
hiddenR.objects = ["Part of a lever"]
hiddenR.objectLoc = ["In the pile of metal you find one pice that seems to be of use"]
hiddenR.objectDesriptions = ['''The object is a metal rod with a handel on top,
holes in the bottom of it looks like it needs to be instreded in something''']
hiddenR.hints = ["If nothing else the level part will look good on your mantal"]
totalRooms.append(hiddenR)

obserR = Rooms("observertory", 6)
obserR.directions = ["S", "dinning hall"]
obserR.needed = ["Part of a lever"]
obserR.roomdescriptions = {'''You stand on a platform that is inside a glass ball. 
Looking around the room the ball is in shows a huge cave 
that has a water fall flowing into a big lake with a rasied bridge. 
In the room you see a botom part of where you would expect a lever to go.
The only path is the same way in, south to the dinning room'''}
obserR.use = ['''You attach the lever to the other part on the ground. 
Afterward you give it a pull and see the brige in the room bellow lower, 
providing a way to the other side.''']

totalRooms.append(obserR)

waterR = Rooms("water room", 7)
waterR.directions = ["N", "tomb", "S", "wating room"]
waterR.blockedDirections = ["N"]
waterR.needed = ["Used part of a lever"]
waterR.roomdescriptions = {'''You are in a large open room, that looks like it was built into a cave. 
Looking around you see a huge water fall feed into a rapidly flowing river that goes under the moutian this place was built into. 
The only way across is a bridge that is currently rasied. For now all you can do is head back south to the cheacking room''', 
'''You are in a large open room, that looks like it was built into a cave. 
Looking around you see a huge water fall feed into a rapidly flowing river that goes under the moutian this place was built into. 
The bridge is lowered you can now go across into the most interectly carved door you have come across.
You can still go back south, but to the north across the bridinge lies the finall resting place of King Movieses'''}
waterR.hints = ["There must be a way to lower that bridge."]
totalRooms.append(waterR)

tomb = Rooms("tomb", 8)
tomb.directions = ["S", "water room"]
totalRooms.append(tomb)