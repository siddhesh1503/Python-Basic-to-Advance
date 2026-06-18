# data = input('Enter the data:')
# if not data.isalnum():
#     print('Yes data having the special characters')
# else:
#     print('Not having the special characters')

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# if a > b:
#     if a > c:
#         print("a is greatere")
# elif b > c:
#     print("b is greater")
# else:
#     print("c is greater")


# num = input("Enter a number: ")
# if num.isdigit():
#     num = int(num)
#     if num % 5 == 0:
#         print("Yes, it is divisible by 5")
#     else:
#         print("It is not divisible by 5")
# else:
#     print("Entered value is not a number")

# a = int(input("Enter a number: "))
# if a > 0:
#     print("Number is positive")
#     if a%2 == 0:
#         print("Number is even")
#     else:
#         print("Number is not even")
# else:
#     print("Number is not positive")

# name = "Yash"
# i = 0
# while i < len(name):
#     print(name[i])
#     i+=1


# num = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= num:
#     sum = sum + i
#     i+=1
# print(sum)

# num = int(input("Enter a number: "))
# sum = 0
# while num > 0:
#     a = num%10
#     sum = sum + a
#     num//=10
# print(sum)

# num = int(input("Enter a number: "))
# fact = 1
# i = 1

# while i <= num:
#     fact = fact * i
#     i += 1

# # print(fact)

# num = int(input("Enter a number: "))
# i = 1

# while i <= num:
#     if num % i == 0:
#         print(i)
#     i += 1

# num = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= num:
#     if num % i == 0:
#         sum = sum + i
#     i += 1
# print("Sum of factors =", sum)

# i = 1
# while i <=10:
#     print(i)
#     i+=1

t = (10, "hello", 3.5, "python", 7, "code")
i = 0
result = ()
while i < len(t):
    if type(t[i]) == str:
        result = result + (t[i],)
    i += 1  
print(result)
