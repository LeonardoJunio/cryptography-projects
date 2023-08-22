from src.auxiliaries.constants.FileConstants import *

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
    