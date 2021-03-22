import math
import random

def gcd_core(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Алгоритм Евклида    
# Возвращает НОД(a, b)
def gcd(a, b):
    return int(gcd_core(math.fabs(a), math.fabs(b)))


# Расширенный алгоритм Евклида
# Возвращает НОД(a, b) и решение уравнения ax+by=1
def gcd_extended(a, b):
    if a == 0:   
        return b, 0, 1
             
    gcd, x1, y1 = gcd_extended(b%a, a)  
     
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd, x, y 

# Функция эйлера 
# Возвращает количество взаимнопростых чисел с n
def euler(n):
    result = n  
       
    p = 2
    while p * p<= n : 
        if n % p == 0 : 
            while n % p == 0 : 
                n = n // p 
            result *= 1.0 - (1.0 / float(p))
        p = p + 1
          
    if n > 1 : 
        result *= 1.0 - (1.0 / float(n))
   
    return int(result) 


# Возвращает список простых чисел в промежутке [start, end)
def primes(start, end):    
    res = []
    for num in range(start, end):
        status = True
        for divisor in range(2, math.isqrt(num)):
            if num % divisor == 0:
                status = False
                break
        if status:
            res.append(num)
    return res

def gen_prime(start=2, end=2):
    ps = primes(start, end)
    return ps[random.randint(0, len(ps)-1)]    width: 100%;


# Возващает True, если n - простое
def is_prime(n):
    if n % 2 == 0:
        return n == 2
        
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


# Возващает True, если x - полный квадрат
def is_perfect_square(x):
    return x == math.isqrt(x) ** 2


# Решает диофантово уравнение ax+by=c
def diophantine(a, b, c):
    check = c % gcd(a, b) == 0
    if check:
        _, xg, yg = gcd_extended(a, b)
        return xg * c, yg * c
    
    return math.nan, math.nan


# Решает сравнение ax=b mod m
def comparison(a, b, m):
    d = gcd(a, m)

    if b % d == 0:
        x, _ = diophantine(a, m, b)
        return x % m

    return math.nan

def comparison_fermat(a,b,m):
    d = gcd(a,m)
    if d == 1:
        x = str(((a**(euler(m)-1))*b) % m)
    else:
        if b % d == 0:
            a1 = a//d
            b1 = b//d
            m1 = m//d
            x1 = ((a1**(euler(m1)-1))*b1) % m1
            x = str(m1)+"k + " + str(x1) + "(mod "+ str(m) + "), k ∈ {0,...," + str(d-1)+"}"
        else:
            x = "Решений нет"
    return x


# Возвращает список взаимнопростых с p чисел в промежутке [start, end)
def relative_primes(p, start=1, end=1):
    if end == 0:
        end = p

    res = []
    for i in range(start, end):
        if gcd(i, p) == 1:
            res.append(i)
    return res

def gen_relative_prime(p):
    relative_with_p = relative_primes(p, 2, 0)
    return relative_with_p[random.randint(0, len(relative_with_p)-1)]


# Возвращает список первообразных корней по основанию m
def primitime_roots(m):
    for r in range(2, m):
        for p in range(1, m):
            val = (r ** p) % m
            if val == 1:
                if p == m-1:
                    primes = relative_primes(m-1, 1, m-1)
                    res = []
                    for rp in primes:
                        res.append(int((r ** rp) % m))
                    return res
                else:
                    break

    empty = []
    return empty

def gen_primitive_root(p):
    roots = primitime_roots(p)
    return roots[random.randint(0, len(roots)-1)]

import numpy as np
def chinise(list_b, list_m):
    n = len(list_b)

    # Проверка
    for i in range(n):
        for j in range(n):
            if i != j:
                if gcd(list_m[i], list_m[j]) != 1:
                    print("Нет решений")
                    return math.nan

    Module = np.prod(list_m)
    Ms = []
    M_inv = []
    
    for i in range(n):
        M = 1
        for j in range(n):
            if i != j:
                M *= list_m[j]
        M_ = comparison(M, 1, list_m[i])

        Ms.append(M)
        M_inv.append(M_)

    x = 0
    for i in range(n):
        x += Ms[i] * M_inv[i] * list_b[i]
    x %= Module

    print(f"M = {M}")
    print(f"Ms = {Ms}")
    print(f"M inversions = {M_inv}")
    print(f"x = {x}")
    print()

    return x

# chinise([2, 15, 5], [5, 17, 12])
# chinise([8, 13, 4], [6, 35, 11])
# chinise([8, 13, 4], [5, 35, 11])