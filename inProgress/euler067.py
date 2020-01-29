import sys
import os
from time import clock

def solve():
	tri = []
	f = open('euler067.py.tri', 'r')
	for line in f:
		l = line.split(' ')
		for i in range(len(l)):
			l[i] = int(l[i])
		tri.append(l)
	for i in range(len(tri)-1, 0, -1):
		for j in range(0, len(tri[i-1])):
			if tri[i][j] > tri[i][j+1]:
				tri[i-1][j] += tri[i][j]
			else: tri[i-1][j] += tri[i][j+1]
	print tri[0][0]
	f.close()

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
