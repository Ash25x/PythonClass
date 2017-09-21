#make input statement

x = input("Select which conversion you would like to do \n type 1 to convert kilobytes to bytes \n type 2 to convert megabyte to byte \n type 3 to convert terabyte to byte \n type 4 to convert terabyte to megabyte    ")
#make a input and assign variable
def convert(x):
#start a function with if statements
#use if and the value of x from input to determine outcome
# do math inside if/elif statements and asign to variable
#print result 
    if (x == 1):
        print(int(input("Type in the number you want to convert to bytes")))
        y = x/1000
        print(f"You have this many {y} bytes")
#use elif for the other inputs
    elif (x == 2):
        print(int(input("Type in the number you want to convert to bytes")))
        y = x/1000000
         print(f"You have this many {y} bytes")

    elif (x == 3):
        print(int(input("Type in the number you want to convert to bytes")))
        y = x/1099511627776
         print(f"You have this many {y} bytes")

    elif (x == 4):
        print(int(input("Type in the number you want to convert to megabytes")))
        y = x/1000000
         print(f"You have this many {y} megabytes")
#make an else if they type something else
    else:
        print("This is not one of the options!")
#call the function
convert(x)
