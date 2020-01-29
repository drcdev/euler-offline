import sys
from time import clock

def digitSum(n):
	s = 0
	while n > 0:
		s += (n % 10)
		n //= 10
	return s

def solve():
	print digitSum(pow(2, 1000))

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
