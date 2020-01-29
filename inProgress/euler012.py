import sys
from time import clock

def pFactNoD(num, plist):
	nod = 1
	rem = num
	for i in range(len(plist)):
		if plist[i] * plist[i] > num:
			return nod * 2;
		
		exp = 1
		while rem % plist[i] == 0:
			exp += 1
			rem = rem / plist[i]
		
		nod *= exp
		if rem == 1:
			return nod
	return nod

def pSieve(max):
	nlist = [True] * max
	nlist[0] = False
	nlist[1] = False
	for i in xrange(2, max):
		if nlist[i]:
			for j in xrange(i+1, max):
				if j % i == 0:
					nlist[j] = False
	plist = [2]
	for i in xrange(3, max, 2):
		if nlist[i]: plist.append(i)
	return plist
		

def solve():
	CP1 = 2
	CP2 = 2
	i = 2
	num = 1
	count = 0
	plist = pSieve(2000)
	while count <= 500:
		if i % 2 == 0:
			CP1 = pFactNoD(i+1, plist)
		else:
			CP2 = pFactNoD((i+1)/2, plist)
		count = CP1 * CP2
		i += 1
	num = i * (i-1) / 2
	print num

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
