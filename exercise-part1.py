print("\nexercise :1 \n")
#i declare many variable
pomme = 16
poire = 4
banane = 32
orange = 12

def maxi(*args):#i create a function named "maxi" and adding "args" method
	maximum = args[0]#i declare a variable named "maximum" is same args[0]
	for fruits in args[1:]:#i create a condition 
		if fruits > maximum:#if fruit is bigger variable maximum
			maximum = fruits#i declare a variable maximum egual fruits
	return maximum#return the function

print(maxi(*[pomme, poire, banane, orange]))#i display the function with items

print("\nexercise 2:\n")

import math#import function "math"
age = int(input("enter age:"))#i declare a variable with the enter of user

if age <= 0:#if age is smallest or egual of zero
	print("enter realy age:")#i display a message "enter realy age"
if age >=21:#if the variable "age" is bigger of egual twenty one
	print("ok")#display message "ok"
if(age%2==0):#if variable "age" modulo of 2 is egual "0"
    print("your age is pair")#display message "pair"
if math.sqrt(age).is_integer():#if math sqrt function is an integer number
    print ("your age is a square")#display a message is a square
if math.sqrt(age).is_integer()==False:#if math sqrt number no
    print ("your age is not a square")#display message is not a square
