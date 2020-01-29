import sys
from time import clock
from fractions import gcd

def solve():
	productN = 1
	productD = 1
	for i in range(10):
		for d in range(i):
			for n in range(d):
				if (n * 10 + i) * d == n * (i * 10 + d):
					productD *= d
					productN *= n
	print productD / gcd(productN, productD)

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
