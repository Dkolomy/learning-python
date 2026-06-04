# Your goal is to implement a function, get_prime_factors(), that takes an integer value as the input argument 
# and returns a list containing all of its prime factors.

def get_prime_factors(n):
  factors = []
  for i in range(2, n+1):
    print(i, n, n % i)
    while n % i == 0:    # if n is divisible by i, then i is a factor of n
      print("stored", i)
      factors.append(i)
      # This line updates n by dividing it by the current prime factor i
      n = n // i
      # print(n)
  return factors

print(get_prime_factors(630))
print(get_prime_factors(13))

