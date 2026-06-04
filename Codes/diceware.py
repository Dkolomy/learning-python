# Your goal is to implement a function, generate_passphrase(), that takes the number of words to include 
# in the password as the input argument and returns a string containing a sequence of randomly selected 
# words from the Diceware list separated by spaces.

# The 'secrets' module provides functions for generating cryptographically strong random numbers
# suitable for managing data such as passwords and account authentication, which makes it preferable
# over the 'random' module for security-sensitive applications like passphrase generation.
import secrets

def generate_passphrase(num_words, wordlist_path="diceware.wordlist.asc"):
  print(f"Generating a {num_words}-word passphrase...")
  with open(wordlist_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()[2:7778]
    word_list = [line.split()[1] for line in lines]

  words = [secrets.choice(word_list) for _ in range(num_words)]
  return ' '.join(words)

print(generate_passphrase(7))
print(generate_passphrase(7))