import os

from src.auxiliaries.constants.FileConstants import *
from src.auxiliaries.constants.ClientConstants import *
from src.auxiliaries.helper.FileHelper import *

# 'object' would be the inheritance, don't need to make it explicit if it's this class
class FileUtil(object):
    def dirBase():
        return os.path.abspath('')

    def updateKey(key: str):
        pathName = FileUtil.dirBase() + FileConstants.PATH_NAME_FILE_KEY

        FileHelper.writeTextFile(pathName, key)

    # Get key from file
    @staticmethod
    def getKey():
        pathName = FileUtil.dirBase() + FileConstants.PATH_NAME_FILE_KEY

        return FileHelper.readTextFile(pathName).strip()
