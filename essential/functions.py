# def performOperation1(a, b, operation='add'):
#   if operation == 'add':
#     return a + b
#   elif operation == 'subtract':
#     return a - b
#   elif operation == 'multiply':
#     return a * b
#   elif operation == 'divide':
#     return a / b
#   else:
#     return None

# print(performOperation1(1, 2))
# print(performOperation1(1, 2, 'subtract'))

# def performOperation2(*args):
#   print(args)

# performOperation2(1, 2, 3, 4, 5)

# def performOperation3(*args, **kwargs):
#   print(args, kwargs)

# performOperation3(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5)

# import math

# def performOperation4(*args, operation='sum'):
#   if operation == 'sum':
#     return sum(args)
#   elif operation == 'multiply':
#     return math.prod(args)
#   else:
#     return None

# print(performOperation4(1, 2, 3, 4, 5))
# print(performOperation4(1, 2, 3, 4, 5, operation='multiply'))

# # locals()
# def performOperation5(num1, num2, operation='sum'):
#   return locals()

# print(performOperation5(1, 2))
# print(performOperation5(1, 2, operation='multiply'))

# globals()
# print(globals())

# message = "Hello, World!"

# def function1(varA, varB):
#   print(message)
#   print(locals())

# def function2(varC, varD):
#   print(message)
#   print(locals())

# function1(1, 2)
# function2(3, 4)

# def function3(varA, varB):
#   massage1 = "DK"
#   print(varA)
#   def inner_function3(varA, varB):
#     print(f"inner_function3 local scope: {locals()}")

#   print(f"function3 local scope: {locals()}")
#   inner_function3(5, 6)

# function3(7, 8)

# function chaining
# def lowercase(text):
#   return text.lower()

# def removePunctuation(text):
#   punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#   for p in punctuation:
#     text = text.replace(p, '')
#   return text

# def removeNewlines(text):
#   text = text.replace('\n', ' ')
#   return text

# def removeShortWords(text):
#   return '',join(word for word in text.split() if len(word) > 3)

# def removeLongWords(text):
#   return '',join(word for word in text.split() if len(word) < 6)

# processingFunctions = [lowercase, removePunctuation, removeNewlines, removeShortWords, removeLongWords]
# for func in processingFunctions:
#   text = func(text)

# print(text)

# Lambda functions
(lambda x: x + 3)(2)
print((lambda x: x + 3)(2))

myList = [5, 4, 3, 2, 1]
print(list(map(lambda x: x + 3, myList)))

print(sorted(myList, reverse=False))

myDict = [{'num': 3}, {'num': 1}, {'num': 2}]
print(sorted(myDict, key=lambda x: x['num']))


