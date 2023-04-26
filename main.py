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
	map/m - lists rooms you have visted with there avalible movments
''')

player = player.Player()

def MovePlayer(direction):
	currLocation = player.location
	print(currLocation)
	avalibleMoves = rooms.currLocation.directions
	print(avalibleMoves)

while userIn not in quit:
	userIn = input("What do you do?\n")
	if userIn == "help":
		userActions.printActions()
	elif userIn == "search":
		#need to add in if in this or that room
		print("You found a key after digging in the sand")
	elif userIn == "move":
		direction = input("What direction? (N, E, S, W)")
		MovePlayer(direction)
	elif userIn != 'quit':
		print("Type 'help' for list of commands")
	print(userIn)


