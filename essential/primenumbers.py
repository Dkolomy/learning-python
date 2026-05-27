# Python code​​​​​​‌‌‌‌‌​‌‌​​​‌‌‌‌​‌​​​‌​​‌​ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    # Your code goes here.
    primes = [2]
    for number in range(3, num):
      num = number ** 0.5
      for prime in primes:
        if number % prime == 0:
          break;
      else:
        primes.append(number)
    return primes

      # for i in range(2, int(number**0.5) + 1):
      #   if number % i == 0:
      #     break;
      # else:
      #   print(number)

print(allPrimesUpTo(100))