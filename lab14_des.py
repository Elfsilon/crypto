alphabet = {
    "e": [0, 0, 0, 1],
    "s": [0, 0, 1, 0],
    "a": [0, 0, 1, 1],
    "g": [0, 1, 0, 0],
    "e": [0, 1, 0, 1],
    "m": [0, 1, 1, 0],
}

def des(mes, key):
    diff = 16 - len(mes)

    binary_string = []

    for letter in mes:
        for b in alphabet[letter]:
            binary_string.append(b)

    for i in range(diff):
        for b in [0, 0, 0, 0]:
            binary_string.append(b)

    L = binary_string[:32]
    R = binary_string[32:]

    subkeys = create_subkeys(key)

    # print(len(L))
    # print(len(R))
    # print(subkeys)


# Таблица перестановки подключей
PC_1 = [
    57,  49,  41,  33,  25,  17,   9,
    1,   58,  50,  42,  34,  26,  18,
    10,  2,   59,  51,  43,  35,  27,
    19,  11,  3,   60,  52,  44,  36,
    63,  55,  47,  39,  31,  23,  15,
    7,   62,  54,  46,  38,  30,  22,
    14,  6,   61,  53,  45,  37,  29,
    21,  13,  5,   28,  20,  12,   4,
]

PC_2 = [
    14,  17,  11,  24,   1,   5,
     3,  28,  15,   6,  21,  10,
    23,  19,  12,   4,  26,   8,
    16,   7,  27,  20,  13,   2,
    41,  52,  31,  37,  47,  55,
    30,  40,  51,  45,  33,  48,
    44,  49,  39,  56,  34,  53,
    46,  42,  50,  36,  29,  32,
]

Shift_Schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def create_subkeys(key):
    # Постановка по PC_1
    key_plus = []
    for k in PC_1:
        key_plus.append(key[k])

    C = key_plus[:32]
    D = key_plus[32:]

    # Shift every key
    # Apply permutation

    print(key_plus)
    

message = "message"
key = [
    0, 0, 0, 1, 0, 0, 1, 1, 
    0, 0, 1, 1, 0, 1, 0, 0, 
    0, 1, 0, 1, 0, 1, 1, 1,
    0, 1, 1, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 1,
    1, 0, 1, 1, 1, 1, 0, 0,
    1, 1, 0, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 0, 0, 0, 1,
]
des(message, key)