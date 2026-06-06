# 40 Python's "magic methods" can help you do which three things?
# - define how objects are represented as strings               - via __str__ and __repr__
# - control access to gettingand setting attribute values       - via __getattr__ and __setattr__
# - bypass the operating system when logging in new users
# - customize object behaviour and integrate with the language  - via __len__(), __iter__(), __add__()
# - ignore comparison and testing capabilities
# - restrict objects from being called like functions +

# ----------------------

# 41 CVS file values separated by tabs? How I parse it?
# import csv
# with open('data.csv', 'r') as file:
#   reader = csv.reader(file, delimiter='\t')  +
#   for row in reader:
#     print(row)


# ----------------------

# 42 What is result of: '1' + '3'
# '13' + 

# ----------------------

# 43 What is result:
# for index in range(0,10):
#   if index % 2 == 0:
#     print(index)

# 0 2 4 6 8 +

# ----------------------

# 44 How would you make a data class immutable?
# use frozen=True in the data class decorator +
# ----------------------

# 45 What is result of this code
# for column in range(0,5):
#   for row in range(0,5):
#     if column + row % 2 == 0:
#       break
#   else:
#     print(f'{column} {row}')

# 4
# 1 4
# 2 4
# 3 4
# 4 4

# ----------------------

# 46 You program needs to store small collection of related data that won't be changed. Which data type would you use?
# tuple +

# ----------------------

# 47 result of this code:
# import threading
# import time

# def eventNumbers(n, results):
#   time.sleep(1)
#   if n % 2 == 0:
#     results[n] = True
#   else:
#     results[n] = False

# results = {}
# threadPool = [threading.Thread(target=eventNumbers, args=(n, results)) for n in range(0, 27)]
# [t.start() for t in threadPool]
# [t.join() for t in threadPool]
# print(results)

# 26 False +

# ----------------------

# 48 How would you look up the ID 73 in this dictionary?
# ????????????

# ----------------------

# 49

# ----------------------

# 50 your coworker shows you a new base exception class they've written. What, if anything is wrong with this code?
# class CustomException(Exception):
#   description = None
#   id = None

#   def __init__(self):
#     super().__init__(f"Custom Exception {self.id}: {self.description}")

# Nothing +

# 7 of 11