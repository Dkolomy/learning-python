# class Dog:
#   _legs = 4
#   def __init__(self, name):
#     self.name = name

#   def get_legs(self):
#     return self._legs

#   def speak(self):
#     print(self.name + " says Woof!")

# my_dog = Dog("Rex")
# my_dog.speak()
# print(my_dog.get_legs())

# Static methods
# class WordSet:
#   replacePuncs = ['.', ',', '!', '?', '\'']
#   def __init__(self):
#     self.words = set()

#   def addText(self, text):
#     text = WordSet.cleanText(text)
#     for word in text.split():
#       self.words.add(word)

#   def cleanText(text):
#     # chain of replace methods
#     for punc in WordSet.replacePuncs:
#       text = text.replace(punc, '')
#     return text.lower()

# wordSet = WordSet()
# wordSet.addText("Hi, I\'m Dmitry! Here is a sentence I want to add to the set.")
# wordSet.addText("This is another sentence I want to add to the set.")

# print(wordSet.words)

# Decorators
class WordSet1:
  replacePuncs = ['.', ',', '!', '?', '\'']
  def __init__(self):
    self.words = set()

  def addText(self, text):
    text = self.cleanText(text)
    for word in text.split():
      self.words.add(word)

  @staticmethod
  def cleanText(text):
    # chain of replace methods
    for punc in WordSet1.replacePuncs:
      text = text.replace(punc, '')
    return text.lower()

wordSet = WordSet1()
wordSet.addText("Hi, I\'m Dmitry! Here is a sentence I want to add to the set.")
wordSet.addText("This is another sentence I want to add to the set.")

print(wordSet.words)
