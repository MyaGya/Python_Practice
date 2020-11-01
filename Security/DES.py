from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA


def make8String(msg):  # 인자를 8의 배수로 맞춘다
    msglen = len(msg)
    filler = ''
    if msglen % 8 != 0:
        filler = '0' * (8 - msglen % 8)

    msg += filler
    return msg.encode('utf-8')  # 기본 메세지를 8배수로 맞춘 값도 utf-8 값으로 변경하여 연산합니다.


class myDES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:24]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:8]

    def enc(self, plaintext):
        plaintext = make8String(plaintext)
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        encmsg = des3.encrypt(plaintext)

        return encmsg

    def dec(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decmsg = des3.decrypt(ciphertext)

        return decmsg


if __name__ == '__main__':
    keytext = 'iloveyou'
    ivtext = '1234'
    msg = 'asi1821s'

    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)

    print(f"Original   : \t{msg}")
    print(f"Ciphered   : \t{ciphered}")
    print(f"Deciphered : \t{deciphered}")
