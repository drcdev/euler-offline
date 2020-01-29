import sys
from time import clock


def primeSieve(num):
    list = [i*2+1 for i in range(1, num/2)]
    primes = [2]
    p = 0
    while (p < num and len(list) > 0):
        p = list[0]
        for i in list:
            if i % p == 0:
                list.remove(i)
        primes.append(p)
    return primes


def primeFactors(num):
    if num == 1:
        return [1]
    primes = primeSieve(int(num**0.5) + 1)
    factors = []
    for p in primes:
        if p * p > num:
            break
        while num % p == 0:
            factors.append(p)
            num //= p
    if num > 1:
        factors.append(num)
    return factors


def solve():
    n = 20
    primes = primeSieve(n)
    factors = []
    product = 1
    for i in range(2, n+1):
        factors.append(primeFactors(i))
    for p in primes:
        max = 0
        for f in factors:
            if f.count(p) > max:
                max = f.count(p)
        for i in range(max):
            product *= p
    print product


if __name__ == "__main__":
    t1 = clock()
    solve()
    t2 = clock()
    print "Runtime:", t2-t1
