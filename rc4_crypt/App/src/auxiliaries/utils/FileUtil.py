import os

from src.auxiliaries.constants.FileConstants import *
from src.auxiliaries.helper.FileHelper import *

# 'object' would be the inheritance, don't need to make it explicit if it's this class
class FileUtil(object):
    def dirBase():
        return os.path.abspath('')

    # Get key from file
    @staticmethod
    def getKey():
        pathName = FileUtil.dirBase() + FileConstants.PATH_NAME_FILE_KEY

        return FileHelper.readTextFile(pathName).strip()

    # Get the message from file
    @staticmethod
    def getMessage():
        pathName = FileUtil.dirBase() + FileConstants.PATH_NAME_FILE_MESSAGE

        return FileHelper.readTextFile(pathName).strip()

    # Get the encrypted message from file
    @staticmethod
    def getEncryptedMessage():
        pathName = FileUtil.dirBase() + FileConstants.PATH_NAME_FILE_ENCRYPT

        return FileHelper.readTextFile(pathName).strip()

    # Set the encrypted message in the file
    @staticmethod
    def setEncryptedMessage(messageEncrypted):
        pathName = FileUtil.dirBase() + FileConstants.PATH_NAME_FILE_ENCRYPT

        return FileHelper.writeTextFile(pathName, messageEncrypted)

    # Set the decrypted message in the file
    @staticmethod
    def setDecryptedMessage(messageDecrypted):
        pathName = FileUtil.dirBase() + FileConstants.PATH_NAME_FILE_DECRYPT

        return FileHelper.writeTextFile(pathName, messageDecrypted)
