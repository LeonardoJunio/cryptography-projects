class FileHelper:
    def saveTextFile(pathName, text):
        fileOutput = open(pathName, 'w')
        fileOutput.write(text)
        fileOutput.close()

    def readTextFile(pathName):
        fileText = open(pathName, 'r')
        text = fileText.read()
        fileText.close()

        return text
