import math

def is_perfect_square(x):
    return x == math.isqrt(x) ** 2

def ferm_factorization(n):
    """
    Если n - натуральное нечетное число, которое представлено в виде n = a*b, где a, b - натуральные,
    то n можно представить в виде n = x^2 - y^2, (x > y)
    Обратное справедливо тоже
    n = x^2 - y^2 = (x+y)(x-y) = a*b => a=x+y, b=x-y

    Args: n - натуральное нечетное число большее 1

    Returns: (a, b) - разложение числа n на множители
    """
    a = math.nan
    b = math.nan

    # Вычисляем наименьшее целое число > sqrt(n)
    s = round(math.sqrt(n) + 0.5)

    if s**2 == n:
        return int(s), int(s/n)

    x = s
    l = x**2-n
    k = 0   

    while True:
        # Если l - полный квадрат, то y = sqrt(l)
        if is_perfect_square(l):
            y = math.isqrt(l)
            return x+y, x-y

        k += 1
        x += 1
        l = x**2-n



    

