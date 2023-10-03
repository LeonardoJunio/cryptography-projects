from src.auxiliaries.constants.ClientConstants import *

class ClientUtil:
    @staticmethod
    def convertStrBytes(text: str) -> bytes:
        return bytes(text, ClientConstants.TEXT_ENCODE_SEND)

    def clearInputField(tkMsgStrVar):
        tkMsgStrVar.set("")
