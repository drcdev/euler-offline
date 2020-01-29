import sys
from time import clock

def factorial(n):
	x = 1
	for i in range(1,n+1): x *= i
	return x

def solve():
	n = 20
	routes = factorial(2*n)/(factorial(n)*factorial(n))
	print routes

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
