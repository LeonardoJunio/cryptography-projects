import numpy as np

QTY_MAX_BYTES_KEY = 256
PATH_NAME_FILE_KEY = 'key.txt'
PATH_NAME_FILE_MESSAGE = 'message.txt'
PATH_NAME_FILE_ENCRYPT = 'messageEncrypted.txt'
PATH_NAME_FILE_DECRYPT = 'messageDecrypted.txt'

# Returns a list of the numbers representing each character in the text
def convertStrDec(text) -> list:
    result = []

    for char in text:
        # Returns an integer representing the Unicode character (string to decimal)
        result.append(ord(char))

    return result

# Returns a string, which each character represents a number on the list
def convertDecStr(list) -> str:
    result = ''

    for char in list:
        # Converts an integer to its Unicode character (decimal to string)
        result += chr(char)

    return result

# Returns a list, which each element represents a number (decimal) of the hexadecimal
def convertHexDec(text) -> list:
    result = []

    # Loop that iterates every 2
    for i in range(0, len(text), 2):
        # Suffix according to procedure in convertDecHex
        hexSuffix = text[i:i+2]
        decimalHex = int('0x' + hexSuffix, 16)
        result.append(decimalHex)  # hex para decimal

    return result

# Returns a string, which is composed of the concatenation of part of the hexadecimal
def convertDecHex(text) -> str:
    result = ''

    # Works with 0x0 to 0x99
    for item in text:
        # Converts an integer to the corresponding hexadecimal number (decimal to hex)
        # Takes the characters after '0x'
        hexSuffix = hex(item)[2:]

        # Add '0' when only 1 number (0x9 ->0x09)
        # Ternary: a if condition else b
        result += ('0' + hexSuffix) if (len(hexSuffix) == 1) else hexSuffix

    return result


# Key Scheduling Algorithm(KSA): 
# It is used to generate a State array by applying a permutation 
# using a variable-length key consisting of 0 to 256 bytes. 
def algorithmKsa(key):
    # S[] is permutation of 0, 1, ..., 255
    S = list(range(QTY_MAX_BYTES_KEY))
    lenKey = len(key)
    j = 0
    
    for i in range(QTY_MAX_BYTES_KEY):
        numberCharMessage = key[i % lenKey]
        j = (j + S[i] + numberCharMessage) % QTY_MAX_BYTES_KEY
        S[i], S[j] = S[j], S[i]

# Pseudo-Random Generation Algorithm(PRGA): 
# It used to generate keystream byte from State vector array 
# after one more round of permutation
def algorithmPrga(message):
    # S[] is permutation of 0, 1, ..., 255
    S = list(range(QTY_MAX_BYTES_KEY))
    i = j = 0
    keyStream = []

    for char in message:
        i = (i+1) % QTY_MAX_BYTES_KEY
        j = (j+S[i]) % QTY_MAX_BYTES_KEY
        S[i], S[j] = S[j], S[i]
        # Generated key stream
        K = S[(S[i] + S[j]) % QTY_MAX_BYTES_KEY]
        # Performing XOR between char and generated key stream
        keyStream.append(char ^ K)
        
    return keyStream

# Encrypt The Message
def encryptMessage(key, message):
    key = convertStrDec(key)
    message = convertStrDec(message)
    
    # Perform the KSA algorithm
    algorithmKsa(key)         
    
    # Perform PRGA algorithm
    keyStream = algorithmPrga(message)
    
    # np.array: Converts [86, 96, 116] to [86  96 116]
    # It's not necessary in this case, if the XOR was done with the complete string 
    # outside the loop, it might be necessary.
    # keyStream = np.array(keyStream)    
    
    messageDecrypted = convertDecHex(keyStream)
    
    return messageDecrypted

# Decrypt The Message
def decryptMessage(key, message):
    key = convertStrDec(key)
    message = convertHexDec(message)
    
    # Perform the KSA algorithm
    algorithmKsa(key)        
        
    # Perform PRGA algorithm
    keyStream = algorithmPrga(message)

    messageEncrypted = convertDecStr(keyStream)
    
    return messageEncrypted

# Get key from file
def getKey():
    return readTextFile(PATH_NAME_FILE_KEY).strip()

# Get the message from file
def getMessage():
    return readTextFile(PATH_NAME_FILE_MESSAGE).strip()

# Get the encrypted message from file
def getEncryptedMessage():
    return readTextFile(PATH_NAME_FILE_ENCRYPT).strip()

# Read the message from file
def readTextFile(pathNameFile):
    file = open(pathNameFile, 'r')
    text = file.read()
    file.close()

    return text

# Write the message in the file
def writeTextFile(pathNameFile, text):
    file = open(pathNameFile, 'w')
    file.write(text)
    file.close()



# RC4 is a symmetric stream cipher and variable key length algorithm. 
# This symmetric key algorithm is used identically for encryption and decryption 
# such that the data stream is simply XORed with the generated key sequence. 
# The algorithm is serial as it requires successive exchanges of state entries 
# based on the key sequence. The algorithm works in two phases: 
# Key Scheduling Algorithm(KSA) and Pseudo-Random Generation Algorithm(PRGA)

menuOption = int(input('Do you want to encrypt(1) or decrypt(2): '))

match menuOption:
    case 1:
        message = getMessage()
        key = getKey()

        print('Message: ', message)

        messageEncrypted = encryptMessage(key, message)
        print('Encrypted Message: ', messageEncrypted)

        writeTextFile(PATH_NAME_FILE_ENCRYPT, messageEncrypted)
    case 2:
        messageEncrypted = getEncryptedMessage()
        key = getKey()

        print('Encrypted Message: ', messageEncrypted)

        messageDecrypted = decryptMessage(key, messageEncrypted)
        print('Decrypted Message: ', messageDecrypted)

        writeTextFile(PATH_NAME_FILE_DECRYPT, messageDecrypted)
    case _:
        print('Invalid option.')
