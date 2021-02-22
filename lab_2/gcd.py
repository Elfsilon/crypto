from lab_2.div import div_core
from math import nan

def gcd(a, b):
    a1 = a
    b1 = b
    r = a
    supposed_gcd = nan

    while True:
        _, r = div_core(a1, b1)

        if r == "0":
            break

        supposed_gcd = r

        a1 = b1
        b1 = r
    
    return supposed_gcd
