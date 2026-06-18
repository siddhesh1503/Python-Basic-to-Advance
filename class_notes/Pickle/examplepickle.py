import pickle

data = {"uname":"Shivam", "password" : "shivam@123"}
by_data = pickle.dumps(data)
with open('emp.json', "wb+") as file:
    file.write(by_data)
    file.seek(0)
    bi_data = file.read()
    py_data = pickle.loads(bi_data)
    print(py_data)