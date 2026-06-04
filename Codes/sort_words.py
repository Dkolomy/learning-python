# Your goal is to implement a function, sort_words(), that takes a string containing one or more words separated by spaces as the input argument 
# and returns a string containing those words sorted alphabetically.

def sort_words(words):
  return ' '.join(sorted(words.split(), key=str.casefold))  
  # return ' '.join(sorted(words.split(), key=str.lower))  
  # return ' '.join(sorted(words.split(), key=lambda x: x.lower()))  

print(sort_words("string of words"))
print(sort_words("Banana Orange apple"))
print(sort_words("Apple banana orange"))
print(sort_words("orange Banana apple"))
print(sort_words("apple banana orange"))