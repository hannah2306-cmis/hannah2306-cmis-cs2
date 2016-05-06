import random

def rounds(numberrounds, c): 
#c = number of rounds you got correct
	if numberrounds == 0: 
		return "You got " + str(c) + "rounds correct." 
	else:
		print "Starting round" + str(numberrounds)
		correct += guess(random.randint(1, 100), 6)
		return rounds(numberrounds - 1, correct)
def guess(random, attempt): 
	input = int(raw_input("Guess a number: "))
	if input == random: 
		print "That's correct!"
		return 1 
	elif attempts == 1: 
		print "The answer was " + str(random) + "You aren't that good at this game"
		return 0
	elif input > random: 
		print "That's too high." 
		return guess(random, attempt -1) 
	elif input < random: 
		print "That's too low."
		return guess(random, attempt -1)  
def main(): 
	result = rounds(1,0) 
	print result
main()
