from math import sin,pi
N, R= map(float, raw_input('Enter the number of sides followed by the circumradius: ').split())
print round(N*(R*2*sin(pi/N)),3)   
