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

import math

def circle_area(a): #taking one argument then representing it as the radius of a circle and finding the area of the circle   
	return math.pi * (a**2) 
 
def sphere_volume (a): #find the volume of a sphere
	return 1.33333333333 * math.pi * (a**3)

def avg_volume (a,b): #find the average of the volumes 
	c= a/2
	d= b/2
	y= 1.33333333333*math.pi*c*c*c
	z= 1.33333333333*math.pi*d*d*d
	return (y+z)/2 
 
def area(a,b,c): #find the area of 3 side lengths of a triangle  
	s=(a+b+c)/2 
	return (s*(s-a)*(s-b)*(s-c))**0.5

def right_align(a): #word with additional spaces so that it is exactly aligned on the screen
	return(80-len(a))*(" ") + a

def center(a): #word with additional spaces so that it is exactly centered on the screen 
	return (40-len(a))*(" ") + a 

def msg_box(a): #string as an argument then returning a message box 
	return "+" + ((len(a)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (a)+ (2*" ") + "|" + "\n" + "+" + ((len(a)+4)*"-") + "+" 

add1 = add(5,6) 
add2 = add(9,6)
sub1 = sub(8,3)
sub2 = sub(7,6) 
mul1 = mul(8,8)
mul2 = mul(7,7) 
div1 = div(4,4)
div2 = div(2,2)
time1 = hours_from_seconds(270000)
time2 = hours_from_seconds(28800) 
circlearea1 = circle_area(4) 
circlearea2 = circle_area(6) 
volumesphere1 = sphere_volume(8)
volumesphere2 = sphere_volume(2) 
average1 = avg_volume (23,45)
average2 = avg_volume (46, 89) 
area1 = area(3,4,5)
area2 = area(6,8,10) 
right1 = right_align("My name is Hannah")
right2 = right_align("You are a computer") 
center1 = ("Hi")
center2 = ("What are you doing")
box1 = msg_box("What's up")
box2 = msg_box("I love dogs")

print msg_box(str(add1))
print msg_box(str(add2))
print msg_box(str(sub1))
print msg_box(str(sub2))
print msg_box(str(mul1))
print msg_box(str(mul2))
print msg_box(str(div1))
print msg_box(str(div2))
print msg_box(str(time1)) 
print msg_box(str(time2))
print msg_box(str(circlearea1))
print msg_box(str(circlearea2))
print msg_box(str(volumesphere1))
print msg_box(str(volumesphere2))
print msg_box(str(average1))
print msg_box(str(average2))
print msg_box(str(area1))
print msg_box(str(area2))
print right1
print right2
print center1
print center2
print box1
print box2
