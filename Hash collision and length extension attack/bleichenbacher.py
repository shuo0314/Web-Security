from roots import *
from Crypto.Hash import SHA
import sys
#message = sys.argv[1]

message="cis551+jdoe+1.23"
digest = str(SHA.new(bytes(message, encoding='utf-8')).hexdigest())
ASN = "3021300906052B0E03021A05000414"
D = "00" + ASN + digest
prefix = "0001"+"F"*24 #218byte = 436 F
garbage = "F"*412

new_message = prefix+D+garbage
new_message_int = int(new_message, base=16)

cube_root, is_exact = integer_nthroot(new_message_int, 3)
print(integer_to_base64(cube_root).decode())