class Rc4Util(object):
    # Returns a list of the numbers representing each character in the text
    @staticmethod
    def convertStrDec(text) -> list:
        result = []

        for char in text:
            # Returns an integer representing the Unicode character (string to decimal)
            result.append(ord(char))

        return result

    # Returns a string, which each character represents a number on the list
    @staticmethod
    def convertDecStr(list) -> str:
        result = ''

        for char in list:
            # Converts an integer to its Unicode character (decimal to string)
            result += chr(char)

        return result

    # Returns a list, which each element represents a number (decimal) of the hexadecimal
    @staticmethod
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
    @staticmethod
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
