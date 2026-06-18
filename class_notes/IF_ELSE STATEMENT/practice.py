# year = int(input('Enter the year: '))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f'The {year} is the leap year')
# else:
#     print('Not a leap year')


# num = int(input('Enter the number: '))
# if num > 0:
#     print('Number is positive')
# elif num < 0:
#     print('Number is Negative')
# else:
#     print('Number is Zero')



a = int(input('Enter the number: '))
b = int(input('Enter the number: '))
c = int(input('Enter the number: '))

if (a > b and a < c) or (a < b and a > c ):
    print('The Middle Value is ',a)
elif (b > a and b < c) or (b < a and b > c ):
    print('The Middle Value is ',b)
else:
    print('The Middle Value is ',c)