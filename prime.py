import math as m
from datetime import datetime

def Eratosthenes(n: int) -> list:
    """
    Sieve of Eratosthenes.

    Input: integer n > 1.
    Output: list of prime numbers from 2 to n.
    """
    start = datetime.now()
    prime = [False, False] + [True]*(n-1)
    for i in range(2, m.floor(m.sqrt(n))+1):
        if prime[i]:
            for j in range(i**2, n+1, i):
                prime[j] = False

    prime_numbers = []
    for i in range(0, n+1):
        if prime[i]:
            prime_numbers.append(i)    

    elapsed = datetime.now() - start
    print(f"Computation time: {elapsed.total_seconds() * 1000.0:.2f} ms")
    return prime_numbers

def sieve(integer, sieve_type=0):
    if sieve_type == 0:
        return Eratosthenes(integer)
    elif sieve_type == 1:
        print('Sieve of Sundaram')
    elif sieve_type == 2:
        print('Sieve of Atkin')

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
        print(f'{condensed[-1]}^{exponents[-1]}.')

def trial_division(n: int) -> list:
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 2
    if n != 1: 
        a.append(n)
    return a
