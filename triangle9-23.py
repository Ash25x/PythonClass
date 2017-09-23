#make function with 3 parameters
#use if statement and or statements
#print result
#use else and print
#call function and assign values to test it

#
# def tricheck(x, y, z):
#     if (x > y + z) or (y > x + z) or (z > x + y):
#
#         print("You can't make a triangle")
#
#     else:
#         print("You can make a triangle")
#
# tricheck(0, 5, 8)
# tricheck(5,5,5)



#Take 3 inputs
#make function
x = int(input("Type in your value"))
y = int(input("Type in your value"))
z = int(input("Type in your value"))

def tri(x, y, z):
        if (x > y + z) or (y > x + z) or (z > x + y):

            print("no")

        else:
            print("yes")

tri(x , y, z)
