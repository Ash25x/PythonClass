#write function and define arguments, they want cheese amount
#and how many boxes of cracker
def cheese_and_crackers(cheese_amount, crackerboxes):
    #make a variable with the result
    #print the variable
    print(f"You have {cheese_amount} cheeses!")
    print(f"You have {crackerboxes} of boxes of crackers!")
#make a statment
    print("Man thats enough for a party")
    print("Get a blanket.\n")

#assign numbers to use with function
print("You can just use numbers directly")
cheese_and_crackers(20, 30)

#assign values to arguments
print("Or we can assign variables from our own script")
cheese = 10
crackcount = 50

#use them in function, new entries
cheese_and_crackers(cheese, crackcount)

#make statement and do addition for function
print("We can even do math inside too")
cheese_and_crackers(10 + 20 + 30, 10 + 40)

#combine variables and the math
cheese_and_crackers(cheese + 400, crackcount + 200)
