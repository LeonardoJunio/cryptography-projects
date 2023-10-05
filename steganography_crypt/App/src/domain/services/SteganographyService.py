from src.auxiliaries.utils.SteganographyUtil import *
from src.auxiliaries.helper.SteganographyHelper import *


class SteganographyService:
    def insertMessageImage(text, image):
        binaryMsg = SteganographyUtil.convertStrToBinary(text)

        # Image is an object, so it is passed as a reference,
        # i.e. it is changed internally in the method
        SteganographyHelper.updateImageMessage(image, binaryMsg)

        SteganographyUtil.saveImageCrypt(image)

    def extractSaveMessageImage(image):
        binaryMessage = SteganographyHelper.extractBinaryImage(image)
        messageDecrypted = SteganographyUtil.convertBinaryToStr(binaryMessage)

        SteganographyUtil.saveMessageDecryptedFile(messageDecrypted)

        return messageDecrypted.strip()
