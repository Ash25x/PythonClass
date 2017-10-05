# list3 = []
# list1= [8, 5, 8]
#
# list2= [5, 2, 5]
#
# for i in range (len(list1)):
#     x = list2[i] - list1[i]
#     list3.append(x)
#
# print(list3)
#
#
# list1 = ['IT', 'Annabelle', 'Conjuring']
# list2 = ['Costumes', 'Halloween', 'Eggs']
# #make first 2 lists, leave 3rd blank
# list3 = []
# for i in range(len(list1)):
#     z = list[i] + list[i]
#     list3.append(z)
#
# print(list3)

pokemon = ['pikachu', 'charmander', 'squirtle', 'bulasaur']
#make list
#print the list with the index
print(pokemon[1])

pokemon[1]= 'charizard'
print(pokemon[1])

pokemon

halloween = {'movie' : 'IT' , 'costume' : 'clown', 'Annabelle' : 'evil spirit'}
print(halloween['costume'])
print(halloween['Annabelle'])

states = {
   'oregon' : 'or'
   'Florida : 'fl'
   'newyork' : 'ny'
   #define dictionary {'' : ''}
}

ten_things = "Apples 0ranges Crows Telephone Light Sugar"

print(" Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
   next_one = more_Stuff.pop()
   print("Adding: ", next_one)
   stuff.append(next_one)
   print(f"There are {len(stuff)} items now. ")

print("There we go: ", stuff)

print("Lets do some things with stuff")

print(stuff[1])
print(stuff[-1]) # whoa fancy
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
