def binAdd(x,y):
    '''x,y are strings'''
    result=''
    if len(x) < len(y):
        x='0'*(len(y)-len(x))+x
    else:
        y='0'*(len(x)-len(y))+y
    carry=0
    for i in range(len(x))[::-1]:
        bitsum=sum(map(int,(x[i],y[i])))+carry
        if bitsum>1:
            result=str(bitsum-2)+result
            carry=1
        else:
            result=str(bitsum)+result
    if carry:
        result='1'+result
    return result
        
            
        
    
def binCollatz(n):
    n='{0:b}'.format(n)
    while n!='1':
        n=binAdd(n+'1',n)
        n=''.join(n.rpartition('1')[0:2])
    print int(n,2)

def verboseBinCollatz(n):
    n='{0:b}'.format(n)
    while n!='1':
        if n[-1]=='0':
            n=n[:-1]
            print int(n,2)
        else:
            n=binAdd(n+'1',n)
            print int(n,2)
    
