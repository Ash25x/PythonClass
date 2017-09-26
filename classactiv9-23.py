#create function and argument
x = int(input("Enter the time in minutes you want to convert to seconds > "))
#create a variable asking for input
def sec (x):
    y= x * 60 + 42
    print(f"There are this many {y} seconds")

sec(x)
#call function

#create a variable that takes input
kilo = int(input("Enter the amount of kilometers you want to convert: > "))
def conv(kilo):
#create function
    mile = kilo / 1.61
    #do math and print result
    print(f"There are this many miles {mile}")

conv(kilo)
#pull function

faren = int(input("Enter the degrees in fahrenheight that you want to convert to celsius: > "))
#assign variable to input integer
def conv1(faren):
    #define function
    #do math and store in variable
    c = ((faren - 32) * (5/9))
    print(f"{faren} degrees in farenheight is {c} degrees celsius")

conv1(faren)
    #call function


#4
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
#returns area of a circle r = 9
r = int(input("Enter the radius you want to get the area of "))
#make function and do the math math.pi represents pi ** is square
def area(r):
    a = (r ** 2) * math.pi
    print(f"Area of {r} is {a} ")
#call function
area(r)


#number 6
#create input

#define x in the strings

#make if else statements if x in num6 then return true and print it otherwise false
# num6 =str(input("Type a string in here >> "))
#
# def xinsid(num6):
#
#
#     if ("x" in num6):
#         print(True)
#         return True
#
#     else:
#         print(False)
#         return False
#
# xinsid(num6)
#call function
#7
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
