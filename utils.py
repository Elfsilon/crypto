import math

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


# Возвращает список взаимнопростых с p чисел в промежутке [start, end)
def relative_primes(p, start=1, end=1):
    if end == 0:
        end = p

    res = []
    for i in range(start, end):
        if gcd(i, p) == 1:
            res.append(i)
    return res


# Возвращает список первообразных корней по основанию m
def primitime_roots(m):
    for r in range(2, m):
        for p in range(1, m):
            val = math.pow(r, p) % m
            if val == 1:
                if p == m-1:
                    primes = relative_primes(m-1, 1, m-1)
                    res = []
                    for rp in primes:
                        res.append(int(math.pow(r, rp) % m))
                    return res
                else:
                    break

    empty = []
    return empty