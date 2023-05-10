import userActions
import player
import shelve
import rooms


#Need to fix
#	Intro
#	Hints maeby
#	Can't get past the obseveretroy
#	Game too short
#		Might add hide mechanic
#	Add save and load
print('''\nFinaly after all this time, after all the deception, trickery, and wrong moves you are here. 
King Movieses tomb
In front of you stands a large stone door without any handles just a hole on the right door. 
The steps in front of the door is covered in sand.''')
      
	
userIn = ""
quit = ("quit", "q")
actions = ('''
	quit/q - Quit out of the game
	save/sa - saves the game
	load/l - loads last save file
	search/s - searches room for items and gets the object 
	use/u - uses iteam in inventorty
	hint/h - gives hint in room
	map/m - gives your location
''')

#This is the function to save the game
def save():
	s = shelve.open('game.bin')
	s["location"] = user.GetLocation()
	s["inventory"] = user.GetInventory()
	s["outsideStuff"] = rooms.outside
	s["mainHall"] = rooms.mainHall
	s["watingR"] = rooms.watingR
	s["dinnH"] = rooms.dinnH
	s["hiddenR"] = rooms.hiddenR
	s["obserR"] = rooms.obserR
	s["waterR"] = rooms.waterR
	s["tomb"] = rooms.tomb
	s.sync()
	s.close()

#This is the function to load the game
def load():
	s = shelve.open('game.bin')
	user.location(s["location"])
	user.SetInventorty(s["inventory"])
	rooms.outside = s["outsideStuff"]
	rooms.mainHall = s["mainHall"]
	rooms.watingR = s["watingR"]
	rooms.dinnH = s["dinnH"]
	rooms.hiddenR = s["hiddenR"]
	rooms.obserR = s["obserR"]
	rooms.waterR = s["waterR"]
	rooms.tomb = s["tomb"]
	s.close()

user = player.Player()

def EndGame():
	print(f'''After truding through the long forgotten tomb, 
	you finally reach it: The Final Resting Place of King Movieses. 
	You scan the room it is by far the most wonderfully decorated room in the tomb. 
	It was obvous that it was once a throne room, along with this tomb used to be a castel. 
	Sitting on the old throne chair was hte sarcofigus of King Movieses. 
	As you move closer to the sarcofoges the throuch you were holding dimmed, 
	the door to the room slide shut. 
	Finally you hear a voice from the sarcofogus, 'What is your quarry?' ''')

while userIn not in quit:
	userIn = input("What do you do?\n")
	if userIn == "help":
		userActions.printActions()
	elif userIn in ("search", "s"):
		user.ChangeInventory(2)
	elif userIn in ("u", "use"):
		user.ChangeInventory(1)
	elif userIn == "move":
		direction = input("What direction? (N, E, S, W)\n")
		user.MovePlayer(direction)
		if user.GetLocation() == "tomb":
			print("DONE")
	elif userIn == "map":
		print(user)
	elif userIn in ("i", "inventory"):
		a = user.PrintInventory()
		print(a)
	elif userIn == "Admin":
		cd = input("Enter command\n")
		if cd == "tp":
			goal = input("Which room?\n")
		else:
			goal = 'na'
		user.Admin(cd, goal)
	elif userIn in ('save'):
		save()
	elif userIn in ("l", "load"):
		load()
	elif userIn != 'quit':
		print("Type 'help' for list of commands")
	else:
		print("Command unknonw try again.")

EndGame()
#def load():
#	name = input("Enter customer's name:\n")
#	try:
#		s = shelve.open('carts.bin')
#		cart = s[name]
#		s.close()
#		return cart
#	except:
#		return


