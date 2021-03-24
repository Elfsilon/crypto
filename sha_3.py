import hashlib

m = hashlib.sha3_256()
m.update(b"super simple sha-3")
encrypted = m.hexdigest()
print(encrypted)