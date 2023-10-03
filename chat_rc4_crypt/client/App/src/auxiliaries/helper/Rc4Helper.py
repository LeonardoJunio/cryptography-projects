import numpy as np

from src.auxiliaries.utils.Rc4Util import *
from src.auxiliaries.constants.Rc4Constants import *

class Rc4Helper:
    # Encrypt The Message
    def encryptMessage(key, message):
        key = Rc4Util.convertStrDec(key)
        message = Rc4Util.convertStrDec(message)

        # Perform the KSA algorithm
        Rc4Helper.algorithmKsa(key)

        # Perform PRGA algorithm
        keyStream = Rc4Helper.algorithmPrga(message)

        # np.array: Converts [86, 96, 116] to [86  96 116]
        # It's not necessary in this case, if the XOR was done with the complete string
        # outside the loop, it might be necessary.
        # keyStream = np.array(keyStream)

        messageDecrypted = Rc4Util.convertDecHex(keyStream)

        return messageDecrypted

    # Decrypt The Message
    def decryptMessage(key, message):
        key = Rc4Util.convertStrDec(key)
        message = Rc4Util.convertHexDec(message)

        # Perform the KSA algorithm
        Rc4Helper.algorithmKsa(key)

        # Perform PRGA algorithm
        keyStream = Rc4Helper.algorithmPrga(message)

        messageEncrypted = Rc4Util.convertDecStr(keyStream)

        return messageEncrypted

    # Key Scheduling Algorithm(KSA):
    # It is used to generate a State array by applying a permutation
    # using a variable-length key consisting of 0 to 256 bytes.
    def algorithmKsa(key):
        # S[] is permutation of 0, 1, ..., 255
        S = list(range(Rc4Constants.QTY_MAX_BYTES_KEY))
        lenKey = len(key)
        j = 0

        for i in range(Rc4Constants.QTY_MAX_BYTES_KEY):
            numberCharMessage = key[i % lenKey]
            j = (j + S[i] + numberCharMessage) % Rc4Constants.QTY_MAX_BYTES_KEY
            S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm(PRGA):
    # It used to generate keystream byte from State vector array
    # after one more round of permutation
    def algorithmPrga(message):
        # S[] is permutation of 0, 1, ..., 255
        S = list(range(Rc4Constants.QTY_MAX_BYTES_KEY))
        i = j = 0
        keyStream = []

        for char in message:
            i = (i+1) % Rc4Constants.QTY_MAX_BYTES_KEY
            j = (j+S[i]) % Rc4Constants.QTY_MAX_BYTES_KEY
            S[i], S[j] = S[j], S[i]
            # Generated key stream
            K = S[(S[i] + S[j]) % Rc4Constants.QTY_MAX_BYTES_KEY]
            # Performing XOR between char and generated key stream
            keyStream.append(char ^ K)

        return keyStream
