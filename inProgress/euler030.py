import sys
from time import clock

def solve():
	ans = 0
	for i in xrange(2, 355000):
		sumOfPow = 0
		num = i
		while num > 0:
			d = num % 10
			num //= 10
			dtemp = d
			for j in range(1, 5):
				dtemp *= d
			sumOfPow += dtemp
		if sumOfPow == i:
			ans += i
	print ans

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
