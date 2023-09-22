class FileHelper:
    # Read the message from file
    @staticmethod
    def readTextFile(pathNameFile):
        file = open(pathNameFile, 'r')
        text = file.read()
        file.close()

        return text

    # Write the message in the file
    @staticmethod
    def writeTextFile(pathNameFile, text):
        file = open(pathNameFile, 'w')
        file.write(text)
        file.close()
