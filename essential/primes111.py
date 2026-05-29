def isPrime(n, foundPrimes=None):
  foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
  for prime in foundPrimes:
    if n % prime == 0:
      return False
  return True

def listPrimes(num):
  foundPrimes = []
  for n in range(2, num):
    if isPrime(n, foundPrimes):
      foundPrimes.append(n)
  return foundPrimes

print(f'primes111.py module name is {__name__}')