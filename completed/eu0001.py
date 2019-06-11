import hashlib
import hash

limit = 1000
factor = 1
sumOfFactors = 0

while factor < limit:
    if factor % 3 == 0 or factor % 5 == 0:
        sumOfFactors += factor
    factor += 1


hash.printHash(str(sumOfFactors))
