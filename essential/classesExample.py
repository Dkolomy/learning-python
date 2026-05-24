class Dog:
  def __init__(self, name):
    self.name = name
    self.legs = 4

  def speak(self):
    print(self.name + " says Woof!")

my_dog = Dog("Rex")
another_dog = Dog("Buddy")

my_dog.speak()
another_dog.speak()