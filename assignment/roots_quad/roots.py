
import math
def findRoots(a, b, c):
    if a == 0:
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
 
    if d > 0:
        r1=((-b + sqrt_val)/(2 * a))
        r2=((-b - sqrt_val)/(2 * a))
        tup=(r1,r2)
        print(tup)
    elif d == 0:
        r1=(-b / (2*a))
        tup=(r1)
        print(tup)
    else: 
        r1=(- b / (2*a), " + i", sqrt_val/ (2 * a))
        r2=(- b / (2*a), " - i", sqrt_val/ (2 * a))
        tup=(r1,r2)
        print(tup)
a = 1
b = -7
c = 12
findRoots(a, b, c)