from lab_1.gcd import gcd
from lab_1.diophantine import diophantine
from math import nan

def comparison(a, b, m):
    d = gcd(a, m)

    if b % d == 0:
        x, _ = diophantine(a, m, b)
        return f"has {d} solutions", x

    return "has no solutions", nan