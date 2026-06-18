'''
We can able to handle exception using only try and except block also, 
if we need to implement any other statment in the exception handling process we can able to use to more statement block that is else and binary block.
Example or order of exception

'''
# try:
#     print('Exception Try Block')
# except:
#     print('Executing Except Block')
#     # else block gets executed only when there is no exception in try block.
# else:
#     print('Executing Else Block')
#     # finally gets executed no matter what happens in try, except and else block
# finally:
#     print('Exception Finally Block')


# try:
#     a = int(input('Enter the number: '))
#     b = int(input('Enter the number: '))
#     c=a/b

# except:
#     print('Exception is handled check inputs')
# else:
#     print(f'a and b value are {a}, {b}')
#     print(f'out put of a by b is {c}')
# finally:
#     print('Task is done!!!')



# ---------------------------------------------------------------------------------------------------------- #



'''
CUSTOM EXCEPTION
Python will support the user to throw the error in the program by their own with the help 0f raise keyword
'''

# saved_id = 2244
# i=1
# while i<10:
#     user_pin = int(input('Enter Your Pincode'))
#     if saved_id == user_pin:
#         print('Welcome to SBI ATM you do the transactions now')
#         break
#     else:
#         print('Wrong Pincode')
#         i+=1
#     if i == 4:
#         raise ValueError('Maximum attempts are reached for today')

# ---------------------------------------------------------------------------------------------------------- #
    
# a = int(input('Enter the value for a: '))
# b = int(input('Enter the value for b: '))

# if a > b:
#     print(a+b)
# else:
#     raise ValueError('a always greater than b')



# ---------------------------------------------------------------------------------------------------------- #


    
'''
ASSERTION
One of way to raise user exception in programs.
when we dont know the standard error,
name then we can go for assertion
Syntax:
  assert condition, 'message'
  statement block
'''

a = int(input('Enter the value for a: '))
b = int(input('Enter the value for b: '))

assert a > b, 'a should be greater than b'
print(a+b)
print('We can use a and b value for next opertions')