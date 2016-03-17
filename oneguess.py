import random 
import math
from random import randint

def main():
    minimumNumber = raw_input("What is the minimum number?: ") 
    maximumNumber = raw_input("What is the maximum number?: ")
    targetNumber = random.randint(minimumNumber, maximumNumber) 
    output = """ 
I'm think of a number from {} to {}.
""".format(minimumNumber, maximumNumber)
    print output
    guessing = raw_input("What do you think it is?: ")   
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
