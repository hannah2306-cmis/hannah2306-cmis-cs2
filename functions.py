def add(a,b): #compute the addition of a and b 
	return a + b #

def sub(a,b): #compute the difference between a and b 
	return a - b

def mul(a,b): #compute the multiplication of a and b 
	return a * b

def div(a,b): #compute the division of a and b
	return a / b

def hours_from_seconds(a): #change the hours to seconds 
	return a / 3600 
print hours_from_seconds(86400)

import math

def circle_area(a):  
	return math.pi * (a**2) 
print circle_area(5)
 
def sphere_volume (a):
	return 1.33333333333 * math.pi * (a**3)
   
print sphere_volume(5) 

def avg_volume (a,b): 
	c= a/2
	d= b/2
	y= 1.33333333333*math.pi*c*c*c
	z= 1.33333333333*math.pi*d*d*d
	return (y+z)/2 
print avg_volume (10, 20) 
 
print avg_volume (10,20)


