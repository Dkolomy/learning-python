# class Dog:
#   _legs = 4
#   def __init__(self, name):
#     self.name = name

#   def speak(self):
#     print(self.name + " says Woof!")

#   def getLegs(self):
#     return self._legs

# class Chihuahua(Dog):
#   def speak(self):
#     print(self.name + " says Yap Yap Yap!")

#   def wagTail(self):
#     print(self.name + " is wagging its tail!")
  

# dog = Chihuahua("Timka")
# dog.speak()
# dog.wagTail()
# print(dog.getLegs())

# Extending built-in classes
myList = list()

class UniqueList(list):

  def __init__(self):
    super().__init__()
    self.someProperty = "Unique List"

  def append(self, value):
    if value in self:
      return
    super().append(value)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(2)
uniqueList.append(3)
uniqueList.append(2)
print(uniqueList)