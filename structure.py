#Define the critical functions used in the program
# These function should almost always return a value 

def mul(x,y): 
	return 2 * (x + y)  

def output(name, x, y, z):
	out = """
HEY GUYS
My name is {}. 
I am your nurse. 
Your baby girl might have {} hairs on the top of her head. 
Oops. We just detected she might have {} hairs on her face as well. 
We are afraid that if she has more than {} hairs on her face and more than {} hairs on her head... 
She could be diagnosed with hypertrichosis. 
However, if are able to wax and shave {} amount of hair on her face. 
We might get all but {} hairs on her face. 
I'm sorry but that is the best we can do. 
Hope your daughter doesn't grow up and get bullied.   
""".format(name, x, y, z)
	return out

def main():
	name= raw_input("What's your name?: ")
	x = raw_input("Type your brother's age: ")
	y = raw_input("Type your age: ") 
	z = add(int(x), int(y))
	out = output(name, x, y, z)
	print out 

main() 

