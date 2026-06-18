class PassWordError(Exception):
    pass

pwd = 'Py@123'
Password = input('Enter the Password : ')
if Password == pwd:
    print("Hello!!!")
else:
    raise PassWordError('Wrong password!!!')