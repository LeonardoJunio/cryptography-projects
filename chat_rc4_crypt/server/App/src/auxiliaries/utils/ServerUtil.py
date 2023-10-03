from src.auxiliaries.constants.ServerConstants import *

# 'object' would be the inheritance, don't need to make it explicit if it's this class
class ServerUtil(object):
    @staticmethod
    def convertStrBytes(text: str, prefix: bool = True) -> bytes:
        if (prefix):
            text = ServerConstants.TEXT_PREFIX + text

        return bytes(text, ServerConstants.TEXT_ENCODE_SEND)
