mySet = {1, 2, 3, 4, 5}
print(mySet)

mySet1 = set(['apple', 'banana', 'cherry'])
print(mySet1)

myList = ['d', 'b', 'c', 'a', 'c', 'd']
mySet2 = set(myList)
print(mySet2)

# Declared with curly braces {}
# All elements are unique
# The order doesn't matter

mySet2.add('orange')
print(mySet2)

print('a' in mySet2)
print('z' in mySet2)

print(len(mySet2))

mySet2.discard('a')
print(mySet2)

# Tuples
myTuple = ('cherry', 'apple', 'banana')
print(myTuple)

# Declared with parentheses ()
# Are ordered and "subscridable"
# Cannot be modified

# More efficient than lists
# They don't grow or change
# Store compactly in memory

a, b, c = myTuple # unpacking
print(b, c, a)










