"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    while len(list) < number_of_primes:
        if (isPrime(count)):
            list.append(count)
        count += 1
    return list

def isPrime(x):
    count = 0
    for i in range(1, x//2 + 1):
        if x % i == 0:
            count += 1
    if (count == 1):
        return True
    else:
        return False