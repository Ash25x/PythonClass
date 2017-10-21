
#6
#do the argument import
#assign the arguments to argv
#make 2 txt files: file1.txt and file2.txt and type something in first one
#open the file
#read the file and assign it to a variable
#use write and copy that variable into write so that the contents of first file go over to second
# from sys import argv
# script, file1, file2 = argv
#
# open(file1)
#
# x = read.file1()
# y =file2.write(x)
#  print(y)

#7
#take inputs for all values and convert to integers
#write the function
#use if statement with a print, use and
#make an else with a print
#call function
# import math
# a = int(input("Enter a number for a  "))
# b = int(input("Enter a number for b  "))
# c = int(input("Enter a number for c  "))
# n = int(input("Enter a number for n  "))
#
# def check_fermat():
#     if n>2 and (a**n + b**n == c**n):
#         print("Fermat was wrong!")
#     else:
#         print("He was right")
# check_fermat()

#3
#make the list
#make the function
#use a for loop
#try adding index 0 to index 1 on list and index 2
#print list
#call function

list1 =[1,2,3]

def cumsum():
    for i in list1:
        i=list1[0] + list1[2]
        print(i)

cumsum()

#5
#make both lists
#use for loop
#use if else and the index so if they are equal it prints true
#go through each index
#do an else print False
list1= [1,2,4]
list2=[1,3,5]

list3=[]

for i in list3:
    if list1[0] == list2[0]:
        print(True)
    elif list1[1] == list2[1]:
        print(True)
    elif list1[2] == list2[2]:
        print(True)
    else:
        print(False)

#2
#make a list of the letters
#have a loop going throuhg it and adding ack to each string
#use append to add ack
#while i is going thhrough each letter it should add ack to it
#print it
list1 = ['J','K','L','M','N','O','P','Q']
for i in list1:
    list1.append(i + 'ack')
    print(list1)
