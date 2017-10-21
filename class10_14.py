class Other:
    def override(self):
        print("Other override() " )

    def implicit(self):
        print("Other Implicit()")

    def altered(self):
        print("Other altered()")
#make your own class
class Child:
    def __init__(self):
        self.other = Other()
#do init to pull the class#do self.other = Other
    def implicit(self):
        self.other.implicit()
#pull class and unction from Other
    def override(self):
        print("CHILD Override()")
#You can override the Other class function in this one
    def altered(self):
        print("CHILD before it was altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
#Pull the function from previois class and print it, then make a new function in it
son =Child()
#print everything
son.implicit()
son.override()
son.altered()
