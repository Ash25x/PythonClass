# #horror = {'movie1': 'IT', 'movie2': 'Annabelle', 'villian' : 'evil demon'}
# #define dictionary dict()
# h1 = dict()
# h1['movie1'] = 'IT'
# h1['movie2'] = 'Annabelle'
# h1['villian'] = 'evil demon'
#
# for i in h1:
#
#     if "IT" == h1[i] :
#         print("yes")
#     else:
#         print("no")
#
# #string bananaaas has the following
# #{'b':1, 'a':6, 'n':2}
#
# #make dict(), give value to key
# #dont give a value
# #make a string to take an input
# ##write a for statement using a key in input
# #make an if statement using dict and key to add 1
# #make
# #try adding the letter
#
# fruit = dict()
#
# string = input("Type a fruit in here > ")
#
# for x in string:
#
#     if x in fruit:
#         fruit[x] += 1
#
#     else:
#         fruit[x] = 1
# print(fruit)

#class activity after lunch
#assign argument
#open file2
#read file2
#do a for line to count lines and do a count to count the lines
#print the count
# from sys import argv
# script, file2 = argv
# count = 0
# y= open(file2)
#
# for line in y:
#     count += 1
#
# print(count)

#classexample
#make a name for the class and give it a paramter
#use init to give the function arguments
#take the argument and define it
#make a function
#assign happy bday to the class song and use square brackets
#to make it print something
#repeat the same for bulls on parade
#call the function using the variable . the method and ()

class Song(object):
   def __init__(self, lyrics):
       self.lyrics= lyrics

   def sing_me_a_song(self):
       for line in self.lyrics:
           print(line)

happy_bday = Song(["Happy bday to you",
                   "I dont want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])

happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()


# [4:31]
# test.import.txt
#
#
# [4:32]
# import classactiv9_30 as wc
# print(wc.)
