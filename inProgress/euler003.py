import sys
import math
from time import clock


def solve():
    n = 600851475143
    factors = [x for x in range(2, int(math.sqrt(n))) if n % x == 0]
    i, j = 0, len(factors) - 1
    while j > i:
        if factors[j] % factors[i] == 0:
            i, j = 0, j-1
        else:
            i += 1
    print factors[j]


if __name__ == "__main__":
    t1 = clock()
    solve()
    t2 = clock()
    print "Runtime:", t2-t1
