import sys
from time import clock

class BigNum:
	def __init__(self, s):
		self.num = []
		num = list(str(s))
		for i in range(len(num)):
			self.num.append(int(num[i]))
		self.num.reverse()
	
	def len(self):
		return len(self.num)

	def add(self, num):
		sum = ""
		carry = 0
		for i in range(min(len(self.num), len(num.num))):
			temp = self.num[i] + num.num[i]
			if carry != 0: temp += 1
			if temp >= 10:
				carry = 1
				temp -= 10
			else:
				carry = 0
			sum += str(temp)
		l = len(self.num) - len(num.num)
		if l == 0:
			if carry == 1: sum += "1"
		elif l > 0:
			for i in range(len(self.num)-l, len(self.num)):
				temp = self.num[i]
				if carry == 1: temp += 1
				if temp >= 10:
					carry = 1
					temp -= 10
				else: carry = 0
				sum += str(temp)
			if carry == 1: sum += "1"
		else:
			for i in range(len(num.num)+l, len(num.num)):
				temp = num.num[i]
				if carry == 1: temp += 1
				if temp >= 10:
					carry = 1
					temp -= 10
				else: carry = 0
				sum += str(temp)
			if carry == 1: sum += "1"
		return BigNum(sum[::-1])

def solve():
	x = BigNum(0)
	y = BigNum(1)
	count = 1
	while y.len() < 1000:
		t = x
		x = y
		y = x.add(t)
		count += 1
	print count

if __name__ == "__main__":
	t1 = clock()
	solve()
	t2 = clock()
	print "Runtime:", t2-t1
