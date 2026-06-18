# a = 10
# b = 20.5
# lst = [10,20,30]
# d = {'a':1,'b':2}

# from time import sleep
# def display(func_adrs,*args,**kwargs):
#     sleep(2)
#     return func_adrs(*args,**kwargs)


# def greet():
#     return 'Hello World'

# def greeting(name):
#     return f'Hello {name}'

# def add(a,b):
#     return a+b

# def mul(a,b,c):
#     return a*b*c

# print(display(greet))
# print(display(greeting,'SID'))
# print(display(add,10,20))
# print(display(mul,1,2,3))

# from time import sleep
# def delay(func_adrs):
#     def wrapper(*args,**kwargs):
#         sleep(2)
#         return func_adrs(*args,**kwargs)
#     return wrapper

# @delay
# def greet():
#     return 'Hello World'
# @delay
# def greeting(name):
#     return f'Hello {name}'
# @delay
# def add(a,b):
#     return a+b
# @delay
# def mul(a,b,c):
#     return a*b*c

# print(greet())
# print(greeting('danish'))
# print(add(1,4))
# print(mul(1,2,3))

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Implement the log message decorator or create a fun it should add the message good unique to all other fuctions before the result 

# from time import sleep
# def delay(func_adrs):
#     def wrapper(*args,**kwargs):
#         sleep(2)
#         return func_adrs(*args,**kwargs)
#     return wrapper

# def log(func):
#     def wrapper(*args,**kwargs):
#         print('Good Evening')
#         return func(*args,**kwargs)
#     return wrapper

# @delay
# @log
# def greet():
#     return 'Hello World'

# @delay
# @log
# def greeting(name):
#     return f'Hello {name}'

# @delay
# @log
# def add(a,b):
#     return a+b

# @delay
# @log
# def mul(a,b,c):
#     return a*b*c

# print(greet())
# print(greeting('danish'))
# print(add(1,4))
# print(mul(1,2,3))

# # ------------------------------------------------------------------------------------------------------------------------------------------------------- # 


# from time import sleep
# def _delay(sec):
#     def delay(func_adrs):
#         def wrapper(*args,**kwargs):
#             sleep(sec)
#             return func_adrs(*args,**kwargs)
#         return wrapper
#     return delay

# @_delay(1)
# def greet():
#     return 'Hello World'
# @_delay(2)
# def greeting(name):
#     return f'Hello {name}'
# @_delay(3)
# def add(a,b):
#     return a+b
# @_delay(4)
# def mul(a,b,c):
#     return a*b*c

# print(greet())
# print(greeting('danish'))
# print(add(1,4))
# print(mul(1,2,3))


# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

# def _log(message):
#     def log(func):
#         def wrapper(*args,**kwargs):
#             print(message)
#             return func(*args,**kwargs)
#         return wrapper
#     return log

# @_log("good morning")
# def greet():
#     return 'Hello World'

# @_log("good evening")
# def greeting(name):
#     return f'Hello {name}'


# @_log("good morning")
# def add(a,b):
#     return a+bc


# @_log("good afternoon")
# def mul(a,b,c):
#     return a*b*c

# print(greet())
# print(greeting('danish'))
# print(add(1,4))
# print(mul(1,2,3))

# Note - Parametraised or customized decorators which are used to add customized extra functioality or different call back functions

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #
