# 20 what priority, if any, is set on all events executed from this function?
# import shed, time
# def executeEvent(function, *args):
#   s = scheduler(time.time, time.sleep)
#   s.enterabs(time.time() + 1, 1, function, argument=args)
#   s.run()

# 1 -

# ----------------------

# 21 what if anything is wrong with this code?
# import csv
# with open('data.csv', 'r') as file:
#   for row in data:
#     print(row)

# reader = cvs.reader(file) -
# for row in reader:

# ----------------------

# 22 What eturn True
# (bool(-1)), (bool(100)), (bool(1)), (bool(0)), (bool('')), (bool(None))
# - (bool(-1)) - True
# - (bool(100)) - True
# - (bool(1)) - True
# - (bool(0)) - False
# - (bool('')) - False
# - (bool(None)) - False - 

# ----------------------

# 23 which function call ed when a new class instance is created?
# __init__ +

# ----------------------

# 24 if anything wrong with this code?
# class User:
#   def __init__(self, id):
#     self.id = id

# class Employee(User):
#   def __init__(self, id, name):
#     self.id = id
#     self.name = name

# super().__init__() is not called — Employee +
 
# ----------------------

# 25 when using a try/catch statement is it always necessary to specify an except block?
# No +

# ----------------------

# 26 overriding which of these methods automatically makes object sortable?
# __lt__ -

# ----------------------

# 27 what will be printed?
# class User:
#   def __init__(self, name):
#     self.name = name

# user1 = User("Brandon")
# user2 = User('Devi')

# print(isinstance(user1, object))
# print(isinstance(user2, type))
# True False +

# ----------------------

# 28 when it comes to the program you've writing on your computer, the operation responsible for ___ to ___ process that running
#ill the blank with one of the following options:
# (allocating memory; the first) - allocating memory; the first
# (allocating memory; each) - allocating memory; each                    <---- +
# (streaming data; the most recent) - streaming data; the most recent
# (streaming data; the last) - streaming data; the last

# ----------------------

# 29 What wrong with that code?
# from abc import ABC, abstractmethod

# class User(ABC):
#   def __init__(self):
#     super().__init__()

#   @abstractmethod
#   def debug(self):
#     pass

# class Employee(User):
#   def __init__(self):
#     print("Employee")

# Employee does not implement the abstract method debug() +

# 5 of 10

