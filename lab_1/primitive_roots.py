import math
from lab_1.relative_primes import relative_primes

def primitime_roots(m):
    for r in range(2, m):
        for p in range(1, m):
            val = math.pow(r, p) % m
            if val == 1:
                if p == m-1:
                    primes = relative_primes(2, m-1, m-1)
                    res = []
                    for rp in primes:
                        res.append(int(math.pow(r, rp) % m))
                    return res
                else:
                    break

    empty = []
    return empty