print("exercise 1 : chessboard\n")
i  = 0 # i declare "i" is = zero
for i in range(0,4):#for i in ran
    print(" # # # # # # # #")# display first line
    print("# # # # # # # #")#display second line
    i = i + 1#i declare i is egual i + 1


print("\nexercise 2 : matrix\n")

i=0#i declare a variable

for i in range(0, 3):#for i in suite 0 at 3
    for j in range(0, 4):#and for j in suite 0 at 4
        if i==j:#if i egual j 
            print(1)#display 1
        else:
            print(0)#else display 0
    print("\"-------\"") #display "-------"


print("\nexercise 3 : pair number\n")

nb = round(float(input("enter a number:")))#i declare nb is enter user
def panier(nb) :# i create a function named "panier"
    if (nb%2) == 0:#if nb modulo 2 is == 0
        print(bool(nb))#display true or false "nb"
    else:#sinon
        print(bool())#display ture or false ""

   

panier(nb)#call function "panier"


print("\nexercise 4 : you said factorial\n")
try:#try 
    num = 1#i declare a variable "num" to "1"
    number = int(input("enter an integer number:"))#i declare a variable "number" to number enter
    for i in range(1,number+1):#for i in range number + 1
        num = num * i#i declare num egual num multiply by "i"
        print("factorial of number is:",num)#display the foctorial of number is ...
except:#exception
        print("error is not an integer")#display messenger error


print("\nexercise 5 : dashes changes\n")

def change():#i create a function nammed "change"
     name = input("enter a string:")#i declare a variable name is = string enter of user
     nameChange = name.replace("-", "\_")#i declare a variable with replace "-" by "\_"
     print(nameChange)#i display new variable "namechange" 
     if name=="":#if name is egual not entry
        print("error")#i display an error messenger
     
change()#call the function named "change"


print("\nexercise 6 : training with boards\n")

liste = ["eau","javel","savon","gateaux","lait","chocolat","pain"]#i create a liste with items 
print("by",liste[0])#i display the first items of the list (number 0 )
print("by",liste[-1])#i display the latest items of the list (number -1)
num=(int(len(liste)/2))#i definite the middle items in the list
print(liste[num])#i display this items
       
print("\nexercise 7 : man boards\n")

information = ["nicolas", "turck", "34ans", 1985]#i create a list with informations of an users

def user(information):#i create a function named "user"
    for i in information:#for i in the list 
        print(i)#display i (items)


user(information)#call the function


print("\npartie 2 exercise 7\n")
#i create a list with several list in and items 
usersboards = [["nicolas", "turck", "34ans", 1985], ["jean", "bernard", "56ans", 1963], ["kevin", "billet", "27ans", 1991]]

def user(usersboards):#i create a function named "usersboards"
    for i in usersboards:#for i in list
        print(i)#display list an order and items

user(usersboards)#call the function


usersboards = [["nicolas", "turck", "34ans", 1985], ["jean", "bernard", "56ans", 1963], ["kevin", "billet", "27ans", 1991]]

def user(usersboards):#i create a function named "usersboards"
    for i in usersboards:#for items in list "userboards"
        for j in i:#for items in list "i"
            print(j)#display list items

user(usersboards)#call the function


print("\nexercise 8 : max of boards\n")

def maximum():#i create a function named "maximum"
    number = [54, 45, 67, 89, 3, 87, 31, 24]#i create a list with many numbers items
    print(max(number))#i display the maximum numbers items of the list

maximum()#call the function

def maximus():#i create a function named "maximus"
    boars = ["carte", "89", "livre", "54", "computeur", "100", "sac", "24"]#i creat a list with many number and name items
    print(max(boars))#i display the maximum items of the list

maximus()#i call the function


print("\nexercise 9 : a to do list\n")

toDoList = []#create a liste
user = ""#declare a variable user
while user != "fin":#conditions
    user = (input("enter a new task : "))#user = input task
    if user == "fin":#if user enter "fin"
        print(toDoList)#display the todo list
    toDoList.append(user)#enter for user adding in todolist
