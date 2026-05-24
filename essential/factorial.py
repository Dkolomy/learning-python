def factorial(n):
  if type(n) != int or n < 0:
    return None
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(1.33))

