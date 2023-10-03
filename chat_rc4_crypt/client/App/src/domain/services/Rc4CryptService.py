from src.auxiliaries.constants.FileConstants import *
from src.auxiliaries.utils.FileUtil import *
from src.auxiliaries.helper.FileHelper import *
from src.auxiliaries.helper.Rc4Helper import *

# RC4 is a symmetric stream cipher and variable key length algorithm.
# This symmetric key algorithm is used identically for encryption and decryption
# such that the data stream is simply XORed with the generated key sequence.
# The algorithm is serial as it requires successive exchanges of state entries
# based on the key sequence. The algorithm works in two phases:
# Key Scheduling Algorithm(KSA) and Pseudo-Random Generation Algorithm(PRGA)

class Rc4CryptService:
    def encrypt(message):
        key = FileUtil.getKey()

        return Rc4Helper.encryptMessage(key, message)

    def decrypt(messageEncrypted):
        key = FileUtil.getKey()

        return Rc4Helper.decryptMessage(key, messageEncrypted)
