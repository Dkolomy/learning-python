# 30 assuming that data.txt ia s multiline file, how will this code print out the file text?
# newFile = open('data.txt', 'r')
#   for line in newFile.readlines():
#     print(line.strip())
# without leading and trailing whitespace     +

# ----------------------

# 31 what will be printed?
# url = 'Zeke78/JDMan/Amiry_007/535KevinWins/gretta/XAVIER1'

# result = url.split('/')
# print(result)
# result = [w.lower() for w in result]
# print(result)
# result.sort()
# print(result)
# result = ' '.join(result)
# print(result)
# 535kevinwins amiry_007 gretta jdman xavier1 zeke78 -

# ----------------------

# 32 Your team is building RSVP app where users can create, add and update
# invites =["John", "Nancy", "Raj", "Yelena"]
# print(invites)
# # ['John', 'Nancy', 'Raj', 'Yelena']
# invites.append("Sofia")
# # ['John', 'Nancy', 'Raj', 'Yelena', 'Sofia']
# invites.insert(2, "Youself")
# # ['John', 'Nancy', 'Youself', 'Raj', 'Yelena', 'Sofia']
# invites.remove("Nancy")
# # ['John', 'Youself', 'Raj', 'Yelena', 'Sofia']


# print(invites)
# ['John', 'Youself', 'Raj', 'Yelena', 'Sofia'] -

# ----------------------

# 33 What happens to the CSV header values when this code runs?
# import csv
# with open('data.csv', 'r') as data:
#   reader = csv.DictReader(data)
#   for row in data:
#     print(row)
# The header row is automatically consumed by csv.DictReader and used as dictionary keys - 

# ----------------------

# 34 what type is decodedData when  this code runs?
# import json
# result = '{"John": "2412", "Joan": "7221", "Devi": "4357"}'
# decodedData = json.loads(result)
# print(type(decodedData))
# Dictionary -

# 35 how wood yiu changevthe score for Player 3 to 1000?
# scores = {'Player 1': 700, 'Player 2': 101, 'Player 3': 23}
# scores['Player 3'] = 1000 +

# print(scores)
# {'Player 1': 700, 'Player 2': 101, 'Player 3': 1000} -

# ----------------------

# 36 Quiz app. Questions/answers, if question and answer are both true.
# question = True
# answer = True
# print(question == answer)
# True +

# ----------------------

# 37 You've just converted an object in your project into a data class. Now you wantadditional object initializationbut data classes
# automate the __init__ function. How solve this problem
# use __post_init__ -

# ----------------------

# 38 ___ classes support default values right out of the box?
# data classes -

# ----------------------

# 39 result of this code:
# firstName = "Johnny Appleseed"
# username = firstName[:8]
# print(username)
# Johnny A +

# ----------------------



