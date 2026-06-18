import json

with  open('users.json', 'w+') as file:
    data = file.read()
    py_data = json.loads(data)
    print(py_data["uname"])