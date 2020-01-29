import sys
from time import clock


def solve():
    sumOfSqr = 0
    sqrOfSum = 0
    for i in range(1, 100+1):
        sumOfSqr += i*i
        sqrOfSum += i
    sqrOfSum = sqrOfSum * sqrOfSum
    print "Sum of squares:", sumOfSqr
    print "Square of sums:", sqrOfSum
    print "Difference:    ", sqrOfSum-sumOfSqr


if __name__ == "__main__":
    t1 = clock()
    solve()
    t2 = clock()
    print "Runtime:", t2-t1
