import sys
from time import clock

def solve():
	dist = []
	for a in range(2, 101):
		for b in range(2, 101):
			x = pow(a, b)
			if not x in dist:
				dist.append(x)
	print len(dist)

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
