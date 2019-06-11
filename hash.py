import hashlib


def printHash(string):
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    print(md5.hexdigest())
