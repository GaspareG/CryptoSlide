#!/bin/python3

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def decrypt(c, e, n):
  return pow(c,e,n)
#  return (c**e) % n

p = 27789079547
q = 28188776653
n = p*q
phi = (p-1)*(q-1)
e = 653
d = modinv(e, phi)

print(d, e, phi)

check = (e*d) % phi

print( check )

C = [309117097659990665453,125675338953457551017,524099092120785248852,772538252438953530955,547462544172248492882,28215860448757441963,543018082275730030658,585936545563088067075,131807465077304821584]


for c in C:
  print( hex(decrypt(c, d, n)) )

