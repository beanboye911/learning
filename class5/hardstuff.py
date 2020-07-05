import math
def hardstuff(a,b,c):
    x = b*b - 4*a*c
    if x>0:
        y = math.sqrt(x)
        z = -b + y
        w = z/(2*a)
        z2 = -b - y
        w2 = z2/(2*a)
        print("solutions are %g and %g." %(w, w2))
    elif x==0:
        w2 = -b/2*a
        print('solution is %g.' %(w2))
    else:
        print('no solution for you.')
