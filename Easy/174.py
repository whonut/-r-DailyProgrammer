from collections import Counter
from timeit import timeit

def comp(bin_str):
    complements = {'0': '1', '1': '0'}
    ret = ''
    for d in bin_str:
        ret = ret + complements[d]
    return ret


def thueMorse(n):
    '''returns the nth order Thue-Morse Sequence'''
    if n == 0:
        return '0'
    else:
        return thueMorse(n-1) + comp(thueMorse(n-1))


def iterThueMorse(n):
    seq = '0'
    while n > 0:
        seq = seq + comp(seq)
        n -= 1
    return seq


def dirThueMorse(n):
    num_digits = 2**n
    seq = ''
    for i in xrange(num_digits):
        b = bin(i)[2:]
        ones = Counter(b)['1']
        seq = seq + str(ones % 2)
    return seq

print 'thueMorse:', timeit('thueMorse(10)','from __main__ import thueMorse')
print 'iterThueMorse:', timeit('iterThueMorse(10)','from __main__ import iterThueMorse')
print 'dirhueMorse', timeit('dirhueMorse(10)','from __main__ import dirThueMorse')
