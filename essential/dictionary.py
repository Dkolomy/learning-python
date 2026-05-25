# animal_sounds = {
#   'dog': 'woof',
#   'cat': 'meow',
#   'bird': 'tweet',
#   'cow': 'moo',
#   'pig': 'oink',
#   'horse': 'neigh',
#   'sheep': 'baa',
#   'goat': 'bleat',
#   'chicken': 'cluck',
#   'duck': 'quack',
#   'turkey': 'gobble',
# }
# print(animal_sounds)

# print(animal_sounds.keys())
# print(animal_sounds.values())

# print(animal_sounds.get('dog'))
# print(animal_sounds.get('dog', 'unknown'))
# print(animal_sounds.get('dog', 'unknown'))

# animals = {
#   'a': ['ant', 'aardvark'],
#   'b': ['bear', 'baboon', 'badger'],
# }

# print(animals)

# animals['b'].append('bison')

# animals['c'] = ['cat', 'cow', 'cat']

# print(animals)

# if 'd' not in animals:
#   animals['d'] = []
# animals['d'].append('dog')

# print(animals)

# Default Dictionary
from collections import defaultdict

animals = defaultdict(list, {})
print(animals)

animals['a'].append('ant')
animals['b'].append('bear')
print(animals['f'])