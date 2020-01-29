import sys
from time import clock

def pSieve(max):
	nlist = [True] * max
	nlist[0] = False
	nlist[1] = False
	for i in xrange(2, max):
		if nlist[i]:
			for j in xrange(i+i, max, i):
				if j % i == 0:
					nlist[j] = False
	plist = [2]
	for i in xrange(3, max, 2):
		if nlist[i]: plist.append(i)
	return plist

def checkCP(p, primes):
	mult = 1
	num = p
	cnt = 0
	d = 0
	while num > 0:
		d = num % 10
		if d % 2 == 0 or d == 5:
			primes.remove(p)
			return 0
		num //= 10
		mult *= 10
		cnt += 1
	mult //= 10
	num = p
	found = []
	for i in range(cnt):
		if num in primes:
			found.append(num)
			primes.remove(num)
		elif num not in found: return 0
		d = num % 10
		num = d * mult + num / 10
	return len(found)

def solve():
	numCP = 2
	primes = pSieve(1000000)
	primes.remove(2)
	primes.remove(5)
	while len(primes):
		numCP += checkCP(primes[0], primes)
	print numCP

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
