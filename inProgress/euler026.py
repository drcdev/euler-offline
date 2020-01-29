import sys
from time import clock

def solve():
	seq = 0
	ans = 0
	for i in range(1000, 1, -1):
		if seq >= i: break
		rem = [0] * i
		val = 1
		pos = 0
		while rem[val] == 0 and val != 0:
			rem[val] = pos
			val *= 10
			val %= i
			pos += 1
		if pos - rem[val] > seq:
			seq = pos - rem[val]
			ans = i
	print ans

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
