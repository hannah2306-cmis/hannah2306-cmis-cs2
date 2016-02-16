def add(a,b): #compute the addition of a and b 
	return a + b 

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

def circle_area(a): #taking one argument then representing it as the radius of a circle and finding the area of the circle   
	return math.pi * (a**2) 
print circle_area(5)
 
def sphere_volume (a): #find the volume of a sphere
	return 1.33333333333 * math.pi * (a**3)
   
print sphere_volume(5) 

def avg_volume (a,b): #find the average of the volumes 
	c= a/2
	d= b/2
	y= 1.33333333333*math.pi*c*c*c
	z= 1.33333333333*math.pi*d*d*d
	return (y+z)/2 
print avg_volume (10, 20) 
 
def area(a,b,c): #find the area of 3 side lengths of a triangle  
	s=(a+b+c)/2 
	return (s*(s-a)*(s-b)*(s-c))**0.5
print area(1,2,2.5) 

def right_align(a): #word with additional spaces so that it is exactly aligned on the screen
	return(80-len(a))*(" ") + a
print right_align("Hello") 

def center(a): #word with additional spaces so that it is exactly centered on the screen 
	return (40-len(a))*(" ") + a
print center ("Hello") 

def msg_box(a): #string as an argument then returning a message box 
	return "+" + ((len(a)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (a)+ (2*" ") + "|" + "\n" + "+" + ((len(a)+4)*"-") + "+" 
print msg_box("Hello") 
print msg_box("I eat cats!")

print hours_from_seconds(86400)
print circle_area(5)
print sphere_volume(5) 
print avg_volume (10, 20)
print area(1,2,2.5) 
print right_align("Hello")
print center ("Hello")
print msg_box("Hello") 
print msg_box("I eat cats!")

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
hours_from_seconds(a)
circle_area(a)
sphere_volume (a)
avg_volume (a,b)
area(a,b,c)
right_align(a)
center(a)
msg_box(a)
