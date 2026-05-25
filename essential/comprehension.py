# myList = [1, 2, 3, 4, 5]
# print([x * 2 for x in myList])

# myList = list(range(100))
# filteredList = [x for x in myList if x % 2 == 0]
# print(filteredList)

# myString = "My name is John. I live in Nashua, NH."
# print(myString.split('.'))

# print(myString.split())

# def cleanWord(word):
#   return word.replace('.', '').replace(',', '').replace(' ', '').lower()

# print([cleanWord(word) for word in myString.split()])

# Dictionary
animalList = [['a', 'aardvark'], ['b', 'bear'], ['c', 'cat']]
animalDict = {k: v for k, v in animalList}
print(animalDict)

print(animalDict.items())

print([{'letter': key, 'animal': value} for key, value in animalDict.items()])








