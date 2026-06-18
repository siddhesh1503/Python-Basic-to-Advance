# It is the process of calling the function by itself, until given recursion condtion is satisfied or upto maximum recursion depth which is 1020
# Maximum recursion length is 1020
# Function can called by itself 1020
# We can increase the maximum recursion length using built-in models
# Recursion is not recommended in the all the scinarios of python programming only whenever reverse trace back structure or tree like structure or nested loop implementation is there then we can use recursion 

# Example 
# WAP to print 1 to 10 using recursion
# def countup(i=1):
#     if i < 11:
#         print(i)
#         i+=1
#         countup(i)
# countup()

# WAPT print even numbers from 20 to 2
# def even(i=20):
#     if i >= 2:
#         print(i)
#         i-=2
#         even(i)
# even()

# WAPT access 1 by 1 character from the given string
# def string(a,i=0):
#     if i < len(a):
#         print(a[i])
#         string(a,i=i+1)
# string("RCB")

# data = [1,2,3,4,5,6,7,8,9,10,11,12]
# def even(data,lst=[],i=0):
#     if i < len(data):
#         if data[i]%2 == 0:
#             lst.append(data[i])
#         even(data,lst,i=i+1)
#     return lst

# print(even([1,2,3,4,5,6,7,8,9,10,11,12]))


# WAPT get the following output
#i/p = [12,"hai",89,"Executed",6.7,"python"]
#o/p = {'hai': 3, 'Executed': 8, 'python': 6}
# def dvc(data,out={},i=0,j=0,count=0):
#     if i>=len(data):
#         return out
#     if type(data[i]) == str:
#         if j < len(data[i]):
#             if data[i][j] in 'AEIOUaeiou':
#                 count+=1
#             return dvc(data,out,i,j+1,count)
#         else:
#             out[data[i]] = count
#             return dvc(data,out,i+1,0,0)
#     else:
#         return dvc(data,out,i+1,0,0)
    
# print(dvc([12,"hai",89,"Executed",6.7,"python"]))
    


# WPT Print Characters one by one from the list of names by avoiding nested loop only 
##names=['YASH', 'RAM', 'KASHI', 'PAVAN']
# def chars(names,i=0,j=0):
#     if i<len(names):
#         if j<len(names[i]):
#             print(names[i][j])
#             chars(names,i,j=j+1)
#         else:
#             chars(names,i=i+1,j=0)

# print(chars(['YASH', 'RAM', 'KASHI', 'PAVAN']))

# # WAPT extract string data from the tuple
# numbers = ('apple',12,4.5,'google',(2+4j),'TCS')

# def data(string,out=[],i=0):
#     if i < len(string):
#         if type(string[i]) == str:
#             out.append(string[i])
#         data(string,out,i=i+1)
#     return out

# print(data(('apple',12,4.5,'google',(2+4j),'TCS')))

# def str_data(data,out=[],i=0):
#     if i == len(data):
#         return out
#     if type(data[i]) == str:
#         out.append(data[i])
#     return str_data(data,out,i=i+1)

# print(str_data(('apple',12,4.5,'google',(2+4j),'TCS')))


# WAP to for factorial of any number using recursion
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num*factorial(num-1)

# print(factorial(5))
        

# Extract all the vowels from the string using recursion 
# def vowels(data,string="",i=0):
#     if i < len(data):
#         if data[i] in 'AEIOUaeiou':
#             string += data[i]
#         return vowels(data,string,i=i+1)
#     return string
# print(vowels('Hello World'))

