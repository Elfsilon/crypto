from lab_2.mult import mult
from lab_2.add import add

# результат + остаток
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



# Вся логика
def div(a, b):
    multiplier_bites = []
    rest=""

    m = ""
    r = a

    while True:
        m, r = div_core(r, b)
        multiplier_bites.append(m)

        if m == "1":
            rest = r
            break
        if r == "0":
            break

    multiplier = multiplier_bites[0]
    if len(multiplier_bites) > 1:
        for i in range(1, len(multiplier_bites)):
            multiplier = add(multiplier, multiplier_bites[i])
    
    return multiplier, rest