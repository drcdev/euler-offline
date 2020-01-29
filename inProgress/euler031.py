import sys
from time import clock

def solve():
	cashMax = 200
	cash = [0] * (cashMax+1)
	cash[0] = 1
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	for i in range(len(coins)):
		for j in range(coins[i], cashMax+1):
			cash[j] += cash[j - coins[i]]
	print cash[-1]

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
