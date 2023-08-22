from src.auxiliaries.constants.FileConstants import *
from src.auxiliaries.utils.FileUtil import *
from src.auxiliaries.helper.FileHelper import *
from src.auxiliaries.helper.HashHelper import *

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
        