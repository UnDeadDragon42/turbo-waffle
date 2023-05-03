import intoSeqence
import userActions
import player
import rooms

userIn = ""
quit = ("quit", "q")
intoSeqence.main()
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
	elif userIn == "map":
		print(user)
	elif userIn in ("i", "inventory"):
		a = user.PrintInventory()
		print(a)
	elif userIn != 'quit':
		print("Type 'help' for list of commands")


