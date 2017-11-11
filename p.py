# #write a function that takes an array of integers
# # and returns if it has more even numbers or more odd numbers?
#
# l =[2,4,6,8,7]
#
# def array1(l):
#     countodd = 0
#     counteven = 0
#     for i in l:
#         if i % 2 == 0:
#             counteven += 1
#             print(counteven)
#         else:
#             countodd +=1
#             print(countodd)
#     if counteven > countodd:
#         print("even is greater")
#
#     else:
#         print("odd is greater")
# array1(l)
#
# #WriteaPythonprogramthatacceptsastringandcalculatethenumberofdigitsandletters
# s= "string"
# x= 0
# y= 0
# for i in s:
#     if i.isdigit():
#         x += 1
#
#     elif i.isalpha():
#         y += 1
#
# print(x)
# print(y)
#
# a= [1,5,6,7,8]
# def lisadd(a):
#     count = 0
#     for i in a:
#         count= count + i
#     print(count)
# lisadd(a)
#
# #writeaprogramthattakesanarrayofintsandreturnsanotherarraythatcontainsthesquaresofelementsfromfirstarra
# o=[2,4,6,1]
# p=[]
# for i in o:
#     p.append(i**2)
# print(p)
#
# #WriteaPythonscripttocheckifagivenkeyalreadyexistsinadictionary
# d = {'h':2, 'blah':'garbage', 'arroz':'con poyo'}
# def ifindic(i):
#     if i in d:
#         print("ya")
#     else:
#         print('nah')
# ifindic('g')
# ifindic('h')
# ifindic('garbage')
#
# def printdic():
#     for i in d:
#         print(d)
#         print(d['blah'])
# printdic()
#
# def deldic():
#     print(d)
#     if 'h' in d:
#         del d['h']
#         print(d)
#     else:
#         print("not in dic")
# deldic()

s= ('hello')
file1 =open('filenamez', 'a')
#x= file1.read()
file1.write(s)
file1.close

x=open('filenamez', 'a')
y=open('file2', 'r')
w=y.read()
x.write(w)
x.close()
y.close()
