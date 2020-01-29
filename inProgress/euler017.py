import sys
from time import clock

numtionary = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7, 1000:8, "and":3}

def verbose(n):
	total = 0
	breakdown = list(str(n))
	if n in numtionary and n != 100 and n != 1000:
		return numtionary[n]
	if n % 100 == 0 and n != 1000:
		return numtionary[100]+numtionary[int(breakdown[0])]
	if n < 100:
		total = numtionary[int(breakdown[-1])]
		total += numtionary[int(breakdown[-2]+"0")]
		return total
	if n < 1000:
		small = int(breakdown[-2]+breakdown[-1])
		if small in numtionary:
			total = numtionary[small]
		else:
			total = numtionary[int(breakdown[-1])]
			total += numtionary[int(breakdown[-2]+"0")]
		total += numtionary[100]
		total += numtionary[int(breakdown[0])]
		total += numtionary["and"]
		return total
	return numtionary[1000]+numtionary[int(breakdown[0])]

def solve():
	total = 0
	for i in range(1, 1000+1):
		total += verbose(i)
	print total

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
