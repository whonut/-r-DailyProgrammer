from time import time
from random import choice


# dict solution
def strands(strand):
    bases = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G', ' ': ' '}
    return strand + '\n' + ''.join(bases[c] for c in strand)


# replace solution
def strands2(strand):
    s = strand
    s = s.replace('A', 'T')
    s = s.replace('T', 'A')
    s = s.replace('G', 'C')
    s = s.replace('C', 'G')
    return s

s = ''
for i in xrange(10000):
    s = s + choice(('A', 'T', 'G', 'C')) + ' '
start = time()
for i in xrange(1000):
    strands(s)
print time() - start
print
start = time()
for i in xrange(1000):
    strands2(s)
print time() - start
