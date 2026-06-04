# Your goal is to implement a function, is_palindrome(), that takes a text string as the input argument 
# and returns a boolean indicating whether or not it's a palindrome.

import re

def is_palindrome(phrase):
  # This line creates a string 'forwards' which contains only the lowercase alphabetic characters from the input phrase, concatenated together.
  # It uses a regular expression to find all sequences of one or more consecutive lowercase letters after converting the phrase to lowercase.
  # The found sequences are joined together as one continuous string.
  forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
  # forwards = phrase.lower().replace(' ', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('"', '').replace("'", '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace(';', '').replace(':', '').replace('|', '').replace('\\', '').replace('/', '').replace('`', '').replace('~', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&', '').replace('*', '').replace('_', '').replace('-', '').replace('+', '').replace('=', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
  reverse = forwards[::-1]
  return forwards == reverse

print(is_palindrome("'hello world'"))
print(is_palindrome("(Go hang a salami, I\'m a lasagna hog."))

