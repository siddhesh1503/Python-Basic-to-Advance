# sum = 0
# for i in range(1,11):
#     sum+=i
# print(sum)

# n = int(input("Enter the numbers: "))
# fact = 1
# for i in range(1, n+1):
#     fact=fact*i
# print(fact)

# n = int(input("Enter the numbers: "))
# sum = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         sum +=i
# print(sum)



# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")



# num = input("Enter number: ")
# sum = 0
# for i in num:
#     sum += int(i)
# print(sum)


# list = ['apple','google','yahoo','flipkart','instagram']
# # print([i for i in list if len(i) > 6])

# print([i[::-1] for i in list if len(i)%2 == 0])


lst = [1,2,3,2,3,4,5,6]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)

# lst = [1,2,3,4,5]
# for z in lst:
#     print(z)

# n = 2
# for i in range(1,11):
#     print(n*i)

# st = 'Hello World'
# chr = 'l'
# count = 0
# for i in st:
#     if i == chr:
#      count= count + 1
# print(count)


# sum = 0
# for i in :
#     if i%2 == 0:
#         sum = sum+i
# print(sum)


# n = 10
# is_prime = True
# for i in range(1, n+1):
#     if i%2 == 0:
#         is_prime = False
#     else:
#         is_prime = True
# print(is_prime)

# num = int(input("Enter a number: "))
# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")


# num = 2
# for i in range(1,11):
#        print(f'{num} * {i} = {num*i}')
 

# num = 6
# sum = 0
# for i in range(1, num+1):
#        if num%i == 0:
#          sum += i
# if sum == num:
#      print('Perfect Number')
# else:
#      print("Not Perfect Number")


# d = {'a': 1, 'b': 2, 'c': 3}
# print({i:j*j for i,j in d.items()})

# temp = {'day1': 20, 'day2': 25, 'day3': 30}
# print({i:(j * 9/5) + 32 for i,j in temp.items()})

# marks = {'A': 45, 'B': 67, 'C': 89, 'D': 40}
# print({i:j for i,j in marks.items() if j > 60})

# data = {'a': '10', 'b': '20', 'c': '30'}
# print({i:int(j) for i,j in data.items()})

# nums = {'a': 2, 'b': 3, 'c': 4}
# print({i:j*10 for i,j in nums.items() if j%2 == 0})

# data ='hello how are you'
# freq = {}
# for i in data.split():
#     if i in freq:
#         freq[i] = freq.get(i, 0) + 1
# print(freq)

#Siddhesh123456
#ddeihhsS13526

# data = input('Enter the Name: ')
# strr = ''
# for ch in data:
#     if ch.islower():
#         strr = strr+ch
#     elif ch.isupper():
#         strr = strr+ch
# print(strr)
