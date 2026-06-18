class Trainer:
    Trainer_name = 'Mr.Yallesh'
    sub = 'Python'
    def req_annoucemnet(self):
        print('VS2 SOLUTIONS')
        print('skill : Python, SQL')
        print('Salary : 30k Per Month')

class Batch_A8(Trainer):
    Time = '2pm to 4pm'
    Batch_type = 'Regular'
    number_std = 20
s1 = Batch_A8()

class Batch_E1(Trainer):
    Time = '7pm to 9pm'
    Batch_type = 'Regular'
    number_std = 15
s2 = Batch_E1()

class Batch_A1(Trainer):
    Time = '9am to 12pm'
    Batch_type = 'Regular'
    number_std = 30
s3 = Batch_A1()

print(s1.Trainer_name)
print(s2.Time)
print(s3.req_annoucemnet())