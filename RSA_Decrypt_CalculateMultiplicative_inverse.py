import sys
from sympy.ntheory import factorint
from builtins import int
from pyDes import des

def multiplicative_inverse(a, b):
    origA = a
    X = 0
    prevX = 1
    Y = 1
    prevY = 0
    while b != 0:
        temp = b
        quotient = a/b
        b = a%b
        a = temp
        temp = X
        X = prevX - quotient * X
        prevX = temp
        temp = Y
        Y = prevY - quotient * Y
        prevY = temp

    return origA + prevX


n = "5b0994b428ed522436b5"
e = "3c2cc83edc2c0c85dd19"
DES = "0x42106384e36f49972d7"
DES2 = "3a1dafd4a78f8fb51d7a27901ec8b463"

DES3 = int(DES2,16)

n2 = int(n,16)
str(n2)

e2 = int(e,16)
str(e2)

DES = int(DES,0)
str(DES)

hexx = hex(365323976857872451486801)

print (DES)

print(("n är = "), n2, (" e är = "), e2, "DES är: ", DES)
print(("inverse is "), multiplicative_inverse(284168074923759821511961, 429912085870883231402220))
print(factorint(n2))

