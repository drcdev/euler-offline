import sys
from time import clock


def solve():
    list = []
    for x in xrange(100, 1000):
        for y in xrange(100, 1000):
            if str(x*y) == str(x*y)[::-1]:
                list.append(x*y)
    print max(list)


if __name__ == "__main__":
    t1 = clock()
    solve()
    t2 = clock()
    print "Runtime:", t2-t1
