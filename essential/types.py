from decimal import Decimal, getcontext

print(int('100'))
print(int('100', 2))

print(Decimal(100))
getcontext().prec = 4
getcontext()
print(Decimal(1) / Decimal(3))

getcontext().prec = 2
print(Decimal(1) / Decimal(3))

print(Decimal(3.14))

# ------------------
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('Hello'))
print(bool(None))
print(bool(100))
print(bool(0.0))
print(bool(''))
print(bool('Hello'))
print(bool(None))

myList1 = []
myList2 = [1, 2, 3, 4, 5]
myDict1 = {}
myDict2 = {'name': 'John', 'age': 30, 'city': 'New York'}

print("myList1 is empty: ", bool(myList1))
print("myList2 is empty: ", bool(myList2))
print("myDict1 is empty: ", bool(myDict1))
print("myDict2 is empty: ", bool(myDict2))
# ------------------
