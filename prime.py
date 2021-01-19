import math as m

def SievePrimes(n):
    """
    Sieve of Eratosthenes.
    Input: integer n > 1.
    Output: list of prime numbers from 2 to n.
    """
    integers = list(range(2,n+1))
    i=0
    while integers[i] <= m.floor(n**0.5):
            multiples = list(range(2*integers[i],n+1,integers[i]))
            integers = [x for x in integers if x not in multiples]
            i += 1
    else:
        return integers
        print(integers)

def SievePrimeCount(x):
    """
    Input: integer n > 1.
    Output: number of primes less than or equal to n.
    """
    return len(SievePrimes(x))
    print(len(SievePrimes(x)))

def TrialFactor(x):
    """
    Prime factorisation/testing by trial division.
    Input: integer n > 1.
    Output: prime factorisation of number if it is not prime.
    """
    n = x
    factors = []                                            #list of prime factors
    q = 2                                                   #first prime factor is 2
    while n != 1:
        if n%q == 0:                        
            factors.append(q)                               #if q divides x, then add it to the list of factors
            n = n/q                                         #divide down to find new factors
        else:
            q += 1                                          #if q does not divide x, then go to next number
    if factors == [x]:                                      #if x is only divisible by itself then it is prime
        print(x, 'is prime.')
    else:
        condensed = list(set(factors))                      #condensed list of non-repeating factors
        exponents = [factors.count(x) for x in condensed]   #list of exponents of corresponding factors
        print(x, '= ' , end = '')                           #print the prime factorisation of x
        k = 0
        while k < len(condensed)-1:
            print(f'{condensed[k]}^{exponents[k]}', end = ' * ')
            k += 1
        print(f'{condensed[len(condensed)-1]}^{exponents[len(exponents)-1]}.')
