def countdown(n):
	if n <= 0:
		print "Blastoff!"
	else: 
		print n 
		countdown(n-1)

def countup(n): 
	if n >= 10: 
		print "Yippy!"
	else: 
		print n
		countup(n+1) 

def countup_from(start, stop):
	if start >= stop: 
		print "YAYYYYYYYYYY!"
	else: 
		print start
		countup_from(start+1, stop) 

def countdown_from(start, stop):
	if start <= stop:
		print"WOO HOO" 
	else:
		print start
		countdown_from(start-1, stop)
 
def adder(sum):
	print "Running total: {}".format(sum)
	inputnumber = raw_input("Next number: ")
	if inputnumber == "":
		print "The sum is {}.".format(sum)
		return sum
	else:
		sum = sum + float(inputnumber)
		adder(sum)

def largestnumber(lastnumber):
	number = raw_input("Next number: ")
	if number == "":
		return lastnumber
	elif lastnumber < float(number):
		lastnumber = float(number)
		return largestnumber(lastnumber)
	else:
		return largestnumber(lastnumber)

def smallestnumber(lastnumber):
	number = raw_input("Next number: ")
	if number == "":
		return lastnumber
	elif lastnumber > float(number):
		lastnumber = float(number)
		return smallestnumber(lastnumber)
	else:
		return smallestnumber(lastnumber)

def power(x, n):
	if n == 1:
		return x
	else:
		return x * power(x, n - 1)
def poweroutput():
	result = power(2, 8)
	print result
#def pow(x, n): 
#	if n == 0:
#		return 1 
#
#
#
def main(): 
	countdown(10) 
	countup(2)
	countup_from(2,12)
	countdown_from(32,12)
	sum = 0
	adder(sum)
	out = largestnumber(-float('Inf'))
	print "The largest number is " + str(out)
	out = smallestnumber(float('Inf'))
	print "The smallest number is " + str(out)
	poweroutput()
main() 
