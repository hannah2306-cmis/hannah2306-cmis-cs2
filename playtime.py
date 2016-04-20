def countup(n): 
	if n >= 10: 
		print "YAYYYYYYYYYY!"
	else: 
		print n
		countup(n+1) 

def count_up_from(start, stop):
	if start == stop: 
		print "YAYYYYYYYYYY!"
	else: 
		print start
		countup(start+1) 

def main():
	countup_up_from(2,12) 
	return

main() 
