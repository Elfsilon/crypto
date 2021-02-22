def mult(a, b):
    layer_len = len(a) + len(b) - 1
    layers = []

    for i in range(len(b)-1, -1, -1):
        if b[i] == "1":
            layer = [0 for s in range(0, layer_len)]
            for j in range(len(a)-1, -1, -1):
                layer[i+j] = int(a[j])
            layers.append(layer)

    # Calculates count of units in each column
    # if odd -> 1 else -> 0 
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
        

