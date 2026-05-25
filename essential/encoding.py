# Python code​​​​​​‌‌‌‌‌​‌‌​​​​‌‌‌‌‌​‌​‌​​​‌ below

# def encodeString(stringVal):
#     # Your code goes here.
#     pass

# def decodeString(encodedList):
#     # Your code goes here.
#     pass

myString = "AAAABBBAACCCCCCDDDDAA"
myString = list(myString)

mask = myString[0]
encodedList = []
count = 0
for i in range(len(myString)):
  if myString[i] == mask:
    count += 1
  else:
    encodedList.append((mask, count))
    mask = myString[i]
    count = 1
encodedList.append((mask, count))
print(encodedList)

decodedString = ''
for mask, count in encodedList:
  decodedString += mask * count
print(decodedString)



# def encodeString(stringVal):
#   encodedList = []
#   while len(stringVal):
#     encodedList.append(stringVal.pop())
#   return encodedList

# def decodeString(encodedList):
#   return ''.join(encodedList)

# print(encodeString(myString))
# print(decodeString(encodeString(myString)))
