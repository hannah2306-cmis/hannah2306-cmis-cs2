#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 2 == 2 
#b) 5 >= 2 
#c) 8 <= 10 
#
#2) What does 'return' do?
# It returns a value. In other words, it brings it back. 
# Spits out a value. 
#
#
#3) What are 2 ways indentation is important in python code?
#a) If the line is indented then it means it is the end of the function. 
#b) If the line is not indented we know it hasn't finished yet. 
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a): 36
#problem1_b): The square root of 3
#problem1_c): The square root of 0 
#problem1_d): -5 
#
#problem2_a): True 
#problem2_b): False 
#problem2_c): False 
#problem2_d): False 
#
#problem3_a): c 
#problem3_b): b 
#problem3_c): a 
#problem3_d): b 
#
#problem4_a): 7
#problem4_b): 5 
#problem4_c): 1.5
#problem4_d): 4.5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

import random 
import math 

print "Type in 3 different numbers (decimals are OK!)"

def main(): 
	firstnumber = float(int(raw_input("A: ")))
	secondnumber = float(int(raw_input("B: ")))
	thirdnumber = float(int(raw_input("C: ")))
	largestnumber = random.randint(firstnumber, secondnumber, thirdnumber)
	output = """
Type in 3 different numbers (decimals are OK!)
""".format(firstnumber, secondnumber, thirdnumber) 
	print output
	if largestnumber == firstnumber:
		print """
The largest number was {}
""".format(largestnumber, firstnumber) 
	elif firstnumber == secondnumber:
		print """
You didn't follow directions
""".format(firstnumber, secondnumber) 
	elif firstnumber == secondnumber == thirdnumber:
		print """
You didn't follow directions
""".format(firstnumber, secondnumber, thirdnumber) 
	elif secondnumber == thirdnumber:
		print """
You didn't follow directions
""".format(secondnumber, thirdnumber)
	elif thirdnumber == firstnumber:
		print """
You didn't follow directions
""".format(thirdnumber, firstnumber)
	elif largestnumber == secondnumber:
		print """
The largest number was {}
""".format(largestnumber, firstnumber) 
	elif largestnumber == thirdnumber:
		print """
The largest number was {}
""".format(largestnumber, firstnumber) 
main() 

