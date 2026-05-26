animals = {
  'a': 'ant',
  'b': 'bear',
  'c': 'cat',
  'd': 'dog',
  'e': 'elephant',
  'f': 'fox',
  'g': 'giraffe',
  'h': 'hippo',
  'i': 'iguana',
  'j': 'jaguar',
  'k': 'kangaroo',
  'l': 'lion',
  'm': 'monkey',
}

print(animals['a'])

print(animals.keys())
print(animals.values())
print(animals.items())

print(list(animals.keys()))
print(list(animals.values()))
print(list(animals.items()))

print(animals.get('z', 'unknown'))
print(animals.get('w'))

if 'z' not in animals:
  animals['z'] = 'zebra'
print(animals)

animals['z'] = 'zebra'
print(animals)

# Default Dictionary
import from collections import defaultdict

animals1 = defaultdict(list, {})

animals1['a'].append('ant')