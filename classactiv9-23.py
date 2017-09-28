#1

#ex34
# animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
#
# 1. bear
# 2. python3.6
# 3. bear
# 4. peacock
# 5. kangaroo
# 6. python3.6
# 7. whale
# 8. kangaroo

#2
#create function and argument
x = int(input("Enter the time in minutes you want to convert to seconds > "))
#create a variable asking for input, do math and print
def sec (x):
    y= x * 60 + 42
    print(f"There are this many {y} seconds")

sec(x)
#call function

#3
#create a variable that takes input
kilo = int(input("Enter the amount of kilometers you want to convert: > "))
def conv(kilo):
#create function
    mile = kilo / 1.61
    #do math and print result
    print(f"There are this many miles {mile}")

conv(kilo)
#pull function


#4
faren = int(input("Enter the degrees in fahrenheight that you want to convert to celsius: > "))
#assign variable to input integer
def conv1(faren):
    #define function
    #do math and store in variable
    c = ((faren - 32) * (5/9))
    print(f"{faren} degrees in farenheight is {c} degrees celsius")

conv1(faren)
    #call function


#5
import math
#import math library
z = int(input("Enter one of the numbers 81, 19, 16, 121 to get the square root of it "))
#make if elif statements to print sqrt of the number input
if z == 81:
    print(f"The square root of {z} is {math.sqrt(z)}")

elif z == 19:
    print(f"The square root of {z} is {math.sqrt(z)}")

elif z == 16:
    print(f"The square root of {z} is {math.sqrt(z)}")

elif z == 121:
    print(f"The square root of {z} is {math.sqrt(z)}")

else:
    print("Wrong number mate! ")
#make an else for other numbers they input

#6
#returns area of a circle r = 9
r = int(input("Enter the radius you want to get the area of "))
#make function and do the math math.pi represents pi ** is square
def area(r):
    a = (r ** 2) * math.pi
    print(f"Area of {r} is {a} ")
#call function
area(r)


#7
#create input

#define x in the strings

#make if else statements if x in num6 then return true and print it otherwise false
num6 =str(input("Type a string in here >> "))
#
def xinsid(num6):
    if ("x" in num6):
         print(True)
         return True

    else:
         print(False)
         return False

xinsid(num6)
#call function

#8
#boolean function that returns true false if letters are a,e,i,o,u and in string by user
num7 = input("Type something in here >")
print(num7)

def aeiou(num7):
    letters= ["a", "e", "i", "o", "u"]
    print(letters[0])
    print(len(letters))
    for i in range(len(letters)):
        if (letters[i] in num7):
            print(True)
            return True

        else:
            print(False)
            return False

aeiou(num7)

#9 slack

#write function

def rad6(v):
    r6 = (4/3) * math.pi*v**3
    print(r6)

rad6(5)

#10
#make function, take an input
#make if/else statement
#do math inside and print and return true false
#call function
w = int(input("Enter a number to divide by 3:  "))

def num10(w):
    if w % 3 == 0:
        print(True)
        return True

    else:
        print(False)
        return False
num10(w)

#11
#do import datetime to get preset function
#assign a variable to datetie.date.today() and print it
import datetime
now = datetime.date.today()
print (now)

#12
#do import datetime
#assign variable to time formula and print variable
import datetime
current = datetime.datetime.now().time()
print(current)

#13
#type up input, then function
#use count and put string in quotes for it to count that string
#asssign it  variable and print it
g = input("Type in something here > ")

def acount(g):
    f = g.count('a')
    print(f"{g} has an 'a' in it {f} times ")

acount(g)



#14
#write an input and assign to variable
#create function, have it print lenth of variable and call function

e = input("Enter your word here >> ")

def wrdcnt(e):
    print(f"{e} has {len(e)} letters" )

wrdcnt(e)

#15
#make function, leave it blank this time since we wont be taking input
#start the count at 20, do a while loop and print what it counts
#make count equal to itself minus 1 so it goes down each time loop goes
#call fucntion

def cnt():
    count = 20
    while count >= 0:
        print(count)
        count = count - 1

cnt()

#16
#make it divisible by 2 remainder 0 after wrtiing function
#print even if true, else make it odd and call function


k =int(input("Enter a number here > "))
def numodd(k):
    if k % 2 == 0:
        print("This is even")

    else:
        print("This is odd")

numodd(k)


#17
#do the input

l = input("Enter a string here > ")
def strlng(l):
    counter = 0
    for char in l:
        counter += 1


strlng(l)

#18
#do the input
u = input("Enter a string here > ")
length = 0
while len(u) 
    length += 1
print(length)
