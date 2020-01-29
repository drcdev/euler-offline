import sys
from time import clock

def solve():
	corners = [1]
	for r in range(2, 1001, 2):
		for s in range(4):
			corners.append(corners[-1]+r)
	print sum(corners)

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
