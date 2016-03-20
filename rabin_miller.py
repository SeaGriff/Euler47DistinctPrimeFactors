# Implements the RabinMiller primality test with the first seven primes. Provably correct for inputs < 3.4 * 10^14.

# Imports
import math

# CONSTANTS
PRIME_SET = {2,3,5,7,11,13,17}

# Counts the factors of two that divide the passed in input
def countFactorsOfTwo(x):
    result = 0
    while math.fmod(x,2) == 0:
        x /= 2.0
        result += 1
    return(result)

""" Checks to see if the input is prime.
Accepts: int x
Restrictions: 3.4 * 10^14 > x > 1 """

def isPrime(x):
    if x in PRIME_SET:
        return(True)
    for p in PRIME_SET:
        if x % p == 0:
            return(False)
    evenPower = int(countFactorsOfTwo(x - 1))
    oddFactor = int((x - 1) / 2**evenPower)
    for p in [prime for prime in PRIME_SET if prime < x]:
        if pow(p,oddFactor,x) == 1:
            return(True)
        for j in range(0,evenPower):
            if pow(p,(2**j)*oddFactor,x) == x-1:
                return(True)
    return(False)

""" Finds the next largest prime.
Accepts: int n
Restrictions: 3.4 * 10^14 > n > 0. May return a false positive for inputs greater than the least prime less
than 3.4 * 10^14
Returns: the least int p such that p > n """

def nextPrime(n):
    n += 1
    while not isPrime(n):
        n += 1
    return(n)