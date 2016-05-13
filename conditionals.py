import math
import random

#The Red Queen's dragon is trapped in a cage waiting for the day to kill Alice, who is supposed to bring the White Queen back in charge of Wonderland. You are ALice and preparing for the day when you can finally bring peace to Wonderland. You have 5 objects to choose from for the weapons you can use to kill the dragon. 
#I have shown the strength of each weapon you can choose from. The scale is on a 1-10 rating of each weapon. As demonstrated below, the sword is the best choice. 
#I have shown the different kinds of attacks that you should look out for from the dragon. The moves the dragon uses on you is on a scale from 1-10.
#If Alice has a good amount of energy, a strong dominant arm, and you are in a good spot to beat the dragon. You have to have a good stance, meaning good leg positions. 
 
print "Hint: The dragon you are about to fight against can beat left handed people!" 

def main(): 
	ready = raw_input("Are you ready?: no or yes ")
	area = raw_input("Where are you?: ")  
	output = """
Don't be scared! You better get your act together and get some confidence to beat this dragon!...

You are in the {}! You can't be anywhere else than the forest! 

Oh my goodness! You have eaten {} items this morning!...
Remember that you need to have a lot of energy before you fight this dragon! 

If you haven't eaten enough, then go get some food before you fight this dragon! You need to try your best to win! 
""".format(area)
 	print output

	energy = int(raw_input("How many items of food did you eat this morning?: "))
	enough(energy)
	hair = raw_input("What condition is your hair in?: behind your ears, out of your face: ") 
	your(hair)
	

	weapon = raw_input("What weapon would you like?: torch, stick, whip, bowling ball, sword: ")
	yourdecision(weapon) 

	move = raw_input("What is the move that the dragon has chosen to use?: breathing fire, breaths out bad breath, steps on your toes, whips tail, or grabs you: ")
	dragonattacks(move)

	clothes, waterbottle = raw_input("Do you have thin clothes on and more than one waterbottle?: yes or no: ")
	howmuch(clothes, waterbottle) 

	hair = raw_input("Is your hair behind your ears?: yes or no: ") 
	your(hair)

	lowerbody = raw_input("What position is your lower body in right now?: wide legs or feet together: ") 
	strengthof(lowerbody)
	upperbody = raw_input("HURRY! THIS IS YOUR LAST SHOT! This is the most important question that you have to answer. If you choose the correct answer you are going to win. But if you choose the wrong answer...I'm sorry, go yell at your Momma! Here it is...What is your dominant hand?: left handed or right handed: ")
	strengthof(upperbody)
#or, >, ==, and, 
def enough(energy):
	if energy > int("0"):
		print "Yay! You have had enough food! Way to go! NEXT..."

def your(hair):
	if hair == "behind your ears" or hair == "out of your face"  :
		print "Yay! You have your hair out of your face or behind your ears. Either way you are on the right track. NEXT..."


def yourdecision(weapon): 
	
	if weapon == "torch": 
		print "You are going to lose this battle! But if you choose the next move that your dragon makes correctly...you still have a chance!"
		strength = 0 
	elif weapon == "stick":
		print "You are going to get injured! But if you choose the next move that your dragon makes correctly...you still have a chance!"
		strength = 3 
	elif weapon == "whip":
		print "You can stike the dragon only a few times. But if you choose the next move that your dragon makes correctly...you still have a chance!" 
		strength = 6
	elif weapon == "bowling ball":
		print "You are going to do pretty well! If you try hard enough...you might win! YAY!" 
		strength = 8 
	elif weapon == "sword":
		print "You've got this, Alice! You are capable of beating this dragon! I believe in you!"  
		strength = 10 
	else:
		strength = random.randint(0,10) 
	return strength * random.random()
#random = random float from 0-1 

def dragonattacks(move):

	if move == "breathing fire":
		print "You are going to lose to this dragon! You still have a chance if you answer the next five questions correctly!"
		enemystrength = 10
	elif move == "breaths out bad breath": 
		print "You have a chance to beat this dragon! GO GO GO!"
		enemystrength = 3 
	elif move == "steps on your toes":
		print "You could lose... You still have a chance if you answer the next five questions correctly!"
		enemystrength = 7
	elif move == "whips tail":
		print "The dragon is probably going to beat you.. You still have a chance if you answer the next five questions correctly! But don't get your hopes up high because you have a fierce competitor! :("
		enemystrength = 8
	elif move == "grabs you": 
		print "Oh no! The dragon has caught you! You are probably going to die most likely! Hurry do something! You still have a chance if you answer the next five questions correctly!"
		enemystrength = 9 
	else:
		enemystrength = random.randint(0,10) 
	return enemystrength * random.random()

#logical operaters/2 Alternative Executrion

def howmuch(clothes, waterbottle):
	if clothes == "thin" and waterbottle > "one":
		print "PERFECT! You have thin clothes and more than one water bottle! YAYY! We are moving on to the next question..."  
	else:
		print "NOOO!!! Your clothes can't be any thicker and you should have more than one water bottle! Don't worry you have a few more questions to answer! GO GO GO!"
 
def strengthof(lowerbody):
	if lowerbody == "wide legs": 
		print "You are strong enough to fight this dragon."
	else:
		print "You are too weak to fight this dragon. HURRY YOU MUST TELL ME WHAT YOUR UPPER BODY IS LIKE BEFORE I TELL YOU IF YOU WON OR LOST TO THIS DRAGON!" 

def strengthof(upperbody):
	if upperbody == "left handed":
		print "You LOST!!! The dragon beat you! I am disapointed in you! You didn't read or you forgot the hint that I have you at the start of this game!" 
	elif upperbody == "right handed":
		print "CONGRATULATIONS!!! YOU HAVE BEATEN THE DRAGON! Thank your Momma for coming out as a right handed person!"

main()
