# num = int(input('Enter the number: '))
# i = 1
# while i <= 10:
#     print(f"{num} * {i} = {num * i} ")
#     i += 1

# num = int(input('Enter the number: '))
# i = 1
# sum = 0
# while i <= num:
#     sum += i
#     i += 1
# print(sum)

# string = 'YASH'
# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1


# lst = [10, 20, 30, 40 , 50]
# i = 0
# sum = 0 
# while i < len(lst):
#     sum += lst[i]
#     i+= 1
# print(sum)

# st = 'Happy Gudi Padwa 2026'
# vowel_st = ''
# i = 0
# while i < len(st):
#     # Check if the character is a vowel or a digit
#     if st[i] in 'AEIOUaeiou' or st[i].isdigit():
#         vowel_st = vowel_st + st[i]
#     i += 1
# print(vowel_st)

# data = ('Steve Jobs',101, 3.14, 'Apple', 2026)
# i = 0
# string_elements = ()
# while i < len(data):
#     if type(data[i]) == str:
#         string_elements = string_elements + (data[i],)
#     i += 1
# print(string_elements) 

# lst = ['apple', 'banana', 'cherry', 'date']
# i = 0
# empty_lst = []
# while i < len(lst):
#     if 'a' in lst[i]:
#         empty_lst.append(lst[i])
#     i += 1
# print(empty_lst)

# num = int(input('Enter the number: '))
# num_st = str(num)
# digit_sum = 0
# i = 0
# while i < len(num_st):
#     digit_sum = digit_sum + int(num_st[i])
#     i += 1
# print(digit_sum)


# Input: 5
# Output: 5 4 3 2 1
# num = int(input('Enter the number: '))
# i = num
# while i >= 1:
#     print(i, end=' ')
#     i -= 1

# Find the Largest Digit in a Number
# num = int(input('Enter the number: '))
# largest = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     num //= 10
# print(largest)

# Find the Smallest Digit in a Number
# num = int(input('Enter the number: '))
# smallest = 0
# while num > 0:
#     digit = num % 10
#     if digit < smallest:
#         smallest = digit
#     num //= 10
# print(largest)


#Count the even and odd numbers 
# num = int(input('Enter the number: '))
# even = 0
# odd = 0
# while num > 0:
#     digit = num % 10
#     if (digit%2 == 0):
#         even = even + 1
#     else:
#         odd = odd + 1
#     num //= 10
# print('Even numbers are',even)
# print('Odd numbers are',odd)


# Reverse the string
# num = int(input('Enter the number: '))
# original = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(rev)

# Palindrome or not
# num = int(input('Enter the number: '))
# original = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# if (original == rev):
#     print('It is palindrome')
# else:
#     print('It is not palindrome')

# Product of number
num = int(input('Enter the number: '))
product = 1
while num > 0:
    digit = num % 10
    product = product*digit
    num //= 10
print(product)