from lab_1.gcd import gcd

def relative_primes(start, end, p):
    res = []
    for i in range(start, end):
        if gcd(i, p) == 1:
            res.append(i)
    return res
