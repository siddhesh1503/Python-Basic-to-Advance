#extract t from string in form of list

# s1="the theory of relativity"
# lst=[]
# for i in s1:
#     if i=='t':
#         lst.append(i)
# print(lst)

#extract 'the' sequence in form of list
s1="the theory of relativity"
lst=[]
for i in s1.split():
    if i == 'the':
        lst.append(i)
print(lst)
