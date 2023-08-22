import hashlib

class HashUtil:
    # hash coding of message and path
    def generateTextHashMd5(texto: str):
        return hashlib.md5(str(texto).encode('utf-8')).hexdigest()
