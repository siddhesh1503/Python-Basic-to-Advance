# # WAPT extract all uppercase and lowercase vowels from data
# data = input("Enter the data: ")
# char = ""
# for i in data:
#     if i in 'aeiouAEIOU':
#         char += i

# print(char)

# # WAPT count all uppercase and lowercase vowels from data
# data = input("Enter the data: ")
# count = 0
# for i in data:
#     if i in 'aeiouAEIOU':
#         count += 1
# print(count)

## WAPT extract all uppercase and lowercase and digits and special characters from data
# data = input("Enter the data: ")
# uppercase, lowercase, digit, special = "", "", "", ""
# for i in data:
#     if i.isupper():
#         uppercase += i
#     elif i.islower():
#         lowercase += i
#     elif i.isdigit():
#         digit += i
#     else:
#         special += i

# print("Uppercase:", uppercase)
# print("Lowercase:", lowercase)
# print("Digits:", digit)
# print("Special characters:", special)

## WAPT count of the specified characters from data
# data = input("Enter the data: ")
# chars = input("Enter the characters to count: ")
# count = 0
# for i in data:
#     if i in chars:
#         count += 1
# print("Count =", count)

## WAPT find the factorial of a number
# num = int(input('Enter a number: '))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i

# print('Factorial of', num, 'is', fact)

## WAPT print the devices of given number
# num = int(input('Enter a number: '))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

## WAPT print the sum of the devices of given number
# num = int(input('Enter a number: '))
# sum = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         sum += i

# print("Sum of devices:", sum)

## WAPT print the whether the given number is prime or not
# num = int(input('Enter a number: '))
# sum = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         sum += i 
# if sum == num + 1:
#     print(num, 'is a prime number')
# else:
#     print(num, 'is not a prime number')

## WAPT to print the multiplication table of a given number
# num = int(input('Enter a number: '))
# for i in range(1, 11):
#     print(num, 'X' , i, '=' , num*i)

## WAP to print the sum of the first n natural numbers
# num = int(input('Enter a number: '))
# sum = 0
# for i in range(1,num+1):
#     sum += i
# print(sum)

## WAP to print the sum of the first n odd numbers
# num = int(input('Enter a number: '))
# sum = 0
# for i in range(1,num+1):
#     if i % 2 != 0:
#         sum += i
# print(sum)


## WAP to reverse a string
# data = input('Enter a string: ')
# reverse = ""
# for i in data:
#     reverse = i + reverse
# print(reverse)


## WAP to print Sum of digits of number
# num = input("Enter number: ")
# sum = 0
# for i in num:
#     sum += int(i)
# print(sum)


## WAP to Create dictionary and print keys and values
# d = {"a":1, "b":2, "c":3}

# print("Keys:", d.keys())
# print("Values:", d.values())

## WAP to Count frequency of characters / Count words using dictionary
# data = input('Enter data: ')
# freq = {}
# for i in data:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)
# otput
# {'H': 1, 'e': 1, 'l': 2, 'o': 1}

## WAP to print Find max element in list
# lst = [2,5,1,9,3]
# m = lst[0]
# for i in lst:
#     if i > m:
#         m = i
# print(m)

## WAP to print Smallest element in list
# lst = [2,5,1,9,3]
# m = lst[0]
# for i in lst:
#     if i < m:
#         m = i
# print(m)

## WAP to print following output
# input = ['hai','hello','how','are','you']
# # output = {'hai': 3, 'hello': 5, 'how': 3, 'are': 3, 'you': 3}
# freq = {}
# for i in input:
#     freq[i] = len(i)
# print(freq)


lst = [12,"hai",89,'executed',6.7,'python']
out = set()
for value in lst:
    if type(value) == str:
        rev = ''
        for char in value:
            rev = char + rev
        out.add(rev)
    else:
        out.add(value)
print(out)



# n = int(input('Enter a number: '))
# count = 0
# for i in range(1, n+1):
#     if i % 3 == 0:
#         count += 1
# print(count)


# n = int(input("Enter terms: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a+b


# Remove spaces from a string
# data = 'kajsd iasjkdj iajsdk jaskj'
# rem = ''
# for i in data:
#     if i != " ":
#         rem+=i
# print(rem)