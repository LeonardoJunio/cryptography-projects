import os

from src.auxiliaries.constants.FileConstants import *

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
