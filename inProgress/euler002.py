import sys
from time import clock


def solve():
    sum = 0
    x = 1
    y = 1
    while(y < 4000000):
        if y % 2 == 0:
            sum += y
        z = y
        y = x + y
        x = z
    print sum


if __name__ == "__main__":
    t1 = clock()
    solve()
    t2 = clock()
    print "Runtime:", t2-t1
