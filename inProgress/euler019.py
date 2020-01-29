import sys
from time import clock
from datetime import date

def solve():
	sun = 0
	for year in range(1901, 2001):
		for month in range(1, 13):
			if date(year, month, 1).weekday() == 6:
				sun += 1
	print sun

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
