from Crypto.Cipher import DES
import base64
from base64 import b64decode
import binascii
import sys  
from builtins import int


#key = b'365323976857872451486801'
#des = DES.new(key)
#encrypted_key = "19498656680071858320087"

j = hex(937643650242)
print (j)

d = int(' DA4FEAACC2', 16)


def convert_hex_to_ascii(h):
    chars_in_reverse = []
    while h != 0x0:
        chars_in_reverse.append(chr(h & 0xFF))
        h = h >> 8

    chars_in_reverse.reverse()
    return ''.join(chars_in_reverse)

print (convert_hex_to_ascii(d))

