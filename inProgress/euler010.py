import sys
from time import clock

def mark(primes, p):
	for i in xrange(2*p, len(primes), p):
		primes[i] = False

def solve():
	num = 10
	if len(sys.argv) > 1:
		num = int(sys.argv[1])
	primes = [True] * num
	for p in xrange(2, int(len(primes) ** 0.5) + 1):
		if primes[p]: mark(primes, p)
	print sum(i for i in xrange(2, len(primes)) if primes[i])

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
