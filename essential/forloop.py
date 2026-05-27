myList = [1, 2, 3, 4, 5]
for item in myList:
  print(item)

print('======================')

# Pass
animalLookup = {
  'a': ['ant'],
  'b': ['bear', 'baboon', 'badger'],
  'c': ['cat', 'cow', 'cat'],
}

# for letter in animalLookup:
#   print(letter)
#   print(animalLookup[letter])

# print('======================')

# for letter, animals in animalLookup.items():
#   if len(animals) > 1:
#     continue
#   print(f'{letter} is a {animals}')

# print('======================')

# For/Else
# for number in range(2, 100):
#   for i in range(2, int(number**0.5) + 1):
#     if number % i == 0:
#       break;
#   else:
#     print(f'{number} is a prime number')

# print('======================')

for number in range(2, 100):
  found_factor = False
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      found_factor = True
      break;
  if not found_factor:
    print(f'{number} is a prime number')

