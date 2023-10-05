from src.auxiliaries.utils.SteganographyUtil import *
from src.domain.services.SteganographyService import *


class SteganographyCrypt:
    def __init__(self):
        option = int(input('Do you wish to encrypt(1) or decrypt(2):'))

        if (option == 1):
            SteganographyCrypt.encryptMessage()
        elif (option == 2):
            SteganographyCrypt.decryptMessage()
        else:
            print('Invalid option.')

    def encryptMessage():
        message = SteganographyUtil.getMessageFile()
        image = SteganographyUtil.readImageCrypt()

        SteganographyService.insertMessageImage(message, image)

        print('Encrypted message created.')

    def decryptMessage():
        imageEncrypted = SteganographyUtil.readImageEncrypt()

        messageDecrypted = SteganographyService.extractSaveMessageImage(
            imageEncrypted)

        print("Decrypted message: ", messageDecrypted)
