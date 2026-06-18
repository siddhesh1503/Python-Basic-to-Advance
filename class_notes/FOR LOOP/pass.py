## WAP to run the loop cotinuously until the user enters password
# saved_pass = 'pyspl112'
# while True:
#     password = input('Enter password: ')
#     if password == saved_pass:
#         break
#     else:
#         print('Wrong password')
#         pass
# print('Welcome to the system')


## WAP to run the loop cotinuously until the user enters right number
# n = int(input('Enter a number: '))
# while True:
#     num = int(input('Enter number: '))
#     if num == n:
#         break
#     elif num > n:
#         print('Too high')
#     elif num < n:
#         print('Too low')
#         pass
# print('Yes, Right number')

## WAP to acess characters one by one from the all the strings which are present inside the given list
# lst =['TCS','IBM','EY']
# coll = []
# for i in lst:
#     for j in range(len(i)):
#         coll.append(i[j])
# print(coll)

# lst =['TCS','IBM','EY']
# for name in lst:
#     for char in name:
#         print(char)

## WAP to get the followiing output
#i/p =[12,"hai",89,'executed',6.7,'python']
#o/p = {'hai':2,'executed':4,'python':1}
# data = [12,"hai",89,'executed',6.7,'python']
# freq = {}
# for i in data:
#     for j in str(i):
#         if j in 'AEIOUaeiou':
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1
# print(freq)

lst = [12,"hai",89,'executed',6.7,'python']
freq = {}
for value in lst:
    if type(value) == str:
        for char in value:
            count = 0
            for char in value:
                if char in 'AEIOUaeiou':
                    count += 1
        freq[value] = count
print(freq)


n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        pass   
    else:
        print(i)