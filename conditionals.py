import math
import random

#The Red Queen's dragon is trapped in a cage waiting for the day to kill Alice, who is supposed to bring the White Queen back in charge of Wonderland. You are ALice and preparing for the day when you can finally bring peace to Wonderland. You have 5 objects to choose from for the weapons you can use to kill the dragon. 
#I have shown the strength of each weapon you can choose from. The scale is on a 1-10 rating of each weapon. As demonstrated below, the sword is the best choice. 
#I have shown the different kinds of attacks that you should look out for from the dragon. The moves the dragon uses on you is on a scale from 1-10. 

def yourdecision(weapon) 
	
	if weapon == "torch": 
		strength = 0 
	elif weapon == "stick":
		strength = 3 
	elif weapon == "whip":
		strength = 6
	elif weapon == "bowling ball":
		strength = 8 
	elif weapon == "sword": 
		strength = 10 


	return strength * random.random() 
def dragonattacks(move)

	if move == "breathing fire":
		enemystrength = 10
	elif move == "breaths out bad breath": 
		enemystrength = 3 
	elif move == "steps on your toes":
		enemystrength = 7
	elif move == "whips tail":
		enemystrength = 8
	elif move == "grabs you": 
		enemystrength = 9 

	else:
		enemystrength = random.randint(0.10) 
	return strength * random.random()

if yourstrength > enemystrength 
	def main():
    minimumNumber = int(raw_input("What is the minimum number?: ")) 
    maximumNumber = int(raw_input("What is the maximum number?: "))
    targetNumber = random.randint(minimumNumber, maximumNumber) 
    output = """ 
I'm think of a number from {} to {}.
""".format(minimumNumber, maximumNumber)
    print output
    guessing = int(raw_input("What do you think it is?: "))   
    if targetNumber == guessing: 
        print """
The target was {}.
Your guess was {}.
That's right! You're a psychic!
""".format(targetNumber, guessing) 
    elif targetNumber < guessing: 
        difference = guessing - targetNumber 
        print """
The target was {}.
Your guess was {}.
That's under by {}. 
""".format(targetNumber, guessing, difference) 
    elif targetNumber > guessing:
        difference = abs(targetNumber - guessing)
        print """
The target was {}.
Your guess was {}.
That's over by {}.
""".format(targetNumber, guessing, difference) 
main() 
	   
def main(): 

