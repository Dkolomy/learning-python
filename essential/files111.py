# Read a file

# f = open('justText.txt', 'r')
# for line in f.readlines():
#   print(line.strip())
# f.close()

# Write to a file
# f = open('justText.txt', 'w')
# f = open('justText.txt', 'a')
# f.write('This is a new line 3\n')
# f.write('This is a new line 4\n')
# f.close()

with open('justText.txt', 'a') as f:
  f.write('This is a new line 5\n')
  f.write('This is a new line 6\n')


