# mySet = {'apple', 'banana', 'cherry'}
# print(mySet)

# mySet = set(['apple', 'banana', 'cherry'])
# print(mySet)

myList = [
  'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry'
]
mySet = set(myList)
# myList = list(set(myList))
# print(myList)

# mySet.add('orange')
# print(mySet)

# print("orange" in mySet)

# while len(mySet):
#   print(mySet.pop())

print(mySet)
mySet.discard('apple')
print(mySet)

# Tuples
myTuple = ('apple', 'banana', 'cherry') # not be able to change the values

a, b, c = myTuple
print(a, b, c)