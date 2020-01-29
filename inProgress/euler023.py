import sys
from time import clock
from math import sqrt

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
			j = p*p
			n //= p
			while n % p == 0:
				j *= p
				n //= p
			fsum *= (j-1) / (p-1)
	if n > 1: fsum *= n + 1
	return fsum - num

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

def solve():
	limit = 28123
	plist = pSieve(int(sqrt(limit))+1)
	abun = []
	for i in range(2, limit+1):
		if fPrimeSum(i, plist) > i:
			abun.append(i)
	sumOfAbun = [False] * (limit+1)
	for i in range(len(abun)):
		for j in range(i, len(abun)):
			if abun[i] + abun[j] <= limit:
				sumOfAbun[abun[i]+abun[j]] = True
			else: break
	sum = 0
	for i in range(len(sumOfAbun)):
		if not sumOfAbun[i]:
			sum += i
	print sum

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
