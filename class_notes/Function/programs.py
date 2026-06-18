# Implement the function to check the user given argument is even no or not if it is even return true if it returns false
# def user_details(numbers):
#     if numbers%2 == 0:
#         return True
#     return False
    
# print(user_details(1))
# OR
# def user_details(numbers):
#     return numbers%2 == 0
    
# print(user_details(4))

# Create the function to check given string is palindrome or not
# def string_n(string):
#     return string == string[::-1]

# print(string_n('nitin'))

# Check whether character is uppercase or not
# def is_upper(character):
#     return 'A' <= character <= 'Z'
# print(is_upper('b'))

# Create a function to print number from 1st argument to 2nd argument
# def numbers(first,last):
#     i = first
#     while i <= last:
#         print(i)
#         i+=1
# print(numbers(1,10))

# Create a function to return list of even no between user entered range
# def list(start,end):
#     even = []
#     for i in range(start,end+1):
#         if i%2 == 0:
#          even.append(i)
#     return even

# print(list(1,10))

# Write a function to check given number is perfect number or not
# def perfect(num):
#     total = 0
#     for i in range(1, num):
#         if num % i == 0:
#             total += i
#     return num == total
# print(perfect(10)) 
# print(perfect(6))   
    

# Prime number or not
# def prime(num):
#    if num <= 1:
#       return True
#    for i in range(2,int(num**0.5)+1):
#       if num%i == 0:
#          return False
#       return True
# print(prime(10))
#OR
# def isprime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num%i == 0:
#             count+=1
#     return count == 2
# print(isprime(3)) # True

# Armstrong number or not 
# def arm(number):
#     temp = number
#     total = 0
#     digits = len(str(number))  
#     while number > 0:
#         digit = number % 10
#         total += digit ** digits
#         number = number // 10
#     return total == temp
# print(arm(1634))  # True
# print(arm(154))  # False
#OR
# def arm_strong(num):
#     digits = len(str(num)) 
#     sum = 0 
#     for i in str(num):
#         sum+=int(i)**digits
#     return sum == num
# print(arm_strong(1634)) # True


# Peterson number
# def fact(num):
#     f = 1
#     for i in range(1, num+1):
#         f *= i
#     return f
# def peterson(number):
#     temp = number
#     total = 0
#     while number > 0:
#         digit = number % 10
#         total += fact(digit)
#         number = number // 10
#     return total == temp
# print(peterson(145))  # True
#OR
# def peterson(num):
#     sum = 0
#     for i in str(num):
#         fact = 1
#         for j in range(1,int(i)+1):
#             fact*=j
#         sum = sum + fact
#     return sum == num
# print(peterson(145))


# WAPT number from 1 to 10 without using any loop
