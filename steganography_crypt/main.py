from PIL import Image
import numpy as np
import cv2

# It will be used as a stop condition in the steganography process
STOP_CONDITION = "00000000"
BINARY_QTY_BYTES = 8


def getBinaryFromChar(char: str) -> str:
    int = getIntFromChar(char)
    return getBinaryFromInt(int)


def getBinaryFromInt(int: int) -> str:
    # bin: Return the binary representation of an integer
    # zfill: Pad a numeric string with zeros on the left
    return bin(int)[2::].zfill(BINARY_QTY_BYTES)


def getIntFromChar(char: str) -> int:
    # ord: Returns an integer representing the Unicode character
    return ord(char)


def getCharFromBinary(strBinary: str) -> int:
    # strBinary with 8 bytes
    return chr(int(strBinary, 2))


def convertStrToBinary(text):
    binary = ''

    for char in text:
        binary += getBinaryFromChar(char)

    binary += STOP_CONDITION

    return binary


def convertBinaryToStr(binary):
    strBinary = ''
    text = ''

    for byte in binary:
        strBinary += byte

        if (len(strBinary) == BINARY_QTY_BYTES):
            text += getCharFromBinary(strBinary)

            strBinary = ''

    return text

# Update te components of pixel colors RGB with the message byte
def updatePixelColorWithByteMsg(componentRgb, byteText):
    # Takes the original 8 bytes of each color
    componentBinary = bin(componentRgb)[2::].zfill(8)
    # Changes the last byte of each color with the bytes of the message
    return int(componentBinary[0:7] + byteText, 2)


def updateImageMessage(image, binaryMsg):
    indexMsg = 0

    for height in image:
        for width in height:
            # An attempt was made with a loop iterating 'width', but it was unsuccessful
            # Element 0 is Red, element 1 is Green, element 2 is Blue
            if (indexMsg >= len(binaryMsg)):
                return

            width[0] = updatePixelColorWithByteMsg(
                width[0], binaryMsg[indexMsg])
            indexMsg += 1

            if (indexMsg >= len(binaryMsg)):
                return

            width[1] = updatePixelColorWithByteMsg(
                width[1], binaryMsg[indexMsg])
            indexMsg += 1

            if (indexMsg >= len(binaryMsg)):
                return

            width[2] = updatePixelColorWithByteMsg(
                width[2], binaryMsg[indexMsg])
            indexMsg += 1


def extractBinaryImage(image) -> str:
    binaryMessage = ''
    byteMessage = 0

    for height in image:
        for width in height:
            for componentRgb in width:
                binaryMessage += bin(componentRgb)[2::].zfill(8)[7]

                if (binaryMessage[-8::] == STOP_CONDITION):
                    return binaryMessage

                if (byteMessage == BINARY_QTY_BYTES):
                    byteMessage = 0
                    break

                byteMessage += 1

    return ""


def insertMessageImage(text, image):
    binaryMsg = convertStrToBinary(text)

    # Image is an object, so it is passed as a reference,
    # i.e. it is changed internally in the method
    updateImageMessage(image, binaryMsg)

    saveImageCrypt(image)


def extractSaveMessageImage(image):
    binaryMessage = extractBinaryImage(image)
    messageDecrypted = convertBinaryToStr(binaryMessage)
    
    saveMessageDecryptedFile(messageDecrypted)
    
    return messageDecrypted.strip()







def saveMessageDecryptedFile(messageDecrypted):
    saveTextFile('mensagemSaida.txt', messageDecrypted)
    
def getMessageFile():
    return readTextFile('mensagem.txt').strip()







def saveTextFile(pathName, text):
    fileOutput = open(pathName, 'w')
    fileOutput.write(text)
    fileOutput.close()
    
def readTextFile(pathName):    
    fileText = open(pathName, 'r')
    text = fileText.read()
    fileText.close()
    
    return text



def readImageCrypt():
    return readImage('imd.bmp')

def readImageEncrypt():
    return readImage('imdM.bmp')

def saveImageCrypt(image):
    return writeImage('imdM.bmp', image)



def readImage(fileNameImage):
    return cv2.imread(fileNameImage)

def writeImage(fileNameImage, image):
    return cv2.imwrite('imdM.bmp', image)





option = int(input('Do you wish to encrypt(1) or decrypt(2):'))

if (option == 1):
    message = getMessageFile()
    image = readImageCrypt()

    insertMessageImage(message, image)

    print('Encrypted message created.')
elif (option == 2):
    imageEncrypted = readImageEncrypt()
    
    messageDecrypted = extractSaveMessageImage(imageEncrypted)

    print("Decrypted message: ", messageDecrypted)
else:
    print('Invalid option.')
