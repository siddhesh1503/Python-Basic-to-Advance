class GrandFather:
    def land(self):
        print('I own 10 acers of land')

class Dad(GrandFather): # Single level
    def car(self):
        print('I can drive the car')
    def rules(self):
        print('Ask your mom')

class mom: 
    def cook(self):
        print('I cook a food')
    def rules(self):
        print('Come to home before 9pm')

class Son(Dad,mom):  # Multiple 
    def phone(self):
        print('I know how to use the mobile phone')

s = Son()

print(s.car())
print(s.cook())