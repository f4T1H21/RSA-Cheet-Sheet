# RSA Şifreleme Yöntemi | Cryptosystem

- `(n, e)` = Açık anahtar (Public key)
- `d`    = Gizli anahtar (Private key)

## Üç tane belirlenen değer (Three determined values): p, q, e

- p & q asal sayı.
    - p & q are prime numbers.
- e ile t aralarında asal e, 1'den büyük, t'den küçük bir tam sayı: 1 < e < t, ebob(e, t) = 1
    - e and t are coprimes, e is an integer which is greater than 1 and smaller than t. (ebob = gcd)


## Üç tane hesaplanan değer (Three calculated values): n, t, d

- `n = p * q`
- `t = λ(n) = ekok(p-1, q-1)`
    - `λ` = Carmichael'in totient fonksiyonu
        - Carmichael's totient function (ekok = lcm)
- `d = (e**-1) % t`

---

- `m` = Şifrelenecek verinin geri döndürülebilir bir protokol kullanılarak oluşturulan sayısal karşılığı.
    - Numerical equivalent of the data (to be encrypted) in a reversible protocol.

## Şifreleme (Encryption)
`c = (m**e) % n`

## Deşifreleme (Decryption)
`m = (c**d) % n`

---

- `0 ≤ m < n` Eşitsizliğinin sağlanmaması halinde, deşifre işlemi doğru bir şekilde gerçekleşmez.
    - If inequality is not met, decryption process cannot be carried out correctly.

## Daha güvenli bir RSA şifrelemesi için bazı tüyolar (Some tips for a more secure RSA encryption): 
1) `d > (1/3) * (n**(1/4))` Eşitsizliği sağlanmazsa, şifreleme [Wiener'in saldırısına](https://en.wikipedia.org/wiki/Wiener%27s_attack#small_private_key) karşı zaaflıı olur.
    - If inequality is not met, encryption becomes vulnerable to Wiener's attack.

2) `e`, küçük bir tam sayı olmamalı. Aksi halde şifreleme [Coppersmith'in saldırısına](https://en.wikipedia.org/wiki/Coppersmith's_attack#Low_public_exponent_attack) karşı zaaflı olur.
    - `e`, shouldn't be a small integer. Otherwise encryption becomes vulnerable to Coppermith's attack.

3) `e`, [Fermat](https://en.wikipedia.org/wiki/Fermat_number) asallarından (`Fn = (2**(2**n))+1`, `F0-F4`) olmamalı.
    - `e`, shouldn't be a Fermat prime.

## Kaynakça (References):
- https://en.wikipedia.org/wiki/RSA_(cryptosystem)

<br>

___─ Written by f4T1H ─___
