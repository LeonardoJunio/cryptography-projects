import os
import hashlib

class FileConstants:
    PATH_TEXTS = '/files/texts'
    PATH_HASHS = '/files/hashs'
    HASH_SUFFIX = 'hash'

# 'object' would be the inheritance, don't need to make it explicit if it's this class
class FileUtil(object):
    def dirBase():
        return os.path.abspath('')
    
    @staticmethod
    def dirFilesText():
        return FileUtil.dirBase() + FileConstants.PATH_TEXTS
    
    @staticmethod
    def dirFilesHash():
        return FileUtil.dirBase() + FileConstants.PATH_HASHS
    
    @staticmethod
    def deleteFile(pathFile: str):
        os.remove(pathFile)
    
class HashUtil:    
    # hash coding of message and path
    def generateTextHashMd5(texto: str):
        return hashlib.md5(str(texto).encode('utf-8')).hexdigest()
    
class FileHelper:    
    def saveMessageFile(path: str, file: str, text: str):
        outputPath = path + '/' + file + FileConstants.HASH_SUFFIX
        
        try:
            outputFile = open((outputPath), 'w')
            
            try:
                outputFile.write(text)        
            except:
                print("Something went wrong when writing to the file.")
            finally:
                outputFile.close()        
        except:
            print("Something went wrong when opening the file") 
    
    def getAllTextFile(path: str) -> str:
        if not path:
            raise Exception("Path is empty") 
        
        file = open((path), 'r')
        fileText = file.read()
        file.close() 
        
        return fileText;
    
    def getLineTextFile(path: str) -> str:
        if not path:
            raise Exception("Path is empty") 
        
        file = open((path), 'r')
        fileLineText = file.readline()
        file.close() 
        
        return fileLineText;
    
class HashHelper:
    def createHashFiles(path, file):
        if (file[-3::] == '.py'):  # not the code files
            return

        if (file[-4::] == FileConstants.HASH_SUFFIX):  # not the hash files
            print('File ' + file + ' is already a hash file.')
            return

        pathFile = path + '/' + file
        message = FileHelper.getAllTextFile(pathFile)        
        pathFileMessage = pathFile + message
        pathFileMessageHash = HashUtil.generateTextHashMd5(pathFileMessage)

        pathHashs = FileUtil.dirFilesHash()        
        # saves the file with the hash information and the path
        FileHelper.saveMessageFile(pathHashs, file, pathFileMessageHash)
    
    def validateAllTextHash(file, pathFileMessage):
        pathHashs = FileUtil.dirFilesHash()

        for (pathHash, dirsHash, filesHash) in os.walk(pathHashs):
            for fileHash in filesHash:
                # checking those that contain the hash data
                if (fileHash != (file + FileConstants.HASH_SUFFIX)):
                    continue

                pathFileHash = pathHash + '/' + fileHash
                originalMessage = FileHelper.getAllTextFile(pathFileHash)
                
                if (originalMessage == HashUtil.generateTextHashMd5(pathFileMessage)):
                    print('File ' + file + ' remains the same.')
                else:
                    print('File ' + file + ' has been changed.')

class HashCrypt:
    def __init__(self):
        option:str = input('Please enter an option: (-i / -t / -x): ')

        try:
            if (option == '-i'):
                self.hashFiles()
            elif (option == '-t'):
                self.checkFiles()
            elif (option == '-x'):
                self.deleteHash()
            else:
                print('No valid option.')
        except Exception as err:
            print("Unexpected error:", err)
            # print(f"Unexpected {err=}")            
        
    def hashFiles(self):
        pathTexts = FileUtil.dirFilesText()

        for path, dirs, files in os.walk(pathTexts):
            for file in files:
                HashHelper.createHashFiles(path, file)

        print('Guard registration completed.')

    def checkFiles(self):
        pathTexts = FileUtil.dirFilesText()

        for (path, dirs, files) in os.walk(pathTexts):
            if not files:
                print("There are no files.")
                return
  
            for file in files:
                # check that it's not the hash files or the code
                if (file[-4::] == FileConstants.HASH_SUFFIX or file[-3::] == '.py'):
                    continue

                pathFile = path + '/' + file
                originalMessage = FileHelper.getAllTextFile(pathFile)
                pathFileMessage = pathFile + originalMessage

                HashHelper.validateAllTextHash(file, pathFileMessage)

        print('Check completed.')

    def deleteHash(self):  # removes the guard and hash files
        absolutePath = FileUtil.dirFilesHash()

        for (path, dirs, files) in os.walk(absolutePath):
            for file in files:
                if (file[-4::] != FileConstants.HASH_SUFFIX):
                    continue

                FileUtil.deleteFile(path + '/' + file)

        print('Hash structure excluded.')




HashCrypt()