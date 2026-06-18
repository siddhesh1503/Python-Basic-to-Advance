class Point:
    a = 10     # Public
    _b = 20    # Protected
    __c = 30   # Private
    def __init__(self,x):
        self.x = x
    
    def __add__(self, other):
        print("add method is called")
        return self.x + other.x
    
    def __sub__(self, other):
        return self.x - other.x
    
p1 = Point(10)
p2 = Point(20)

print(p1.a)
print(p1._b)
print(p1.__c)