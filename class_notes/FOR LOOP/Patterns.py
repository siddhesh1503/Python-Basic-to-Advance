# *****
# *****
# *****
# *****
# *****

# for i in range(1,6):
#     for j in range(1,6):
#         print('*', end=" ")
#     print()

# *
# **
# ***
# ****
# *****

# r = 5
# for i in range(1, r+1):
#     for j in range(1, i+1):
#         print('*',end=' ')
#     print()
#or
# num =5
# for i in range(1, num+1):
#     print('* '*i)

# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# n = 5
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         print('*',end=' ')
#     print()


# 1
# 22
# 333
# 4444
# 55555
# for i in range(1, 6):
#     print(str(i)*i)


# 55555
# 4444
# 333
# 22
# 1
# for i in range(5, 0, -1):
#     print(str(i)*i)


# 1
# 12
# 123
# 1234
# 12345

# n = 5
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# 123456
# 12345
# 1234
# 123
# 12
# 1
# n = 6
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

#12345
#12345
#12345
#12345
#12345

# n = 5
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end='')
#     print()


# 654321
# 54321
# 4321
# 321
# 21
# 1

# n = 6
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()



# A
# BB
# CCC
# DDDD
# EEEEE

# for i in range(ord('A'),ord('E')+1):
#     for j in range(ord('A'), i+1):
#         print(chr(i), end='')
#     print()
#or
# for i in range(65,70):
#     print(chr(i)*(i-64))

# EEEEE
# DDDD
# CCC
# BB
# A

# for i in range(ord('E'), ord('A')-1, -1):
#     for j in range(i - ord('A') + 1):
#         print(chr(i), end="")
#     print()
#or
# for i in range(69, 64, -1):
#     print(chr(i)*(i-64))

# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(ord('A'),ord('E')+1):
    for j in range(ord('A'), i+1):
        print(chr(j), end='')
    print()

# ABCDE
# ABCD
# ABC
# AB
# A
# for i in range(ord('E'), ord('A')-1, -1):
#     for j in range(ord('A'), i+1):
#         print(chr(j), end='')
#     print()


# EDCBA
# DCBA
# CBA
# BA
# A
# for i in range(ord('E'), ord('A')-1, -1):
#     for j in range(i, ord('A')-1, -1):
#         print(chr(j), end=" ")
#     print()



# *         
# * *       
# * * *     
# * * * *   
# * * * * * 
# num = 5
# for i in range(num, 0, -1):
#     for j in range(num, 0, -1):
#         if i <= j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#or
# num = 5
# for i in range(1, num+1):
#     print("* "*i)
#or
# num = 5
# for i in range(1, num+1):
#     print("* "*i + " "*(num-i))

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# num = 5
# for i in range(num, 0, -1):
#     print("* "*i)


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
# num = 5
# for i in range(num, 0, -1):
#     for j in range(1,num+1):
#         if i <= j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#or
# num = 5
# for i in range(1, num+1):
#     print("  "*(num-i) + "* "*i)

# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 
# num = 5
# for i in range(num, 0, -1):
#     print("  "*(num-i) + "* "*i)





#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# num = 5
# for i in range(1, num+1):
#     print(" "*(num-i) + "* "*i)

# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
# num = 5
# for i in range(num, 0, -1):
#     print(" "*(num-i) + "* "*i)


#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
# num=5
# for i in range(1, num+1):
#     print(" "*(num-i) + "* "*i)
# for i in range(num, 0, -1):
#     print(" "*(num-i) + "* "*i)



# * * * * *  
# *  
# *  
# *  
# * * * * *  

# n = 5
# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print("* "*n)
#     else:
#         print("* ")

# * * * * *          
#         * 
#         * 
# * * * * * 
# n = 5
# for i in range(n):
#     if i==0 or i==n-1:
#         print('* '*n)
#     else:
#         print('  '*(n-1) + '*')


# * * * * * 
# *       *
# *       *
# *       *
# * * * * * 
# num = 5
# for i in range(1, num+1):
#     if i == 1 or i == num:
#         print('* '*num)
#     else:
#         print("*"+'  '*3+" *")


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# n = 5
# # Upper half
# for i in range(1, n+1):
#     print('*'*i + ' '*(2*(n-i)) + '*'*i)
# # Lower half
# for i in range(n, 0, -1):
#     print('*'*i + ' '*(2*(n-i)) + '*'*i)


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
# n = 1
# for i in range(1, 6):
#     for j in range(i):
#         print(n, end=" ")
#         n+=1
#     print()


# for i in range(ord('A'),ord('E')+1):
#     for j in range(ord('A'), i+1):
#         print(chr(j), end=" ")
#     print()


# for i in range(ord('A'), ord('E')-1, -1):
#     for j in range(ord('A'), i+1):
#         print(chr(j), end='')
#     print()

