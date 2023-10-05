from src.auxiliaries.constants.SteganographyConstants import *
from src.auxiliaries.helper.SteganographyHelper import *
from src.auxiliaries.utils.SteganographyUtil import *


class SteganographyHelper:
    # Update te components of pixel colors RGB with the message byte
    def updatePixelColorWithByteMsg(componentRgb, byteText):
        # Takes the original 8 bytes of each color
        componentBinary = SteganographyUtil.getBinaryFromInt(componentRgb)
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

                width[0] = SteganographyHelper.updatePixelColorWithByteMsg(
                    width[0], binaryMsg[indexMsg])
                indexMsg += 1

                if (indexMsg >= len(binaryMsg)):
                    return

                width[1] = SteganographyHelper.updatePixelColorWithByteMsg(
                    width[1], binaryMsg[indexMsg])
                indexMsg += 1

                if (indexMsg >= len(binaryMsg)):
                    return

                width[2] = SteganographyHelper.updatePixelColorWithByteMsg(
                    width[2], binaryMsg[indexMsg])
                indexMsg += 1

    def extractBinaryImage(image) -> str:
        binaryMessage = ''
        byteMessage = 0

        for height in image:
            for width in height:
                for componentRgb in width:
                    binaryMessage += SteganographyUtil.getBinaryFromInt(componentRgb)[7]

                    if (binaryMessage[-8::] == SteganographyConstant.STOP_CONDITION):
                        return binaryMessage

                    if (byteMessage == SteganographyConstant.BINARY_QTY_BYTES):
                        byteMessage = 0
                        break

                    byteMessage += 1

        return ""
