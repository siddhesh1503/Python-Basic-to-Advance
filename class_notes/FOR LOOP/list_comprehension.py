
## Comprehenssion
# WAP to print list of no from 1 to 20
# num= []
# for i in range(1,21):
#     num.append(i)
# print(num)
print([i for i in range(1,21)])

# num= []
# i = 1
# while i < 21:
#     num.append(i)
#     i+=1
# print(num)

# numbers = [i for i in range(1, 21)]
# print(numbers)

# print([i for i in range(1, 21)])


# WAP to print list of characters in given string
# greet = 'Hello World'
# char = []
# print([char for char in greet])

# WAP to print list of sqaure numbers, which are present given number
# number = [1,2,3,4]
# print([num*num for num in number])

# WAP to building a list of first_name and last_name from full_name
# full_name = ["Steve Jobs", "Bill gates", "John Doe"]
# f_name = []
# l_name = []
# for name in full_name:
#     f_name.append(name.split()[0])
#     l_name.append(name.split()[1])
# print(f_name)
# print(l_name)

full_name = ["Steve Jobs", "Bill gates", "John Doe"]
# Using list comprehension to get first names
f_name = [name.split()[0] for name in full_name]
# Using list comprehension to get last names
l_name = [name.split()[1] for name in full_name]
print(f_name)
print(l_name)


# WAP to print list of even number 1 to 20
# print([i for i in range(1, 21) if i%2==0])

# WAP to print palindromes from the given list
# list = ['eve','john','anna']
# print([i for i in list if i == i[::-1]])


# WAP to print filter out those names less than 6 characters
# list = ['apple','google','yahoo','flipkart','instagram']
# print([i for i in list if len(i) < 6])

# WAP to print filter out names start from P
# list = ['apple','google','yahoo','flipkart','instagram','pappu','PRACHI','Python']
# print([i for i in list if i[0]=="P"])
# print([i for i in list if i.lower().startswith('p')])

# WAP build a list only with even strings
# list = ['apple','google','yahoo','flipkart','instagram','pappu','PRACHI','Python']
# print([i for i in list if len(i)%2==0])

# WAP reverse the item of list only if it is odd, otherwise keep it is
# list = ['apple','google','yahoo','flipkart','instagram','pappu','PRACHI','Python']
# print([i[::-1] if len(i)%2!=0 else i for i in list])

# WAP reverse the item of list only if it is string, otherwise keep it is
# print([i[::-1] if type(i)==str else i for i in list])

# squares_even = [i**2 if i % 2 == 0 else i for i in range(1, 11) ]
# print(squares_even)

# words = ['apple', 'banana', 'grape', 'mango', 'date']
# first_letters = [i[0] for i in words if i.endswith('e')]
# print(first_letters)

# words = ['apple', 'banana', 'grape', 'kiwi']
# new_words = [w.upper() if len(w) % 2 == 0 else w.lower() for w in words]
# print(new_words)

# Add the items of two list
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# sum_values = []
# for i in range(len(a)):
#     sum_values.append(a[i] + b[i])
# print(sum_values)

# print([a[i]+b[i] for i in range(len(a))])


# WAP to get the following ouput
# matrix = [[1,2,3,4],[5,6,7],[8,9,10]]
# lst = []
# for row in matrix:
#     for col in row:
#         lst.append(col)
# print(lst)

# print([col for row in matrix for col in row])
# output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

