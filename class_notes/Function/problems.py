# # 1. function without argumets and without return values
# def greet():
#     print("Hello World")
# greet()
# print(greet())

# # 2. function with argumets and without return values
# def greeting(name):
#     print(f"Hello World {name}")

# gt =greeting('Virat')
# print(gt)

# # 3. function without argumets and with return values
# def add():
#     a=int(input("Enter the number: "))
#     b=int(input("Enter the number: "))
# x = add()
# print(x)

# # 4. function with argumets and with return values
# def mul(a,b,c):
#     return a*b*c
# y = mul(1,2,3)
# print(y)


###########################################################################
# Global variable
# x = 10
# def outer():
#     x = 30  # we can access the global variable inside local space but we cant modify
#     print(x)
# outer()
# print(x)
#output = 10 30

# x = 10
# def outer():
#     x = x + 1  # we cannot change or modify the global variable 
#     print(x)
# outer()
#output = Error

# x = 10
# def outer():
#     global x
#     x = x + 1 # By using the 'global' we can modify the global variable
#     print(x)
# outer()
# print(x)
#output = 11 11


###########################################################################    
# Local Variable

# x = 10 #global variable
# def outer():
#     y = 20 #   y is local variable for outer function
#     print(y)
#     y = y + 1
#     print(y)
#     y = y * 2
#     print(y)
#     def inner():
#         nonlocal y
#         y = y + 1
#         z = 30
#         print(z,y,x)
#     inner()
# outer()
#output 
# 20
# 21
# 42
# 30 43 10

# x = 10 #x is global variable
# def outer():
#     y = 20 #y is local variable for outer for the outer function, y is clossur
#     def inner():
#         z = 30 #z is local variable inner function 
#         print(z,y,x) #x is global variable, y enclosed variable
#     inner() 
# outer()
#output = 30 20 10

####################################################################

# def add(a,b,c):
#     print(a,b,c)
#     return a+b+c
# print(add(1,2,3))


# WAP implement a function it will return sum of minimum three numbers maximum 5 numbers

# def add(a,b,c,d=0,e=0):
#     print(a,b,c,d,e)
#     return a+b+c+d+e
# print(add(1,2,3))


# Database = []
# def reg(name,phone_no,gmail,alt_phone=None,alt_gmail=None):
#     if name and phone_no and gmail:
#         Database.append({
#             'User_name':name,
#             'Phone_Number':phone_no,
#             'Gmail':gmail,
#             'Alt_Phone':alt_phone,
#             'Alt_gmail':alt_gmail
#         })
#         return "Registration Successfull"

# reg('SID',993245235,'siddhesh@gmail.com')
# print(Database)

# WAF to get product of minimum 2 number maximum 5 numbers
# def mul(a,b,c=1,d=1,e=1):
#     return a*b*c*d*e
# print(mul(1,2,3))
# print(mul(1,2,4,4))


#########################################################################################
## Positional and keyword arguments

# def info(name,age,salary):
#     print(f'Hi my name {name} and Im {age} years old and i getting {salary} per month')
# info('SID',21,10000)


# def info(name,age,salary):
#     print(f'Hi my name {name} and Im {age} years old and i getting {salary} per month')
# info(name='SID',age=21,salary=10000)


# def info(name,age,salary):
#     print(f'Hi my name {name} and Im {age} years old and i getting {salary} per month')
# info('SID',age=21,salary=10000)


# def info(name,age,salary):
#     print(f'Hi my name {name} and Im {age} years old and i getting {salary} per month')
# info(name='SID',age=21,100000000000) # Error because positional arguments we can not access after keyword arguments


# def info(name,age,salary,/):
#     print(f'Hi my name {name} and Im {age} years old and i getting {salary} per month')
# info(name='SID',age=21,salary=100000000000)
# info(info('SID',21,100000000000)) # when we use / we can not access the positional arguments


# def info(*,name,age,salary):
#     print(f'Hi my name {name} and Im {age} years old and i getting {salary} per month')
# info('SID',21,100000000000)
# info(name='SID',age=21,salary=100000000000) # when we use * we can not access keyword arguments


# def info(name,/,age,*,salary):
#     print(f'Hi my name {name} and Im {age} years old and i getting {salary} per month')
# info('SID',21,100000000000) 



#################################################################################
## Tuple packing in python / Single packing
## args

# def pack(*args):
#     print(args)

# pack()
# pack(1)
# pack(1,2)
# pack(1,2,3)
# pack(1,2,3,4)
# pack(1,2,4,5,6,7,8)

# pack("PRACHI",101,2)
# #Output:
# ()
# (1,)
# (1, 2)
# (1, 2, 3)
# (1, 2, 3, 4)
# (1, 2, 4, 5, 6, 7, 8)
# ('PRACHI', 101, 2)



################################################################################## 
## Dictionary packing in python / Double packing
## kwargs

def packing(**kwargs):
    print(kwargs)

packing()
packing(a=1,b=2,c=3)
packing(ID=101,name='SID',age=25,salary=5000)


## Combination of args and kwargs / variable arguments
# def var_packing(*args,**kwargs):
#     print(args)
#     print(kwargs)

# var_packing()
# var_packing(2)
# var_packing(a=2)
# var_packing(1,2,a=3,b=4)
# #Output:
# ()
# {}
# (2,)
# {'a': 2}
# (1, 2)
# {'a': 3, 'b': 4}

###############################################################################
## Unpacking

# user_data =['steve',23,300]
# def User_details(name,age,salary):
#     print(name)
#     print(age)
#     print(salary)

# User_details(*user_data)

# def unpacking(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# numbers = {1,2,3,4}
# numbers = (1,2,3,4)
# unpacking(*numbers)


# d = {'x':1,'y':2,'z':3}
# unpacking(*d)
# unpacking(*d.values())
# unpacking(*d.items())
# unpacking(*range(1,5))
# unpacking(*zip("abcd",[1,2,3,4]))

####################################################################
## Unpacking collection using multiple variable declaration
# s = {'GT','RCB','MI'}
# t1,t2,t3 = s
# print(t1)
# print(t2)
# print(t3)

# d = {'x':1,'y':2,'z':3}
# x,y,z = d
# x,y,z = d.values()
# print(x)
# print(y)
# print(z)

# user_details = [101,'steve jobs',(18,11,1981),4000,'apple']
# ID,name,DOB,sal,comp = user_details
# print(ID)
# print(name)
# print(DOB)
# print(comp)

# dd,mm,yy = DOB
# print(dd)
# print(mm)
# print(yy)

## Customize Unpacking 
# user_details = [101,'steve jobs',(18,11,1981),4000,'apple']
# ID,*rest,comp = user_details
# print(ID)
# print(rest)
# print(comp)
# #output: 
# 101
# ['steve jobs', (18, 11, 1981), 4000]

# numbers = (1,2,3,4)
# n1,*rest=numbers
# print(n1)
# print(rest)
# #Output:
# 1
# [2, 3, 4]

# def unpacking(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# numbers = {1,2,3,4}
# numbers = (1,2,3,4)
# unpacking('steve',*numbers)

# Note - In customize unpacking remaining values python pack in the form list

