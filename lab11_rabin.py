import utils

def select_keys(p, q):
    # p = q = 3 mod 4 (!!!)
    n = p * q

    return {
        'public': {
            'n': n,
        },
        'private': {
            'p': p,
            'q': q,
        },
    }


def encrypt(mes, n):
    encoded = mes.encode()

    for b in encoded:
        print(b, end=' ')
    print()

    encrypted = []
    for m in encoded:
        c = (m ** 2) % n
        encrypted.append(int(c))

    return encrypted


def decrypt(encrypted, p, q, n):
    l = len(encrypted)

    yp, yq = utils.diophantine(p, q, 1)

    decrypted = []
    for i in range(l):
        pow_p = int((p + 1) / 4)
        pow_q = int((q + 1) / 4)
        mp = encrypted[i] ** pow_p % p
        mq = encrypted[i] ** pow_q % q

        f1 = yp*p*mq
        f2 = yq*q*mp

        r = int((f1 + f2) % n)
        r_inv = int(n - r)
        s = int((f1 - f2) % n)
        s_inv = int(n - s)

        decrypted.append([r, r_inv, s, s_inv])

    return decrypted


config = select_keys(311, 71)
print(config)

mes = "Some phrase"
print(f"Исходное сообщение: {mes}")

enc = encrypt(mes, config['public']['n'])
print(f"Зашифрованное сообщение: {enc}")

dec = decrypt(enc, config['private']['p'], config['private']['q'], config['public']['n'])
print(f"Расшифрованное сообщение:")
encoded = mes.encode()
for i in range(len(dec)):
    print(f"{encoded[i]} : {dec[i]}")