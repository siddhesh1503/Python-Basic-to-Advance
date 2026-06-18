# Set Comprehensions
# Set comprehensions is a way to build sets from sequence or any other iterable type by filtering and tranforming items.

# WAP to extract set of unique even numbers from the given tuple of numbers

numbers = (1,2,3,4,1,2,3,41,2,3,4,5,6,7,8,9,1,2,4)
unique = set()
for i in numbers:
    if i not in unique:
        unique.add(i)

# print({i for i in numbers if i%2 == 0})