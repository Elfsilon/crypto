from lab_1.gcd import gcd
from lab_1.gcd_extended import gcd_extended
from math import nan

def diophantine(a, b, c):
    check = c % gcd(a, b) == 0

    if check:
        _, xg, yg = gcd_extended(a, b)
        return xg * c, yg * c
    
    return nan, nan
    