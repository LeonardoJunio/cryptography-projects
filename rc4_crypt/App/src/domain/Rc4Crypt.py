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

class Rc4Crypt:
    def __init__(self):
        try:
            menuOption: int = int(
                input('Do you want to encrypt(1) or decrypt(2): '))

            match menuOption:
                case 1:
                    self.encrypt()
                case 2:
                    self.decrypt()
                case _:
                    print('Invalid option.')
        except Exception as err:
            print("Unexpected error:", err)

    def encrypt(self):
        message = FileUtil.getMessage()
        key = FileUtil.getKey()

        print('Message: ', message)

        messageEncrypted = Rc4Helper.encryptMessage(key, message)
        print('Encrypted Message: ', messageEncrypted)

        FileUtil.setEncryptedMessage(messageEncrypted)

    def decrypt(self):
        messageEncrypted = FileUtil.getEncryptedMessage()
        key = FileUtil.getKey()

        print('Encrypted Message: ', messageEncrypted)

        messageDecrypted = Rc4Helper.decryptMessage(key, messageEncrypted)
        print('Decrypted Message: ', messageDecrypted)

        FileUtil.setDecryptedMessage(messageDecrypted)
