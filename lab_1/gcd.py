import math

def gcd_core(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd(a, b):
    return int(gcd_core(math.fabs(a), math.fabs(b)))