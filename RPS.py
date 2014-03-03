import sys
import os
import random

print "Choose: rock, paper, scissors"
uChoice = raw_input("> ")

cpuChoice = random.random()
if cpuChoice < 1.0 and cpuChoice > (2.0 / 3.0):
	cpuChoice = 'rock'
elif cpuChoice <= (2.0 / 3.0) and cpuChoice > (1.0 / 3.0):
	cpuChoice = 'paper'
else:
	cpuChoice = 'scissors'

print "The computer chose: %s" % cpuChoice

if uChoice == 'rock':
	if cpuChoice == 'scissors':
		print "Congratz! You win this round."
	elif cpuChoice == 'paper':
		print "You lose. Paper beats rock."
	else:
		print "It's a draw!"
elif uChoice == 'paper':
	if cpuChoice == 'rock':
		print "Congratz! You win this round."
	elif cpuChoice == 'scissors':
		print "You lose. Scissors beat paper."
	else:
		print "It's a draw!"
else:
	if cpuChoice == 'paper':
		print "Congratz! You win this round."
	elif cpuChoice == 'rock':
		print "You lose. Rock beats scissors."
	else:
		print "It's a draw!"

print "Press RETURN to continue"
raw_input()

rProgram = raw_input("Do you want to play again? (Y/n) ")
if rProgram == 'Y' or rProgram == 'y':
	def restart_program():
		python = sys.executable
		os.execl(python, python, * sys.argv)
		
	restart_program()
elif rProgram == 'n' or rProgram == 'N':
	print "OK. Hope you had fun!"
	raw_input()
else:
	print "Please type 'Y' or 'n' next time."
	raw_input()
	
