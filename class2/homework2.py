import math
a = float(input("pls type a-value: "))
b = float(input("pls type b-value: "))
c = float(input("pls type c-value: "))
print("equation is %gx^2+%gx+%g=0" %(a, b, c))
x = b*b - 4*a*c
if x>0:
    y = math.sqrt(x)
    z = -b + y
    w = z/(2*a)
    z2 = -b - y
    w2 = z2/(2*a)
    print("solutions are %g and %g." %(w, w2))
elif x==0:
    w3 = -b/(2*a)
    print("solution is %g." %(w3))
else:
    print("no solution for you.")
