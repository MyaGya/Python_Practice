import sha3


data='maydata'
s=sha3.sha3_224(data.encode('utf-8')).hexdigest()
print(s)
data='maydata'
s=sha3.sha3_384(data.encode('utf-8')).hexdigest()
print(s)
data='maydata'
s=sha3.sha3_512(data.encode('utf-8')).hexdigest()
print(s)

