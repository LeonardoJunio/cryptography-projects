import os
import hashlib

'''
Esse programa no momento de envio ainda não esta funcionando via linha de comando como foi pedido.
'''

def hash():
    caminhoAbsoluto = os.path.abspath('')
    for caminho, diretorios, arquivos in os.walk(caminhoAbsoluto):#verifica os arquivos de acordo com o caminho, pastas e arquivo
        for arquivo in arquivos:
            if(arquivo[-3::]!='.py'):
                if (arquivo[-4::]!='hash'):            
                    caminhototal = caminho+'/'+arquivo#caminho mais nome do arquivo
                    arq = open((caminhototal), 'r')
                    mensagem = arq.read()
                    diretorio = caminhototal
                    mensagemHash = hashlib.md5(str(diretorio+mensagem).encode('utf-8')).hexdigest()#codificacao hash da mensagem e do caminho
                    
                    arquivoSaida = open((arquivo+'hash'), 'w')#salva o arquivo com a informacao do hash e o caminho
                    arquivoSaida.write(mensagemHash)
                    arquivoSaida.close()
                else: #nao sao os arquivos hash nem o codigo
                    print('Arquivo ' + arquivo + ' já consta o arquivo hash')
    
    print('Registro de guarda concluido.')


def verifica():
    caminhoAbsoluto = os.path.abspath('')
    for caminho, diretorios, arquivos in os.walk(caminhoAbsoluto):      
        mensagemOri = ''
        nomeArquivo = ''
        diretorio = ''
        
        for arquivo in arquivos:
            if (arquivo[-4::]!='hash' and arquivo[-3::]!='.py'): #verifica se nao sao os arquivos hash nem o codigo
                caminhototal = caminho+'/'+arquivo
                arq = open((caminhototal), 'r')
                mensagemOri = arq.read()  
                nomeArquivo = arquivo
                diretorio = caminhototal
                
                for caminhoH, diretoriosH, arquivosH in os.walk(caminhoAbsoluto):
                    for arquivoH in arquivosH:
                        if(arquivoH==(nomeArquivo+'hash')): #verifando os que contem os dados hash
                            caminhototalH = caminhoH+'/'+arquivoH
                            arqH = open((caminhototalH), 'r')
                            mensagemArq = arqH.read()
                            
                            if(mensagemArq == hashlib.md5(str(diretorio + mensagemOri).encode('utf-8')).hexdigest()):
                                print('Arquivo ' + nomeArquivo + ' continua o mesmo.')
                            else:
                                print('Arquivo ' + nomeArquivo + ' foi alterado.')
    
    print('Verificação concluida.')
    
    
def exclui(): #remove a guarda e os arquivos hash
    caminhoAbsoluto = os.path.abspath('')
    for caminhoH, diretoriosH, arquivosH in os.walk(caminhoAbsoluto):
        for arquivoH in arquivosH:
            if(arquivoH[-4::]=='hash'):
                os.remove(arquivoH)
                                        
    print('Guarda e estrutura hash excluida.')
    
    


          
opcao = input('Digite a opção: (-i / -t / -x): ')

if(opcao == '-i'):
    hash()
elif(opcao == '-t'):
    verifica()                    
elif(opcao =='-x'):
    exclui()
else:
    print('Nenhuma opção valida.')     