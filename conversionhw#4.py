#make input statement

x = input("Select which conversion you would like to do \n type 1 to convert kilobytes to bytes \n type 2 to convert megabyte to byte \n type 3 to convert terabyte to byte \n type 4 to convert terabyte to megabyte    ")

def convert(x):

    if (x == 1):
        print(int(input("Type in the number you want to convert to bytes")))
        y = x/1000
        print(f"You have this many {y} bytes")

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

convert(x)
