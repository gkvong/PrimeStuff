import math as m
from datetime import datetime

def Eratosthenes(n: int) -> list:
    """
    Sieve of Eratosthenes.
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

def Sundaram(n: int) -> list:
    """
    Sieve of Sundaram.
    """
    k = (n-2) // 2
    prime = [True]*(k+1)
    for i in range(1, k+1):
        j = i
        while i + j + 2*i*j <= k:
            prime[i + j + 2*i*j] = False
            j += 1
    
    prime_numbers = [2]
    for i in range(1, k+1):
        if prime[i]:
            prime_numbers.append(2*i + 1)
    return prime_numbers

def Atkin(limit: int) -> list:
    """
    Sieve of Atkin (Unoptimised).
    """
    sieve = [False]*(limit+1)
    
    for x in range(1, int(m.sqrt(limit))+1):
        for y in range(1, int(m.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n <= limit and n % 60 in {1, 13, 17, 29, 37, 41, 49, 53}:
                sieve[n] = not sieve[n]
            n = 3*x**2 + y**2
            if n <= limit and n % 60 in {7, 19, 31, 43}:
                sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x > y and n <= limit and n % 60 in {11, 23, 47, 59}:
                sieve[n] = not sieve[n]
    for x in range(7, int(m.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit+1, x**2):
                sieve[y] = False

    prime_numbers = [2,3,5]
    for i in range(7, limit):
        if sieve[i]:
            prime_numbers.append(i)
    return prime_numbers

def sieve(limit, sieve_type=1):
    """
    Prime number sieves. Returns a list of prime numbers up to and including the limit.
    
    limit: Integer greater than 1. Search limit for prime sieve.

    sieve_type: 1(default), 2 or 3. Specify the type of sieve to use:
    '1' for Sieve of Eratosthenes,
    '2' for Sieve of Sundaram,
    '3' for Sieve of Atkin.
    
    """
    if sieve_type == 1:
        start = datetime.now()
        primes = Eratosthenes(limit)
        end = datetime.now() - start
    elif sieve_type == 2:
        start = datetime.now()
        primes = Sundaram(limit)
        end = datetime.now() - start
    elif sieve_type == 3:
        start = datetime.now()
        primes = Atkin(limit)
        end = datetime.now() - start
    
    print(primes)
    print(f"Computation time: {end.total_seconds() * 1000.0:.2f} ms")


def trial_division(n: int) -> list:
    """
    Trial division prime factorisation.
    """
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

def factor(integer, method=1):
    """
    Prime factorisation algorithms. Returns the prime factorisation of a number in exponential form.
    
    integer: number to prime factorise.

    method: 1(default), 2 or 3. Specify the prime factorisation algorithm to use:
    '1' for Trial division,
    '2' for Fermat's factorisation method.
    '3' for Pollard's rho algorithm,
    '4' for Quadratic sieve method,
    '5' for Shor's algorithm.
    """
    if method == 1:
        start = datetime.now()
        factors = trial_division(integer)
        end = datetime.now() - start
    elif method == 2:
        start = datetime.now()
        print('Fermat\'s factorization method')
        end = datetime.now() - start
    elif method == 3:
        start = datetime.now()
        print('Pollard\'s rho algorithm')
        end = datetime.now() - start
    elif method == 4:
        start = datetime.now()
        print('Quadratic Sieve Method')
        end = datetime.now() - start
    elif method == 5:
        start = datetime.now()
        print('Shor\'s Algorithm')
        end = datetime.now() - start

    if len(factors) == 1: 
        print(integer, 'is prime.')
    else:
        factorise = dict()
        for i in factors:
            factorise[i] = factorise.get(i ,0) + 1

        print(integer, '= ', end = '')
        for key, value in factorise.items():
            if key == list(factorise.keys())[-1]:
                if value == 1:
                    print(f'{key}.')
                else:
                    print(f'{key}^{value}.')
            elif value == 1:
                print(f'{key}', end = ' * ')
            else:
                print(f'{key}^{value}', end = ' * ')
    print(f"Computation time: {end.total_seconds() * 1000.0:.2f} ms")
