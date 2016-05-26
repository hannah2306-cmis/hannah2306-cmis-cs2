x = 0
while x < 11:
	print x 
	x += 1

x = 50
while x >= 0:
	print x
	x -= 1 

def countdown(x):
	while x >= 0:
		print x
		x -= 1 
countdown(50)

#count down
def count(x):
	if x > 0:
		while x >= 0:
			print x
			x -= 1
#count up
	else:  
		while x <= 0:
			print x 
			x += 1
count(10)
count(-10)

def countfrom(start, stop):
	while start < stop:
		print start 
		start += 1 
	while start > stop: 
		print stop
		stop -= 1 
countfrom(-10, 10) 

def sumOfOdds(n):
	total = 0 
	while n < 0:
		if n % 2 == 0:
			n += 1 
		else:
			total += n 
			 
	while n > 0: 
		print stop
		stop -= 1 
countfrom(-10, 10) 



