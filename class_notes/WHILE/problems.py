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

# t = (10, "hello", 3.5, "python", 7, "code")
# i = 0
# result = ()
# while i < len(t):
#     if type(t[i]) == str:
#         result = result + (t[i],)
#     i += 1  
# print(result)


# a = int(input("Enter a number: "))
# b = a
# rev = 0
# while a > 0:
#     digit = a%10
#     rev = rev*10 + digit
#     a//=10

# if (rev == b):
#     print('palindrome')
# else:
#     ('Not a pal')

# def descending_order(num):
#     lst = list(num)
#     lst.sort(reverse = True)
#     return "".join(lst)
# print(descending_order("4525"))

# def descending_order(num):
#     return int("".join(sorted(str(num))))

# print(descending_order(2345325))


lst = [10, 20, 30, 40]
i = 1
while i <= 5:
    print(lst)
    i+=1