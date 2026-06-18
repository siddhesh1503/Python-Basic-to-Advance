## ZIP CONCEPT
# It is built in function or iterator, which use to loop over on multiple collections 
# We can able to access values from multiple collections simultanously using zip function
# It will stop returning the values at shortest length of collections 
# It does not have structure to display all its values we can access by using for loop or type casting 
# Syntax
# zip(col1,co.2,col3...colN)

# Examples
# zip ('abc',[10,20,30,40])
# for value in zip('abc',[10,20,30,40]):
#     print(value)
# output
# ('a', 10)
# ('b', 20)
# ('c', 30)

# for char,num in zip('abc',[10,20,30,40]):
#     print(char,num)

# for char,num,tuple in zip('abc',[10,20,30,40],(2,4)):
#     print(char,num,tuple)
# output
# a 10 2
# b 20 4

# for value in zip('abc',[10,20,30,40],(2,4)):
#     print(value)
# output
# ('a', 10, 2)
# ('b', 20, 4)


# WAP to Add the 
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# sum_values = [x + y for x, y in zip(a, b)]
# print(sum_values)
# output 
# [6, 8, 10, 12]
