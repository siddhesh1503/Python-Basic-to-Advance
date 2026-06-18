# class Point:
#     a = 1
#     b = 2
#     def add(x,y):
#         return x+y

# p1 = Point()
# p2 = Point()
# # print(dir(p1))
# # print(Point.add(2,3))

# print(Point.a)
# print(Point.b)
# print(p1.a,p1.b)
# print(p2.a,p2.b)

# Point.a = 23
# Point.b = 45

# print(Point.a)
# print(Point.b)
# print(p1.a,p1.b)
# print(p2.a,p2.b)


# class Bank:
#     bname = 'SBI'
#     mbl = 'Mumbai'
#     ceo = 'Mr. Siddhesh'

# c1 = Bank()
# c1.name = 'Steve'
# c1.Account_num = 'SBI122342'
# c1.balance = 20000

# print(c1.name)
# print(c1.Account_num)
# print(c1.balance)
# print(c1.ceo)

# c2 = Bank()
# c2.name = 'Bill'
# c2.Account_num = 'SBI1231234'
# c2.balance = 234234
# print(c2.name)
# print(c2.Account_num)
# print(c2.balance)

# c3 = Bank()

# Bank.ceo = 'Hitesh'
# print(c1.ceo)
# print(c2.ceo)
# print(c3.ceo)

# Bank.ceo = 'Pushpa'
# print(c1.ceo)
# print(c2.ceo)
# print(c3.ceo)

#Create a class with 5 class members and 5 object members and minimum 4 object creations

# class members:
#     name = 'Siddhesh'
#     phone_no = 23423894234
#     email = 'siddheshshinde232@gmail'
#     Id_no = 23
#     gender = 'Male'

# c1 = members()
# c1.ename = 'Shivam'
# c1.ephone_no = 2342345235
# c1.eemail = 'shivam@gmail.com'
# c1.eId_no = 22
# c1.egender = 'Male'

# c2 = members()
# c2.ename = 'Satish'
# c2.ephone_no = 3434455235
# c2.eemail = 'satis@gmail.com'
# c2.eId_no = 20
# c2.egender = 'Male'

# c3 = members()
# c3.ename = 'Vishal'
# c3.ephone_no = 6666666666
# c3.eemail = 'vishal@gmail.com'
# c3.eId_no = 20
# c3.egender = 'Female'

# c4 = members()
# c4.ename = 'Prachi'
# c4.ephone_no = 64534534643
# c4.eemail = 'Prachi@gmail.com'
# c4.eId_no = 25
# c4.egender = 'Female'

# c5 = members()
# c5.ename = 'Saujanya'
# c5.ephone_no = 5243545345
# c5.eemail = 'sauju@gmail.com'
# c5.eId_no = 24
# c5.egender = 'Female'


class members:
    name = 'Siddhesh'
    phone_no = 23423894234
    email = 'siddheshshinde232@gmail'
    Id_no = 23
    gender = 'Male'
    def __init__(self,name,phone,email,id,gender):
        self.name = name
        self.phone = phone
        self.email = email
        self.Id = id
        self.gender = gender

c1 = members('Siddhesh',2384982374,'sid@gmail.com',45,'male')
print(c1.__dict__)
c2 = members('Satish',6534534523,'satis@gmail.com',78,'male')
print(c2.__dict__)
c3 = members('Shivam',859952374,'shivam@gmail.com',44,'male')
print(c3.__dict__)
c4 = members('Vishal',577882374,'vishal@gmail.com',88,'male')
print(c4.__dict__)
# c5 = members()

# members.__init__(c1,'Siddhesh',2384982374,'sid@gmail.com',45,'male')
# print(c1.__dict__)
# members.__init__(c2,'Satish',6534534523,'satis@gmail.com',78,'male')
# print(c2.__dict__)
# members.__init__(c3,'Shivam',859952374,'shivam@gmail.com',44,'male')
# print(c3.__dict__)
# members.__init__(c4,'Vishal',577882374,'vishal@gmail.com',88,'male')
# print(c4.__dict__)
# members.__init__(c5,'Prachi',3455982374,'prachi@gmail.com',99,'male')
# print(c5.__dict__)

