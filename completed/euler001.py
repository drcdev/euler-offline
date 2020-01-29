import hashlib
import hash
import sys
from time import perf_counter


def solve():
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == "__main__":
    t1 = perf_counter()
    hash.printHash(str(solve()))
    t2 = perf_counter()
    print("Runtime:", t2-t1)
