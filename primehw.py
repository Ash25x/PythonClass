#make function after you make an input
#assign the input to a variable and make the input an int
x = int(input("Enter a number >> "))
#create if else statement inside function
def prime(x):
    if (x > 1):
        for y in range(2,x):
#create a y variable
#set the range for y to be greater than 1
#make another if statement to do the math and print 
            if (x % y) == 0:
                print(f"{x} is not a prime number")
                break
#use break to separate from else statement
#kept printing everything without break
        else :
#make else statement
            print(f"{x} is prime")

#call the function
prime(x)
