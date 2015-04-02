import random

def isSorted(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True

def bogo(L):
    while not isSorted(L):
        random.shuffle(L)
    return L

def recbogo(L):
    if isSorted(L):
        return L
    else:
        random.shuffle(L)
        return bogo(L)


