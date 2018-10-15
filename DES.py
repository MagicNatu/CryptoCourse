from Crypto.Cipher import DES
from Crypto.Util import number
import base64
from base64 import b64decode
from builtins import int
import binascii
import codecs
from mpmath.libmp.six import int2byte


bytestring = number.long_to_bytes(937643650242,8)
sas = binascii.hexlify(bytestring)

ll = 937643650242

v = int.to_bytes(8, ll)

#a = codecs.encode(ll, 'bytes')

print (bytestring)
print (sas)
print (v)

key= b'\x00\x00\x00\xdaO\xea\xac\xc2'


des = DES.new(key, DES.MODE_ECB)
fo = open('C:\\file5-36277.enc', 'r')
a = des.decrypt(fo)



#encrypted_key = "19498656680071858320087 "
#decrypted_text = des.decrypt(encrypted_key)

#print (decrypted_text)

