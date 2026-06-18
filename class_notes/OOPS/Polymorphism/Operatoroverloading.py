lst1 = list([1,2])
lst2 = list([3,4])

st1 = {1,2,3}
st2 = {4,5,6}

class Point:
    def __init__(self,x):
        self.x = x
    
    def __add__(self, other):
        print("add method is called")
        return self.x + other.x
    
    def __sub__(self, other):
        return self.x - other.x
    
p1 = Point(10)
p2 = Point(20)

print(p1+p2)
print(p1-p2)