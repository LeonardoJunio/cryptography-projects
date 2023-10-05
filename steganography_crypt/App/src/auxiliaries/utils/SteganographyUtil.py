from src.auxiliaries.constants.SteganographyConstants import *
from src.auxiliaries.constants.FileConstants import *
from src.auxiliaries.helper.FileHelper import *
from src.auxiliaries.helper.ImageHelper import *
from src.auxiliaries.utils.SteganographyUtil import *


class SteganographyUtil:
    def getBinaryFromChar(char: str) -> str:
        int = SteganographyUtil.getIntFromChar(char)
        return SteganographyUtil.getBinaryFromInt(int)

    def getBinaryFromInt(int: int) -> str:
        # bin: Return the binary representation of an integer
        # [2::]: Because the return follows the style: 0b1010..., so remove the '0b'
        # zfill: Pad a numeric string with zeros on the left
        return bin(int)[2::].zfill(SteganographyConstant.BINARY_QTY_BYTES)

    def getIntFromChar(char: str) -> int:
        # ord: Returns an integer representing the Unicode character
        return ord(char)

    def getCharFromBinary(strBinary: str) -> int:
        # strBinary with 8 bytes
        return chr(int(strBinary, 2))

    def convertStrToBinary(text):
        binary = ''

        for char in text:
            binary += SteganographyUtil.getBinaryFromChar(char)

        binary += SteganographyConstant.STOP_CONDITION

        return binary

    def convertBinaryToStr(binary):
        strBinary = ''
        text = ''

        for byte in binary:
            strBinary += byte

            if (len(strBinary) == SteganographyConstant.BINARY_QTY_BYTES):
                text += SteganographyUtil.getCharFromBinary(strBinary)

                strBinary = ''

        return text

    def saveMessageDecryptedFile(messageDecrypted):
        FileHelper.saveTextFile(
            FileConstants.FILE_MESSAGE_OUTPUT, messageDecrypted)

    def getMessageFile():
        return FileHelper.readTextFile(FileConstants.FILE_MESSAGE_INPUT).strip()

    def readImageCrypt():
        return ImageHelper.readImage(FileConstants.FILE_IMAGE_INPUT)

    def readImageEncrypt():
        return ImageHelper.readImage(FileConstants.FILE_IMAGE_OUTPUT)

    def saveImageCrypt(image):
        return ImageHelper.writeImage(FileConstants.FILE_IMAGE_OUTPUT, image)
