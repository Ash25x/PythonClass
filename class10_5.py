import math
class Rectangle():
   def __init__(self, width, height):
       self.width= width
       self.height= height

   def area(self):
       ar = self.width * self.height
       return print(f" The area is {ar}")

z = Rectangle(2, 6)
z.area()


#make the class first
#then use class newclass(oldclass):
#do a regular __init for new class add arguments if you want
#then oldclass.__init__ copy the same amount of old arguments
#you can change them
#define the new argument you added
#when calling it

class Triangle(Rectangle):
   def __init__(self, base, w, h):
       Rectangle.__init__(self, w, h)
       self.base = base

   def triarea(self):
       ab = (1/2)*(self.base* self.height)
       return print(f"The area is {ab} ")

bleh = Triangle(4, 2, 4)
bleh.area()

hi = Triangle(2,4,6)
hi.triarea()

x= Rectangle(3,2)
x.area()
