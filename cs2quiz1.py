#Part 1: Terminology (15 points)

#1 1pt) What is the symbol "=" used for?
#This symbol is called an assignment operator. 
#You use it to assign values from the right side to the left side. For #examle z = x + y assigns value of x + y into the variable z. 
#In other words, it is used to put a value inside a variable. 

#2 3pts) Write a technical definition for 'function'
#A function is a named sequence of statements that does a computation, or math.  
#When you are defining a function,you state the sequence of statements and #the name. You can also "call" a function.   
#For example: type(54) --> This means the name of the function is type and #the argument of the function is in the parentheses. The output that you #will get from this functions is the type of argument. 
#3 1pt) What does the keyword "return" do?
#When you return something, you are spitting out a value. 
#So, when a functions takes an argument and "returns" an answer. This answer #and result is known as the return value. 
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide #two
#   examples of each below
#	1: Boolean--
#For example bool(1 == 1) which is true.   
#For example bool(2 ==3 ) which is false. 
#	2:Integer
#For example: 1, -34 
#	3:string
#Ex. = "Hello", "What's up"
#	4:tuple 
#ex. ("Hannah", "Staton", 15, "student") 
#	5:floating point
#ex. = 1.0, 5.0 
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#Function call is the code that is used to pass control to a function. (b = mul(5,6) 
#Function definition is a block of code that does an operation and returns a result. It has parameters which is the input and return the result. (add(5,6)) 
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:Input -- you are putting in a value into the program 
#	2:Process -- it performs a computation 
#	3:Output --the result of the computation 

#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
def sum3circlearea(a, b, c): 
	return (a + b + c) 
def output (a, b, c, d): 
	out = """
The area of circle number 1 is {}. 
The area of the circle number 2 is {}
The area of the circle number 3 is {}
Circle      Diameter
c1          {}
c2          {}
c3          {} 
Totals      {} 
""".format(a, b, c) 
	return out

def main():
	a = raw_input("Area of c1: ")
	b = raw_input("Area of c2: ") 
	c = raw_input("area of c3: ")
	d = sum3circlearea(int(a), int(b), int(c))
	out = output(a, b, c, d) 
	print out

main()
