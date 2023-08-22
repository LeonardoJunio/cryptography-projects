from src.auxiliaries.constants.FileConstants import *
from src.auxiliaries.utils.FileUtil import *
from src.auxiliaries.utils.HashUtil import *
from src.auxiliaries.helper.FileHelper import *

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
                    