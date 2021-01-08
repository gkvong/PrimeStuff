import math as m

def sieve(n):
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

def pcount(x):
    """
    Input: integer n > 1.
    Output: number of primes less than or equal to n.
    """
    return len(sieve(x))
    print(len(sieve(x)))

def factor(x):
    """
    Prime factorisation/testing by trial division.
    Input: integer n > 1.
    Output: prime factorisation of number if it is not prime.
    """
    n = x
    factors = []                            #list of prime factors
    q = 2                                   #first factor is 2
    while x != 1:
        if x%q == 0:                        
            factors.append(q)               #if q divides x, then add it to the list of factors
            x = x/q                         #divide down to find new factors
        else:
            q += 1                          #if q does not divide x, then go to next number
    if factors == [n]:                      #if x is only divisible by itself then it is prime
        print(n, 'is prime.')
    else:
        condense = []                       #condensed list of non-repeating factors
        exponents = []                      #list of exponents of corresponding factors
        i = 0
        while i <= len(factors)-1:
            condense.append(factors[i])     #add unique factors to list condensed list of factors
            sup = factors.count(factors[i]) #count number of repeating factors
            exponents.append(sup)           #add number to list of exponents
            i = i + sup                     #skip over repeated factors in factor list
        else:                               #print the prime factorisation of x
            print(n, '= ' , end = '')
            k = 0
            while k < len(condense)-1:
                print('{}^{}'.format(condense[k], exponents[k]), end = ' * ')
                k += 1
            print('{}^{}.'.format(condense[len(condense)-1], exponents[len(exponents)-1]))
