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
		exit()
	else:
		sum = sum + float(inputnumber)
		adder(sum)
 
def main(): 
	countdown(10) 
	countup(2)
	countup_from(2,12)
	countdown_from(32,12)
	sum = 0
	adder(sum) 
	return

main() 
