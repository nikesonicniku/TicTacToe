import os
os.system('clear')
print ("Welcome To Tic Tac Toe Game >")
class board():
	#CREATING CELLS!
	def __init__(self):
		self.cells=[" "," "," "," "," "," "," "," "," "," "]


	#Functin To Display Board
	def display(self):
		print(" %s || %s || %s "%(self.cells[1],self.cells[2],self.cells[3]))
		print("=============")
		print(" %s || %s || %s "%(self.cells[4],self.cells[5],self.cells[6]))
		print("=============")
		print(" %s || %s || %s "%(self.cells[7],self.cells[8],self.cells[9]))
	

	#Function To Refresh Screen
	def refresh(self):
		os.system('clear')
		print ("Welcome To Tic Tac Toe Game >")
		self.display()


	#Function To Play The Turn
	def play(self,cell_no,player):
		if self.cells[cell_no]==" ":
			self.cells[cell_no]=player
		else:
			cell_no=int(raw_input("Invalid Input! Try Again.\n"))
			self.play(cell_no,player)


	#Function To Check The Winning State.
	def won(self,player):
		if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
			return True
		if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
			return True
		if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
			return True
		if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
			return True
		if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
			return True
		if self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
			return True
		if self.cells[5]==player and self.cells[2]==player and self.cells[8]==player:
			return True
		if self.cells[9]==player and self.cells[6]==player and self.cells[3]==player:
			return True
		
	#Function For Resetting The Game!
	def reset(self):
		self.cells=[" "," "," "," "," "," "," "," "," "," "]


	#Function To Check Tie
	def tie(self):
		full=0
		for i in self.cells:
			if i!=" ":
				full+=1
		if full==9:
			return True

#Calling Class
j=board()
j.display()
xwon=0
owon=0
ties=0
while  True:
	#Taking Turn of X!
	x=int(raw_input("\nX) Choose A Number B/W 1-9 >\n"))
	j.play(x,"X")
	j.refresh()
	if j.won("X"):
		print ("\nX Won The Game")
		xwon+=1
		end=raw_input("Do You Want To Continue? Y/N\n")
		if end=="y" or end=="Y":
			j.reset()
			continue
		else:
			print("Thank You For Playing!")
			print "X won:",xwon," Times"
			print "O won:",owon," Times"
			print "Ties: ",ties," Times"
			break

	#Check Tie Condition!
	if j.tie():
		print("It Was A Tie!")
		ties+=1
		end=raw_input("Do You Want To Continue? Y/N\n")
		if end=="y" or end=="Y":
			j.reset()
			continue		
		else:
			print("Thank You For Playing!")
			print "X won:",xwon," Times"
			print "O won:",owon," Times"
			print "Ties: ",ties," Times"
			break

	#Taking Turn of O!
	o=int(raw_input("\nO) Choose A Number B/W 1-9 >\n"))
	j.play(o,"O")
	j.refresh()
	if j.won("O"):
		print ("\nO Won The Game")
		owon+=1
		end=raw_input("Do You Want To Continue? Y/N\n")
		if end=="y" or end=="Y":
			j.reset()
			continue
		else:
			print("Thank You For Playing!")
			print "X won:",xwon," Times"
			print "O won:",owon," Times"
			print "Ties: ",ties," Times"
			break