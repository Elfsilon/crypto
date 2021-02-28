import random

# Тест Ферма
def fermat_test(n, iter_count=100):
    if n == 2:
        return True

    for _ in range(iter_count):
        x = random.randint(1, n - 1)
        if (x ** (n - 1) % n != 1):
            return False
    return True


# Испытание квадратным корнем
def square_root_test(n):
    if n == 2:
        return True

    counter = 0
    for x in range(1, n):
        if x**2 % n == 1:
            counter += 1
    
    return counter == 2


# Тест Миллера-Рабина
def miller_rabin_test(n, k=100):
    if n < 2: 
        return False

    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: 
            return n == p

    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2

    for _ in range(k):
        x = pow(random.randint(2, n-1), int(d), int(n))
        if x == 1 or x == n-1: 
            continue
        for _ in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: 
            return False
    return True