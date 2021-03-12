import math
import random
import utils
import operator
from functools import reduce

def original(n):
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            return i, int(n/i)
    return n, 1


# Метод факторизации Полларда p-1
def pollard_p_minus_one(n, B=5, M=13, a=2):
    if B < 1:
        raise Exception('B must be bigger than 1')
    if B >= M:
        raise Exception('B must be less than sqrt(n)')
    if M >= B ** 2:
        raise Exception('M must be less than B^2')
    if M >= math.sqrt(n):
        raise Exception('M must be less than sqrt(n)')
    if a < 1:
        raise Exception('a must be bigger than 1')

    # 1 stage 
    mb_primes = utils.primes(2, B)
    primes_mul = reduce(operator.mul, mb_primes, 1)

    b = (a ** primes_mul) % n
    q = utils.gcd(b-1, n)

    if q > 1:
        return q, n // q

    # 2 stage
    m_primes = utils.primes(B, M)
    for m in m_primes:
        fm = (b ** (m-1)) % n
        gm = utils.gcd(fm, n)
        if gm > 1:
            return gm, n // gm


    return math.nan, math.nan


# Метод факторизации Полларда PO (Rho)
def pollard_po(n, func=lambda x: x**2 + 1):
    x = random.randint(1, n-2)
    y = 1
    i = 1
    d = 1
    stage = 2

    while utils.gcd(n, x - y) == 1:
        if i == stage:
            y = x
            stage *= 2

        x = func(x) % n
        i += 1
    
    d = utils.gcd(n, x - y)
    b = n // d

    res = [d]
    # Если второй множитель не простой - продолжаем раскладывать уже его
    if not utils.is_prime(b):
        b1, b2 = pollard_po(b)
        res.append(b1)
        if isinstance(b2, tuple):
            res.append(b2[0])
            res.append(b2[1])
        else:
            res.append(b2)
        return res

    res.append(b)
    return res


# Метод факторизации Ферма
def fermat(n):
    s = round(math.sqrt(n) + 0.5)

    if s**2 == n:
        return int(s), int(s/n)

    x = s
    l = x**2-n
    k = 0   

    while True:
        if utils.is_perfect_square(l):
            y = math.isqrt(l)
            return x+y, x-y

        k += 1
        x += 1
        l = (x ** 2) - n


test_numbers = [561, 1207, 983, 65623]
for n in test_numbers:
    print(f"{n}:")
    print("Original:", original(n))
    print("P-1:", pollard_p_minus_one(n))
    print("PO(Rho):", pollard_po(n))
    print("Fermat:", fermat(n))
    print()