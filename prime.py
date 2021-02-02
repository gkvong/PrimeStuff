import math as m
from datetime import datetime

def Eratosthenes(n: int) -> list:
    """
    Sieve of Eratosthenes.

    Input: integer n > 1.
    Output: list of prime numbers from 2 to n.
    """
    prime = [True]*(n+1)
    for i in range(2, m.floor(m.sqrt(n))+1):
        if prime[i]:
            for j in range(i**2, n+1, i):
                prime[j] = False

    prime_numbers = []
    for i in range(2, n+1):
        if prime[i]:
            prime_numbers.append(i)
    return prime_numbers

def sieve(integer, sieve_type=0):
    if sieve_type == 0:
        start = datetime.now()
        primes = Eratosthenes(integer)
        end = datetime.now() - start
    elif sieve_type == 1:
        print('Sieve of Sundaram')
    elif sieve_type == 2:
        print('Sieve of Atkin')
    
    print(primes)
    print(f"Computation time: {end.total_seconds() * 1000.0:.2f} ms")

def trial_division(n: int) -> list:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n /= f
        else:
            f += 2
    if n != 1: 
        factors.append(int(n))
    return factors

def factor(integer, method=0):
    if method == 0:
        start = datetime.now()
        factors = trial_division(integer)
        end = datetime.now() - start
    elif method == 1:
        print('Fermat\'s factorization method')
    elif method == 2:
        print('Pollard\'s rho algorithm')
    elif method == 3:
        print('Quadratic Sieve Method')
    elif method == 4:
        print('Shor\'s Algorithm')

    if len(factors) == 1: 
        print(integer, 'is prime.')
    else:
        condensed = list(set(factors))
        exponents = [factors.count(x) for x in condensed]
        print(integer, '= ' , end = '')
        k = 0
        while k < len(condensed)-1:
            print(f'{condensed[k]}^{exponents[k]}', end = ' * ')
            k += 1
        print(f'{condensed[-1]}^{exponents[-1]}.')

    print(f"Computation time: {end.total_seconds() * 1000.0:.2f} ms")
