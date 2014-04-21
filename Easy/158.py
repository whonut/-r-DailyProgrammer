def noDups(n):
    for c in str(n):
        if not str(n).count(c)==1:
            return False
    return True

for n in xrange(1000,10000):
    s=str(n)
    if (int(s[:2])+int(s[2:]))**2==n and n!=3025 and noDups(n):
        print n
#bonus
def isTorn(n):
    s=str(n)
    return (int(s[:len(s)/2])+int(s[len(s)/2:]))**2==n and len(s)%2==0
