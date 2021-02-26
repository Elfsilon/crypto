import math
import random
from lab_1.gcd import gcd

# Простая функция для проверки
def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def f(x):
    return x**2 + 1


def po_pollard_factorization(n):
    x = random.randint(1, n-2)
    y = 1
    i = 1
    stage = 2
    d = 1

    while gcd(n, x - y) == 1:
        if i == stage:
            y = x
            stage *= 2

        x = f(x) % n
        i += 1
    
    d = gcd(n, x - y)
    b = int(n/d)

    # Если второй множитель не простой - продолжаем раскладывать уже его
    if not is_prime(b):
        b1, b2 = po_pollard_factorization(b)
        return d, b1, b2

    return d, b
