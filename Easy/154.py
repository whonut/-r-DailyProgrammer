def decode(s):
    string=s[1:-1]
    msg=''
    while '(' in string or '{' in string or '[' in string:
        print string
        bracks={'(':')','{':'}','[':']'}
        indices=[]
        for b in bracks.keys():
            if string.find(b)!=-1:
                indices.append(string.find(b))
            #print b,str(indices[-1])
        next_brack=string[min(indices)]
        print 'next open bracket should be '+next_brack
        phrase1_end=string.find(next_brack)
        phrase2_start=string.find(bracks[next_brack])+1
        encoded_start=string.find(next_brack)+1
        encoded_end=string.find(bracks[next_brack])
        print string[phrase1_end:]+string[phrase2_start:]+' *'
        string=string[encoded_start:encoded_end]

def decode(s):
    s=s.split('(')
    print s

s=raw_input('Enter string: ')
print decode(s)





