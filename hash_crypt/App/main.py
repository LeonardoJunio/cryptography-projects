import os
import hashlib

class FileConstants:
    PATH_TEXTS = '/files/texts'
    PATH_HASHS = '/files/hashs'

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
    def saveHashFile(arquivo, mensagemHash):
        hashPath = FileUtil.dirFilesHash()
        # salva o arquivo com a informacao do hash e o caminho
        arquivoSaida = open((hashPath + '/' + arquivo + 'hash'), 'w')
        arquivoSaida.write(mensagemHash)
        arquivoSaida.close()
    
class HashHelper:
    def createHashFiles(path, file):
        if (file[-3::] == '.py'):  # not the code files
            return

        if (file[-4::] == 'hash'):  # not the hash files
            print('Arquivo ' + file + ' já consta o file hash')
            return

        diretorio = path+'/'+file  # path mais nome do file
        arq = open((diretorio), 'r')
        mensagem = arq.read()

        texto = diretorio + mensagem
        mensagemHash = HashUtil.generateTextHashMd5(texto)

        FileHelper.saveHashFile(file, mensagemHash)
    
    def validateAllTextHash(nomeArquivo, pathTextOriginal):
        pathHashs = FileUtil.dirFilesHash()

        for caminhoH, diretoriosH, arquivosH in os.walk(pathHashs):
            for arquivoH in arquivosH:
                if (arquivoH != (nomeArquivo+'hash')):  # checking those that contain the hash data
                    continue

                caminhototalH = caminhoH+'/'+arquivoH
                arqH = open((caminhototalH), 'r')
                mensagemArq = arqH.read()

                if (mensagemArq == HashUtil.generateTextHashMd5(pathTextOriginal)):
                    print('Arquivo ' + nomeArquivo + ' continua o mesmo.')
                else:
                    print('Arquivo ' + nomeArquivo + ' foi alterado.')

class HashCrypt:
    def __init__(self):
        option:str = input('Please enter an option: (-i / -t / -x): ')

        if (option == '-i'):
            self.hashFiles()
        elif (option == '-t'):
            self.checkFiles()
        elif (option == '-x'):
            self.deleteHash()
        else:
            print('No valid option.')
        
    def hashFiles(self):
        pathTexts = FileUtil.dirFilesText()

        # verifica os arquivos de acordo com o caminho, pastas e arquivo
        for path, dirs, files in os.walk(pathTexts):
            for file in files:
                HashHelper.createHashFiles(path, file)

        print('Registro de guarda concluido.')

    def checkFiles(self):
        pathTexts = FileUtil.dirFilesText()

        for (path, dirs, files) in os.walk(pathTexts):
            for file in files:
                # check that it's not the hash files or the code
                if (file[-4::] == 'hash' or file[-3::] == '.py'):
                    continue

                pathTotal = path+'/'+file
                arq = open((pathTotal), 'r')
                mensagemOri = arq.read()
                nomeArquivo = file
                pathTextOriginal = pathTotal + mensagemOri

                HashHelper.validateAllTextHash(nomeArquivo, pathTextOriginal)

        print('Verificação concluída.')

    def deleteHash(self):  # removes the guard and hash files
        absolutePath = FileUtil.dirFilesHash()

        for (path, dirs, files) in os.walk(absolutePath):
            for file in files:
                if (file[-4::] != 'hash'):
                    continue

                FileUtil.deleteFile(path + '/' + file)

        print('Hash structure excluded.')




HashCrypt()