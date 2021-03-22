import utils
import math

def select_keys(p, q):
    n = p * q
    ef = utils.euler(n)

    e = 17
    d = utils.comparison(e, 1, ef)

    return {
        'public': {
            'e': e,
            'n': n,
            'ef': ef,
        },
        'private': {
            'd': d,
        },
    }


def encrypt(mes, public_key, module):
    encoded = mes.encode()

    encrypted = []
    for m in encoded:
        c = (m ** public_key) % module
        encrypted.append(int(c))

    return encrypted


def decrypt(encrypted, private_key, module):
    l = len(encrypted)

    decrypted = bytearray(l)
    for i in range(l):
        m = (encrypted[i] ** private_key) % module
        decrypted[i] = int(m)

    return decrypted.decode()


config = select_keys(17, 13)
print(config)

mes = "Iron man"
print(f"Исходное сообщение: {mes}")

enc = encrypt(mes, config['public']['e'], config['public']['n'])
print(f"Зашифрованное сообщение: {enc}")

dec = decrypt(enc, config['private']['d'], config['public']['n'])
print(f"Расшифрованное сообщение: {dec}")