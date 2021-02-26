import random

def ferm_test(n, iter_count):
    if n == 2:
        return True

    for i in range(iter_count):
        x = random.randint(1, n - 1)
        if (x ** (n - 1) % n != 1):
            return False
    return True
