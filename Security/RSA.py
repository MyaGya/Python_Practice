def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def get_private_key(e, tot):
    k=1
    while (e*k)%tot != 1 or k == e:
        k+=1
    return k

def get_public_key(tot):
    e=2
    while e<totient and gcd(e, totient)!=1:
        e += 1
    return e

# Input message to be encrypted
m = input("Enter the text to be encrypted:")

# Step 1. Choose two prime numbers
p = 13
q = 23

print("Two prime numbers(p and q) are:", str(p), "and", str(q))

# Step 2. Compute n = pq which is the modulus of both the keys
n = p*q
print("n(p*q)=", str(p), "*", str(q), "=", str(n))

# Step 3. Calculate totient
totient = (p-1)*(q-1)
print("(p-1)*(q-1)=", str(totient))

# Step 4. Find public key e
e = get_public_key(totient)
print("Public key(n, e):("+str(n)+","+str(e)+")")

# Step 5. Find private key d
d = get_private_key(e, totient)
print("Private key(n, d):("+str(n)+","+str(d)+")")

# Step 6.Encrypt message
encrypted_msg = encrypt((e,n), m)
print('Encrypted Message:', ''.join(map(lambda x: str(x), encrypted_msg)))

# Step 7.Decrypt message
print('Decrypted Message:', decrypt((d,n),encrypted_msg))

# 출처 https://wkdtjsgur100.github.io/RSA-algorithm/