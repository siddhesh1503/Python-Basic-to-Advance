for i in range(1,12):
    if i==6 or i==9:
        continue
    print(i)

# list = []
# for i in range(1, 12):
#     if i%2!= 0:
#         continue
#     list.append(i)
# print(list)

# a = [1,2,3,4,5,8,'hello','haii']
# items = []
# for i in range(len(a)):
#     if i%2 == 0:
#         continue
#     items.append(a[i])
# print(items)


n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i%3 == 0:
        continue
    print(i)