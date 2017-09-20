people = 10
cars = 20
trucks = 15
#give values to each variable
#assign if statements
#
if cars > people:
     print("We should take the cars.")
#add elif since more than one else
elif cars < people:
     print("We should not take the cars.")
     #add else 
else:
     print("We cant decide")

if trucks >cars:
    print("Thats too many trucks")
elif trucks < cars:
    print("We should not take the cars")
else:
    print("We still cant decide")

if people > trucks:
    print("Alright lets just take trucks")
else:
    print("Fine lets stay home")
