import sys
from time import clock
from math import sqrt

def pSieve(max):
	nlist = [True] * max
	nlist[0] = False
	nlist[1] = False
	for i in xrange(2, max):
		if nlist[i]:
			for j in xrange(i+1, max):
				if j % i == 0:
					nlist[j] = False
	plist = [2]
	for i in xrange(3, max, 2):
		if nlist[i]: plist.append(i)
	return plist

def fPrimeSum(num, plist):
	n = num
	fsum = 1
	p = plist[0]
	i = 0
	j = 0
	
	while p*p <= n and n > 1 and i < len(plist):
		p = plist[i]
		i += 1
		if n % p == 0:
			j = p * p
			n //= p
			while n % p == 0:
				j *= p
				n //= p
			fsum = fsum * (j-1) / (p-1)
	if n > 1: fsum *= n + 1
	return fsum - num
			

def solve():
	amicableSum = 0
	fac1 = 0
	fac2 = 0
	limit = 10000
	plist = pSieve(int(sqrt(limit)+1))
	
	for i in range(2, limit+1):
		fac1 = fPrimeSum(i, plist)
		if fac1 > i and fac1 < limit + 1:
			fac2 = fPrimeSum(fac1, plist)
			if fac2 == i:
				amicableSum += i + fac1
	print amicableSum

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
