import utils
import math
import random

# El-Gamal cryptosystem

def select_keys():    
    p = 307 # p - большое простое число
    g = utils.gen_primitive_root(p) # случайный первообразный корень p
    x = utils.gen_relative_prime(p-1) # взаимнопростое с p-1: 1 < x < p-1 (private key)
    y = (g ** x) % p # (public key)

    return {
        'public': {
            'p': p,
            'g': g,
            'key': y,
        },
        'private': {
            'key': x
        }
    }

def encrypt_message(mes, g, p, public_key):
    # mes < p (!!!)
    mes_bytes = mes.encode()

    encrypted_bytes_a = []
    encrypted_bytes_b = []

    rp = utils.relative_primes(public_key-1, 2, public_key-1)
    k = rp[random.randint(0, len(rp)-1)]

    for M in mes_bytes:
        encrypted_bytes_a.append(int((g ** k) % p))
        encrypted_bytes_b.append((int(public_key ** k) * M % p))

    return encrypted_bytes_a, encrypted_bytes_b


def decrypt_message(encoded_bytes_a, encoded_bytes_b, p, private_key):
    l = len(encoded_bytes_a)

    M = bytearray(l)
    power = p - 1 - private_key
    for i in range(l):
        M[i] = ((encoded_bytes_a[i] ** power) * encoded_bytes_b[i]) % p

    return M.decode()


config = select_keys()
print(config)

message = "Большое сообщение для шифрования"
print(f"Исходное сообщение: '{message}'")

encrypted_a, encrypted_b = encrypt_message(message, config['public']['g'], config['public']['p'], config['public']['key'])
enc_a_str = " ".join(map(lambda x: str(x), encrypted_a))
enc_b_str = " ".join(map(lambda x: str(x), encrypted_b))
print(f"Зашифрованное сообщение: {enc_a_str} {enc_b_str}")

decrypted_message = decrypt_message(encrypted_a, encrypted_b, config['public']['p'], config['private']['key'])
print(f"Расшифрованное сообщение: '{decrypted_message}'")
