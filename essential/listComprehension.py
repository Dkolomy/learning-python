myList = [1, 2, 3, 4, 5]
newList = [2 * item for item in myList]
print(newList)

myList = list(range(100))
filteredList = [x for x in myList if x % 10 == 0]
print(filteredList)

filteredList = [x for x in myList if x % 10 < 3]
print(filteredList)

myString = "My name is John. I live in Nashua, NH."
words = myString.split('.')
print(words)

def cleanWord(word):
  return word.replace('.', '').lower()

print([cleanWord(word) for word in myString.split()])

print([cleanWord(word) for word in myString.split() if len(word) < 3])