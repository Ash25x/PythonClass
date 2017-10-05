#do an import math
#create the class called Shapes use init to define arguments
#creath methods for area and perimeter
#do a print statement and a return
#give those variables a class then try calling them

import math
class shapes:
    def __init__(self, a, b):
        self.a= a
        self.b = b

    def areasqrc(self):
        ar = self.a* self.b
        print(ar)
        return ar

    def persqrc(self):
        pr = (2*self.a)+ (2*self.b)
        print(pr)
        return pr

    def triar(self):
        triar = (1/2) * self.a *self.b
        print(triar)
        return triar

    def tripr(self):
        tripr = self.a + self.b
        print(tripr)
        return tripr

ex1 = shapes(4,5)
ex1.areasqrc()

ex2 = shapes(5,6)
ex2.persqrc()

ex3 = shapes(2,1)
ex3.triar()

ex4 = shapes(4,5,6)
ex4.tripr()
