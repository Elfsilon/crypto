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