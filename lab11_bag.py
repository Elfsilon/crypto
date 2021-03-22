import utils
import math
import random

def select_keys(supervector):    
    supersum = sum(supervector)
    q = random.randint(supersum + 10, supersum * 10)
    r = utils.gen_relative_prime(q)

    fn = lambda x: r * x % q
    b = list(map(fn, supervector))

    return {
        'public': {
            'b': b,
        },
        'private': {
            'w': supervector,
            'q': q,
            'r': r,
        }
    }

def encrypt_message(mes, b):
    cipher = 0
    for i in range(len(mes)):
        if mes[i] == "1":
            cipher += b[i]

    return cipher


def decrypt_message(cipher, r, q, w):
    s = utils.comparison(r, 1, q)

    stack = []
    diff = cipher * s % q
    while diff != 0:
        for i in reversed(range(len(w))):
            if w[i] <= diff:
                stack.append(w[i])
                diff -= w[i]
                break
    
    decrypted = ""
    for num in w:
        if num in stack:
            decrypted += "1"
        else:
            decrypted += "0"
        
    return decrypted
        


config = select_keys([3, 5, 11, 21, 43, 87, 172, 350, 701, 1500])
print(config)

message = "1000101011"
print(f"Исходное сообщение: '{message}'")

enc = encrypt_message(message, config['public']['b'])
print(f"Зашифрованное сообщение: {enc}")

dec = decrypt_message(enc, config['private']['r'], config['private']['q'], config['private']['w'])
print(f"Расшифрованное сообщение: '{dec}'")
