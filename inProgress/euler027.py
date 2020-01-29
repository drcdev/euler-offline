import sys
from time import clock

def pSieve(max):
	nlist = [True] * max
	nlist[0] = False
	nlist[1] = False
	for i in xrange(2, max):
		if nlist[i]:
			for j in xrange(i+1, max):
				if j % i == 0:
					nlist[j] = False
	return nlist 

def testConsecutive(a, b):
	global plist
	n = 0
	done = False
	while not done:
		temp = n*n + a*n + b
		if temp < 1:
			done = True
		elif plist[temp] == True:
			n += 1
		else:
			done = True
	return n-1, a, b

plist = []
def solve():
	global plist
	plist = pSieve(12990)
	maxn = 0
	maxa = 0
	maxb = 0
	for a in range(-999, 1000):
		for b in range(-999, 1000):
			n = testConsecutive(a, b)
			if n[0] > maxn:
				maxn = n[0]
				maxa = n[1]
				maxb = n[2]
	print maxa * maxb

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
