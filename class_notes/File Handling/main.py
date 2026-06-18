# with open('emp.csv','w') as file:
#     file.write('ID,NAME,AGE,GENDER,SALARY\n')
#     file.writelines(['101,steve jobs, 30, male, 50000\n',
#                      '102,Bill Gates, 40, male, 60000\n'])

from time import sleep
from csv import reader,DictReader
with open('emps.csv','r') as file:
    rows = reader(file)
    header_row = next(rows)
    lst_emps = []
    for row in rows:
        lst_emps.append(row)

class Emp_data:
    def total_pay():
        Sum = 0
        for emp in lst_emps:
            Sum += int(emp[-4])
        return Sum

    print('Total Pay of Emp :', total_pay())


    def gender():
        Male = 0
        Female = 0
        for emp in lst_emps:
            if emp[2] == 'Male':
                Male += 1
            else:
                Female += 1
        return Male, Female

    print(gender())


    def emp_count_gender():
        gender = {}
        for emp in lst_emps:
            if emp in lst_emps:
                if emp[2] not in gender:
                    gender[emp[2]] = 1
                else:
                    gender[emp[2]] += 1
        return gender

    print(emp_count_gender())


    def emp_count_dept():
        emp_dept = {}
        for emp in lst_emps:
            if emp[3] not in emp_dept:
                emp_dept[emp[3]] = 1
            else:
                emp_dept[emp[3]] += 1
        return emp_dept

    print(emp_count_dept())


    lst_sorted_sal = sorted(lst_emps, key=lambda emp:int(emp[-4]))
    for emp in lst_sorted_sal:
        print(emp[1],emp[-4])

    lst_sorted_age = sorted(lst_emps, key=lambda emp:int(emp[6]))
    for emp in lst_sorted_age:
        print(emp[1],emp[6])



# Using DICT

# from csv import DictReader
# def emp_data(path):
#     lst_emps = [row for row in DictReader(open(path))]
#     return lst_emps

# file_path = r"C:\Users\91892\Downloads\emps.csv"

# lst_emps_data = emp_data(file_path)

# def count_city():
#     city_count = {}
#     for emp in lst_emps_data:
#         if emp in lst_emps_data:
#             if emp['City'] not in city_count:
#                 city_count[emp['City']] = 1
#             else:
#                 city_count[emp['City']] += 1
#     return city_count

# print(count_city())


with open('data.csv', 'w+') as file:
    file.write('Emp_ID,Name,Gender,Department,Designation,City,Age\n')
    file.writelines('101,Amit Sharma,Male,IT,Python Developer,Mumbai,26\n'
                    '102,Priya Mehta,Female,HR,HR Executive,Pune,29\n')
    file.seek(0)
    print(file.read())


with open('data.csv', 'r+') as file:
    print(file.read())
    # file.write('103,Yash,Male,IT,Python Developer,Mumbai,26\n') only reads the file and does not write because the pointer is at the end of the file after reading

with open('data.csv', 'a+') as file:
    print(file.read())
    file.write('103,Yash,Male,IT,Python Developer,Mumbai,26\n')


with open('user.csv','a+') as file:
    file.write('USENAME,PASSWORD\n')
    file.writelines(['steve jobs,steve123\n',
                    'Bill Gates,bill123\n'])
    file.seek(0)
    print(file.read())