
#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a function that calls itself. 
#
#
# 2) What happens if there is no base case defined in a recursive function?
#Then it will keep repeating itself and there is no end. It is called an infinite recursion. 
#
#
# 3) What is the first thing to consider when designing a recursive function?
#You have to start with a base case to not let it repeat itself over and over. 
#
#
# 4) How do we put data into a function call?
#We put data into a function call by using the variable names within parenthesis. 
#
# 
# 5) How do we get data out of a function call?
#We can do this by printing or returning the function. 
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 3, 6  
#a2 = 7, 2  
#a3 = 0, -1 

#b1 = 2 
#b2 = 2, 1 
#b3 = 4 (-2, -2)
#+15 points

#c1 = 1 (-2, 3) 
#c2 = 4 (4, -2) 
#c3 = 19 (5,5) 
#+1 points

#d1 = -4 (1, 2, 3)
#d2 =(3, 2, 1)
#d3 =(1, 3, 2) 

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


def yourguess(number):
	number == raw_input("Next: ")
#base case below
	if number == "":
		return number 
	elif number == not float(number):
		return yourguess(number)
	else:
		return yourguess(number)
def adder(sum):
	print "The average number is...".format(sum)
	inputnumber = raw_input("Next number: ")
	if inputnumber == "":
		print "The average number is {}.".format(sum)
		return sum
	else:
		sum = sum + float(inputnumber)
		adder(sum)

def main():
	yourguess(number)
	adder(sum)

