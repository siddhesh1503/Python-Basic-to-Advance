class Calculator:
    def add (self,a,b):
        return a+b
    def add (self,a,b,c):
        return a+b+c

u1 = Calculator()
u2 = Calculator()

print(u1.add(1,2))
print(u2.add(1,2,3))