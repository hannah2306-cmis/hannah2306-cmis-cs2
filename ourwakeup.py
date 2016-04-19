
print "This program will ask for 5 integer or float values. It will calculate the average of all values from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd." 

def main(): 

    number0 = raw_input("n0: ") 
    if float(number0) < 0 or float(number0) >= 10: 
        floatednumber0 = float(number0)
        print (floatednumber0, " is out of range.")

	else sumofnumbers = float(0thnumber):
        Anumberofnumbers = 1
     
    firstnumber = raw_input("n1: ") 
    if float(firstnumber) = 0 or float(firstnumber) >= 10:
            floatedfirstnumber = float(firstnumber) 
            print floatedfirstnumber " is out of range." 
 
        elif float(0thnumber) >= 0 or float(0thnumber) < 10:
                sumofnumbers = float(0thnumber) + float(firstnumber) 
                Bnumberofnumbers = Anumberofnumbers + 1
    secondnumber = raw_input("n2: ")
    if float(secondnumber) < 0 or float(secondnumber) >= 10:
            floatedsecondnumber = float(secondnumber)
            print floatedsecondnumber " is out of range."

        elif float(firstnumber) >= 0 or float(firstnumber) < 10:
                sumofnumbers = float(firstnumber) + float(secondnumber) 
                Bnumberofnumbers = Anumberofnumbers + 1
 
    thirdnumber = raw_input("n3: ")
    if float(thirdnumber) < 0 or float(thirdnumber) >= 10:
            floatedthirdnumber = float(thirdnumber)
            print floatedthirdnumber " is out of range."

        elif float(secondnumber) >= 0 or float(secondnumber) < 10:
                sumofnumbers = float(secondnumber) + float(thirdnumber) 
                Bnumberofnumbers = Anumberofnumbers + 1

    fourthnumber = raw_input("n4: ") 
    if float(fourthnumber) < 0 or float(fourthnumber) >= 10: 
            floatedfourthnumber = float(fourthnumber)
            print floatedfourthnumber " is out of range." 

        elif float(thirdnumber) >= 0 or float(thirdnumber) < 10:
                sumofnumbers = float(thirdnumber) + float(fourthnumber) 
                Bnumberofnumbers = Anumberofnumbers + 1

