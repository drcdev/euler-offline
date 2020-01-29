import sys
from time import clock

def factorial(num):
	if num == 0: return 1
	f = 1
	for i in range(num, 1, -1):
		f *= i
	return f

def solve():
	facts = []
	ans = 0
	for i in range(10):
		facts.append(factorial(i))
	for i in xrange(10, 2540161):
		sumf = 0
		num = i
		while num > 0:
			d = num % 10
			num //= 10
			sumf += facts[d]
		if sumf == i: ans += i
	print ans

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
