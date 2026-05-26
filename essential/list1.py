myList = [1, 2, 3, 4, 5]
print(myList[3:]) # [4, 5]

# from index 0 to index 6 with step 2
print(myList[0:6:2]) # [1, 3, 5]
print(myList[::2]) # [1, 3, 5]

# print the numbers from 0 to 9
for i in range(10):
  print(i)
myList = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myList[::2]) # [0, 2, 4, 6, 8]
print(myList[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(myList[::-2]) # [9, 7, 5, 3, 1]

# Modify a list
myList = [1, 2, 3, 4, 5]
myList.append(6) # [1, 2, 3, 4, 5, 6]
print(myList)

myList.insert(1, 'new value') # [1, 'new value', 2, 3, 4, 5, 6]
print(myList)

myList.remove('new value') # [1, 2, 3, 4, 5, 6]
print(myList)

myList.pop() # [1, 2, 3, 4, 5]
print(myList)

myList.pop(1) # [1, 3, 4, 5]
print(myList)

while len(myList):
  print(myList.pop())
print(myList)

a = [1, 2, 3, 4, 5]
b = a
b.append(6)
print(a)
print(b)

a = [1, 2, 3, 4, 5]
b = a.copy()
b.append(6)
print(a)
print(b)
