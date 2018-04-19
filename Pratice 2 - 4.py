#import math
#radius = int(input("What is the radious of your circle?")) #Let's the user input the radious.
#area =  math.pi *radius *radius
#print ("The are of your circle is", area)

#num1 = int(input("What is your first integer?"))
#num2 = int(input("What is your second integer?"))
#num3 = int(input("What is your third integer?"))
#total = num1 + num2 + num3
#average = total /3
#averagefinal = round(average, 2)
#print ("The average of your three numbers is", averagefinal)

name1 = input("Please enter description of the first item bought.")
item1 = float(input("Price of first item?"))
name2 = input("Please enter description of the second item bought.")
item2 = float(input("Price of second item?"))
total = item1 + item2
tax = round(total *0.13,2)
aftertax = round(tax + total, 2)
print ("Your purchases today comes to $", total)
print ("The HST on your purchase is $", tax)
print ("The total of your purchase is $", aftertax)
give = float(input("How much money do you give off the total?"))
change = round(give - aftertax,2)
print ("You received $", change, "in change.")