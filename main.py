import intoSeqence
import userActions
#def main():
#print("HERE WE ARE")
intoSeqence.main()
actions = ('''
	quit/q - Quit out of the game
	load/l - loads last save file
	search/s - searches room for items and gets the object 
	use/u - uses iteam in inventorty
	hint/h - gives hint in room
	map/m - lists rooms you have visted with there avalible movments
''')
userIn = input("What do you do?\n")

if userIn == "help":
	userActions.printActions()
elif userIn == "search":
	#need to add in if in this or that room
	print("You found a key after digging in the sand")
else:
	print("Type 'help' for list of commands")
