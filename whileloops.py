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


