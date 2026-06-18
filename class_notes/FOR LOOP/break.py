# name ='yALLUSh'
# for i in name:
#     if i.isupper():
#         print(i)
#         break

# num = int(input('Enter a number: '))
# for i in range(2, num+1):
#     if num%i == 0:
#         print('Smallest Divisor',i)
#         break

# st = 'hello'
# char ='l'
# for i in range(len(st)):
#     if st[i] == char:
#         print(i)
#         break


# for i in range(1000):
#     num = int(input("Enter number: "))
#     if num == 0:
#         break
#     total += num
# print("Total =", total)

# for i in range(1000):
#     num = int(input("Enter number: "))
#     if num == 0:
#         break
#     pass
# print('Loop ended')


password = "python123"
attempts = 3

while attempts > 0:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong Password")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")