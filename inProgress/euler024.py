import sys
from time import clock
from math import ceil

def permutations(num):
	n = num
	if n == 1: return 1
	for i in range(2, num):
		n *= i
	return n

def solve():
	ans = []
	goal = 1000000
	nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	for i in range(9, 0, -1):
		div = int(ceil(float(goal)/permutations(i)))-1
		goal = goal % permutations(i)
		n = nums[div]
		ans.append(n)
		nums.remove(n)
	ans.append(nums[0])
	print "".join(map(str, ans))

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
