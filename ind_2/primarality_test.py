import random

def ferm_test(n, iter_count):
    if n == 2:
        return True

    for i in range(0, iter_count):
        x = random.randint(1, n - 1)
        if (x ** (n - 1) % n != 1):
            return False
    return True


def primarality_test():
    with open('./ind_2/numbers.txt', 'w') as file:
        title = "Number     "
        for i in range(1, 101):
            if i < 10:
                title += f"Test {i}   "
            elif i != 100:
                title += f"Test {i}  "
            else:
                title += f"Test {i}"
        file.write(title+"\n")

        for num in range(2, 1000):
            if num < 10:
                row = f"{num}          "
            elif num < 100:
                row = f"{num}         "
            elif num < 1000:
                row = f"{num}        "
            elif num < 10000:
                row = f"{num}       "
            elif num < 100000:
                row = f"{num}      "
            elif num < 1000000:
                row = f"{num}     "
            elif num < 10000000:
                row = f"{num}    "
            elif num < 100000000:
                row = f"{num}   "
            elif num < 1000000000:
                row = f"{num}  "

            for rounds in range(1, 101):
                res = ferm_test(num, rounds)
                if res:
                    row += f"   +    "
                else:
                    row += f"   -    "
            file.write(row+"\n")

primarality_test()