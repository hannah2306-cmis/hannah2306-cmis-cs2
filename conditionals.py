import math
import random

#The Red Queen's dragon is trapped in a cage waiting for the day to kill Alice, who is supposed to bring the White Queen back in charge of Wonderland. You are ALice and preparing for the day when you can finally bring peace to Wonderland. You have 5 objects to choose from for the weapons you can use to kill the dragon. 
#I have shown the strength of each weapon you can choose from. The scale is on a 1-10 rating of each weapon. As demonstrated below, the sword is the best choice. 
#I have shown the different kinds of attacks that you should look out for from the dragon. The moves the dragon uses on you is on a scale from 1-10.
#If Alice has a good amount of energy, a strong dominant arm, and you are in a good spot to beat the dragon. You have to have a good stance, meaning good leg positions. 
 
print "Hint: The dragon you are about to fight against can beat left handed people!" 

def main(): 
	area = raw_input("Where are you?: ") 
	energy = raw_input("Did you eat enough?: ") 
	weapon = raw_input("What weapon would you like?: torch, stick, whip, bowling ball, sword: ")
	yourdecision(weapon) 
	move = raw_input("What is the move that the dragon has chosen to use?: breathing fire, breaths out bad breath, steps on your toes, whips tail, or grabs you: ")
	dragonattacks(move)
	lowerbody = raw_input("What position is your lower body in right now?: wide legs or feet together: ") 
	strenthof(lowerbody)
	upperbody = raw_input("What is your dominant hand?: left handed or right handed: ")
	strengthof(upperbody)
	output = """
You are in the {}!
Be sure that you are in an area where the dragon would most likely be.
You have eaten {}...
If you haven't eaten enough, then go get some food before you fight this dragon! You need to try your best to win! 
""".format(area, dominantarm, energy)
 	print output  

def yourdecision(weapon): 
	
	if weapon == "torch": 
		print "You are going to lose this battle!"
		strength = 0 
	elif weapon == "stick":
		print "You are going to get injured!"
		strength = 3 
	elif weapon == "whip":
		print "You can stike the dragon only a few times. But he will still beat you!" 
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

def dragonattacks(move):

	if move == "breathing fire":
		print "You are going to lose to this dragon!"
		enemystrength = 10
	elif move == "breaths out bad breath": 
		print "You have a chance to beat this dragon! GO GO GO!"
		enemystrength = 3 
	elif move == "steps on your toes":
		print "You might have a chance to win if you have a good weapon. But if you don't then you are probably going to lose."
		enemystrength = 7
	elif move == "whips tail":
		print "The dragon is probably going to beat you...but if you have chosen a good weapon there might be a chance for you to win! But don't get your hopes up high because you have a fierce competitor! :("
		enemystrength = 8
	elif move == "grabs you": 
		print "Oh no! The dragon has caught you! You are probably going to die most likely! Hurry do something!"
		enemystrength = 9 
	else:
		enemystrength = random.randint(0,10) 
	return strength * random.random()

def strengthof(lowerbody):
	if lowerbody == "wide legs": 
		print "You are strong enough to fight this dragon."
	elif lowerbody == "feet together":
		print "You are too weak to fight this dragon." 

def strengthof(upperbody):
	if upperbody == "left handed":
		print "You are going to lose because the hint before the game started said that the dragon can beat you. You will lose!" 
	elif upperbody == "right handed":
		print "You are going to win! Only if you have chosen the right weapons and everything else correctly! Way to go right handed person! You've got this!" 
main()
