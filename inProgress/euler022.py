import sys
import os
from time import clock
from random import randint

names = []
letter = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def qsSwap(l, r):
	global names
	temp = names[l]
	names[l] = names[r]
	names[r] = temp

def qsPartition(l, r, pivot):
	global names
	pValue = names[pivot]
	qsSwap(pivot, r)
	ind = l
	for i in range(l, r):
		if names[i] < pValue:
			qsSwap(i, ind)
			ind += 1
	qsSwap(ind, r)
	return ind

def quicksort(l, r):
	global names
	if l < r:
		pivot = randint(l,r)
		pivotNew = qsPartition(l, r, pivot)
		quicksort(l, pivotNew-1)
		quicksort(pivotNew+1, r)

def solve():
	global names
	nsum = 0
	with open('euler022.py.names', 'r') as f:
		names = f.read().split('\",\"')
	names[0] = names[0][1:]
	names[-1] = names[-1][0:-1]
	quicksort(0, len(names)-1)
	for i in range(len(names)):
		temp = 0
		for j in range(len(names[i])):
			temp += letter[names[i][j]]
		nsum += temp * (i+1)
	print nsum

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
