# Your goal is to implement a function, count_words(), that takes the path to a text file 
# as the input argument and prints the total number of words in the file, 
# as well as the top 20 most frequently used words and how many times each of them occurs.

# The 're' module provides support for regular expressions in Python.
# It allows us to search, match, and manipulate string patterns.
import re

# The 'collections' module provides specialized container datatypes beyond the built-in types.
# In this script, we'll likely use 'collections.Counter' to count word frequencies in the text file.
import collections

def count_words(path):
  # Open the file in read mode
  with open(path, 'r', encoding='utf-8') as file:
    # Read the file content
    content = file.read()
    # Use regular expression to find all words in the content
    words = re.findall(r"[0-9a-zA-Z-']+", content)
    # Use Counter to count the frequency of each word
    word_counts = collections.Counter(words)
    # Print the total number of words
    print(f"Total number of words: {len(words)}")

    # Print the top 20 most frequently used words and how many times each of them occurs
    for word, count in word_counts.most_common(20):
      print(f"{word}: {count}")

count_words("shakespeare.txt")