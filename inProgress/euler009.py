import sys
from time import clock

def solve(n):
	for a in range(1,n+1):
		b = a + 1
		c = b + 1
		while c < n:
			while c*c < a*a + b*b:
				c = c + 1
			if c*c == a*a + b*b and a+b+c == n:
				return a,b,c
			b = b + 1

if __name__ == "__main__":
	t1 = clock()
	a,b,c = solve(1000)
	t2 = clock()
	print "a =", a
	print "b =", b
	print "c =", c
	print "p =", a*b*c
	print "Runtime:", t2-t1
