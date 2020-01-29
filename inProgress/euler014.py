import sys
from time import clock

def sequence(n):
	x = n
	len = 0
	while x != 1:
		if x % 2 == 0:
			x //= 2
		else:
			x *= 3
			x += 1
		len += 1
	return len + 1

def solve():
	if len(sys.argv) > 1: tmax = int(sys.argv[1])
	else: tmax = 1000000
	max = 0
	val = 0
	for i in range(2,tmax+1):
		x = sequence(i)
		if x > max:
			max = x
			val = i
	print "Value:", val, "\tChain:", max

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
