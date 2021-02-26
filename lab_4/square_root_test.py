def square_root_test(n):
    if n == 2:
        return True

    counter = 0
    for x in range(1, n):
        if x**2 % n == 1:
            counter += 1
    
    return counter == 2
    