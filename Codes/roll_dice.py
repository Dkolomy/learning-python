# Your goal is to implement a function, roll_dice(), that takes a variable number of input arguments 
# representing the number of sides on an arbitrary number of dice, its and its output should print 
# a table of the probability for each possible outcome.

from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):
  total_roll_counts = Counter()
  for _ in range(num_trials):
    total_roll = sum((randint(1, sides) for sides in dice))
    total_roll_counts[total_roll] += 1
  
  print('Total Roll Probability from {num_trials} rolls:')
  for outcome in range(len(dice), sum(dice) + 1):
    print(f'{outcome}: {total_roll_counts[outcome] / num_trials:.2%}')

roll_dice(4, 6, 6)
roll_dice(4, 6, 6, 20)