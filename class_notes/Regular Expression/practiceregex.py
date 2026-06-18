from re import findall
st ="9876543210,2323424134,1234567890,9876543211"
print(findall(r'[6-9]\d{9}',st))

email = "asdb@gmail.com, asdb@.com, asdb@gmail,"
print(findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',email))


__formats = ['00:00:00', '23:59:59', '24:00:00', '14:59:20', '12:9:10', '10:20:8']
for format in __formats:
    print(findall(r'\b(?:[0-1]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)\b',format))