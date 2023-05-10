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

user = player.Player()



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
		#print(f"Players location {user.location}")
		if user.location == "tomb":
			print("DONE")
	elif userIn == "map":
		print(user)
		print(f"As comapered to {user.GetLocation()}")
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
		s = shelve.open('game.bin')
		s["location"] = user.GetLocation()
		s["inventory"] = user.GetInventory()
		s["outsideStuff"] = rooms.outside
		s["mainHall"] = rooms.mainHall
		s["watingR"] = rooms.watingR
		s["dinnH"] = rooms.dinnH
		s["hiddenR"] = rooms.outside
		s["obserR"] = rooms.obserR
		s["waterR"] = rooms.waterR
		s["tomb"] = rooms.tomb
		s.sync()
		s.close()
		print(f"The outside location has {rooms.outside.needed}")
		print(f"You saved with {user.GetInventory()} at {user.GetLocation()}")
	elif userIn in ("l", "load"):
		s = shelve.open('game.bin')
		user.location = s["location"]
		s.close()
	elif userIn != 'quit':
		print("Type 'help' for list of commands")

#def save(cart):
#	s = shelve.open('carts.bin')
#	s[cart.name] = cart
#	s.sync()
#	s.close()
#
#def load():
#	name = input("Enter customer's name:\n")
#	try:
#		s = shelve.open('carts.bin')
#		cart = s[name]
#		s.close()
#		return cart
#	except:
#		return


