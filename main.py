import intoSeqence
import userActions
#def main():
#print("HERE WE ARE")
intoSeqence.main()

userIn = input("What do you do?\n")

if userIn == "help":
	userActions.printActions()
elif userIn == "search":
	#need to add in if in this or that room
	print("You found a key after digging in the sand")
else:
	print("Type 'help' for list of commands")
