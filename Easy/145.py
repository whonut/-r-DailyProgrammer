input=raw_input('Enter the base width, trunk character and leaf character: ')
width,trunk,leaf=int(input.split()[0]),input.split()[1],input.split()[2]
n=1
while n<=width:
    print ' '*((width-n)/2)+leaf*n+' '*((width-n)/2)
    n+=2
print ' '*((width-3)/2)+trunk*3+' '*((width-3)/2)

