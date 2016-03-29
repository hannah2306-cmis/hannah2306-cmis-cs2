#Define the critical functions used in the program
# These function should almost always return a value 

def bothdaughtershairscombined(x,y): 
	return 2 * (x + y)  

def output(name, amountofhaironface,shouldhaveamountofhaironface, sumofbothdaughtershairs):
	out = """
HEY GUYS
My name is {}. 
I am your nurse. 
Your baby girl might have {} hairs on her face. 
We are afraid that if she has more than {} hairs on her face... 
Then she could be diagnosed with hypertrichosis.  
So if we add both of your daughter's amount of hair on the head and face, then we have {} amount of hair for both daughters together. 
This means really need to try and shave your daughter's face with hypertrichosis to have an even number of hairs for both children. We should end up with an easy 100.    
""".format(name, amountofhaironface, shouldhaveamountofhaironface, sumofbothdaughtershairs)
	return out

def main():
	name= raw_input("What's your name?: ")
	amountofhaironface = raw_input("Type your daughter's amount of hair on her face with hypertrichosis: ")
	shouldhaveamountofhaironface = raw_input("Type the amount of hair she should have on her face: ") 
	sumofbothdaughtershairs = bothdaughtershairscombined(int(x), int(y))
	out = output(name, amountofhaironface, shouldhaveamountofhaironface, sumofbothdaughtershairs)
	print out 

main() 
