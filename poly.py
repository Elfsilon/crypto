import math

# Сложение 2 полиномов в GF(2)
def add(a, b):
    res_len = max(len(a), len(b))
    op_a = "".join(["0" for i in range(0, res_len - len(a))])
    op_b = "".join(["0" for i in range(0, res_len - len(b))])
    op_a += a
    op_b += b

    res = ""
    for j in range(0, res_len):
        if op_a[j] == "1" and op_b[j] == "0" or op_a[j] == "0" and op_b[j] == "1":
            res += "1"
        else:
            res += "0"
    
    return str(int(res))


# Умножение 2 полиномов в GF(2)
def mult(a, b):
    layer_len = len(a) + len(b) - 1
    layers = []

    for i in range(len(b)-1, -1, -1):
        if b[i] == "1":
            layer = [0 for s in range(0, layer_len)]
            for j in range(len(a)-1, -1, -1):
                layer[i+j] = int(a[j])
            layers.append(layer)

    res = ""
    for j in range(0, layer_len):
        units_quantity = 0
        for i in range(0, len(layers)):
            if layers[i][j] == 1:
                units_quantity += 1
        if units_quantity % 2 != 0:
            res += "1"
        else:
            res += "0"
    
    return res
        


# Деление с остатком 2 полиномов в GF(2)
def div(a, b):
    multiplier_bites = []
    rest=""

    m = ""
    r = a

    while True:
        m, r = div_core(r, b)
        multiplier_bites.append(m)

        if m == "1" or m == "0":
            rest = r
            break
        if r == "0":
            break

    multiplier = multiplier_bites[0]
    if len(multiplier_bites) > 1:
        for i in range(1, len(multiplier_bites)):
            multiplier = add(multiplier, multiplier_bites[i])
    
    return multiplier, rest

def div_core(a, b):
    if a == b:
        return "1", "0"

    deg_a = len(a)-1
    deg_b = len(b)-1

    if deg_a < deg_b:
        return "0", a

    if deg_a == deg_b:
        return "1", add(a, b)

    deg_m = deg_a - deg_b
    m = ["0" for i in range(0, deg_m+1)]
    m[0] = "1"
    m = "".join(m)

    mul = mult(b, m)
    r = add(a, mul)

    return m, r


# НОД 2 полиномов в GF(2) 
def gcd(a, b):
    a1 = a
    b1 = b
    r = a
    supposed_gcd = math.nan

    while True:
        _, r = div_core(a1, b1)

        if r == "0":
            break

        supposed_gcd = r

        a1 = b1
        b1 = r
    
    return supposed_gcd

# Проверка на приводимость
def is_privodim(polynom):
    d = int("0b" + polynom, 2)
    for i in range(2, d):
        if div(polynom, bin(i)[2:])[1] == "0":
            return False

    return True

# Проверка на примитивность
def is_primitive(polynom):
    pow = len(polynom) - 1
    m = 2 ** pow - 1

    lst = generate_polynom(pow, m) 
    if div(lst[len(lst) - 1], polynom)[1] == "0":
        for i in range(0, len(lst)-1):
            d, m = div(lst[i], polynom)
            print(lst[i] + "  " + polynom + "  " + d + "  " +  m)
            if m == "0":
                return False
        return True

    return False

# Хелпер
def generate_polynom(n, m):
    lst = list()
    for p in range(n,m):
        new_pol = "1" + ''.join([ "0" for i in range (p) ]) + "1"
        lst.append(new_pol)

    return lst

# примитивные корни для полинома в поле 
# main_elem - образующий многочлен, m - поле
# print(len(prim_root('1000011', 64)))
def prim_root(main_elem, m):
    d = int("0b" + main_elem, 2)
    first_root = None
    mod_list = None
    for i in range(2, d):
        x = i
        mod_list = [bin(x)[2:]]
        
        # поиск остатков для корня i
        for j in range(2, m):
            x *= i
            mod = div(bin(x)[2:], main_elem)[1]
            mod_list.append(mod)
            # остаток
            if mod == "1" :
                if j != m - 1:
                    break
                else:
                    first_root = i
        
        if first_root:
            break
    
    result = list()
    for j in range(0, m-1):
        if gcd_lab1(j+1,m-1) == 1:
            result.append(mod_list[j])
        
    return result