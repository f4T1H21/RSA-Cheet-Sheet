# ﺏ
# Written by Şefik Efe aka f4T1H
# For more information, see https://github.com/f4T1H21/RSA-Cheet-Sheet

"""
RSA

n, e = Açık anahtar  (Public key)
d    = Gizli anahtar (Private key)
----------
- Üç tane belirlenen değer: p, q ve e
p & q asal sayı,
e ise t ile aralarında asal ve 1'den büyük, t den küçük bir tam sayı:
1 < e < t, ebob(e, t) = 1

- Üç tane hesaplanan değer: n, t ve d
n = p * q
t = λ(n) = ekok(p-1, q-1) # λ = Carmichael'in totient fonksiyonu
d = (e**-1) % t

m = Şifrelenecek verinin geri döndürülebilir bir protokol
kullanılarak oluşturulan sayısal karşılığı

-----------
Şifreleme işlemi = c = (m**e) % n
Deşifreleme işlemi   = (c**d) % n

-----------
0 ≤ m < n # Eşitsizliğinin sağlanmaması halinde,
deşifre işlemi sağlıklı bir şekilde gerçekleşemez.

Daha güvenli bir RSA şifrelemesi için:
1) d > (1/3) * (n**(1/4)) # Eşitsizliği sağlanmazsa: Wiener'in saldırısına karşı zaafiyet içerir.
2) e, küçük bir sayı olmamalı # Aksi halde Coppersmith'in saldırısı karşı zaafiyet içerir.
3) e, Fermat asallarından (Fn = (2**(2**n))+1, F0-F4) olmamalı.
"""


from math import lcm, gcd # ekok, ebob
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes # pycryptodome

# Prime generation
p, q = 1, 1
while p == q:
    p, q = getPrime(512), getPrime(512)

# Key generation
n = p * q
t = lcm(p-1, q-1)
while not (1 < (e:=getPrime(64)) < t and gcd(e, t) == 1):
    pass
d = pow(e, -1, t)
assert d > (1/3) * (n**(1/4))

# Data encoding
m = bytes_to_long(input('Please enter data to be encrypted: ').encode())
if not 0 <= m < n:
    print('\nEntered data is bigger than multiplication of primes,\nencryption is not possible in such a case! Exiting...')
    exit(1)

# Encryption
def encrypt(m, e, n):
    return pow(m, e, n)

# Decryption
def decrypt(c, d, n):
    return pow(c, d, n)

c = encrypt(m, e, n)
m_ = decrypt(c, d, n)

# Key distribution
print(f'Public key:\nn = {n}\ne = {e}\n')

print(f'Encrypted data: {hex(c)}')
print(f'Decrypted data: {long_to_bytes(m_).decode()}')
