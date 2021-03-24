from ecdsa import SigningKey, NIST384p, BadSignatureError

sk = SigningKey.generate(curve=NIST384p)
vk = sk.verifying_key
signature = sk.sign(b"message")

try:
    assert vk.verify(signature, b"message")
    print('Цифровая подпись прошла проверку')
except BadSignatureError:
    print("Цифровая подпись не прошла проверку")