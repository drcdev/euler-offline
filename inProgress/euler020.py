import sys
from time import clock
from math import factorial

def solve():
	print sum(map(int, str(factorial(100))))

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
