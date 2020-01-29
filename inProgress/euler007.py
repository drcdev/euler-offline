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

def solve():
	plist = primeSieve(125000)
	if len(plist) >= 10001:
		print plist[10000]

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
