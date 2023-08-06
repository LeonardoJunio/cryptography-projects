import numpy as np

def converterStrDec(texto): #string para decimal
    aux = []
    for c in texto:
        aux.append(ord(c))
    return aux

def converterDecStr(texto): #decimal para string
    aux = ''
    for c in texto:
        aux += chr(c)
    return aux

def converterHexDec(texto): #hex para decimal
    aux = []
    for i in range(0, len(texto), 2):
        byte = texto[i:i+2]
        aux.append(int('0X' + byte, 16))
    return aux

def converterDecHex(texto): #decimal para hex
    aux = ''
    for d in texto:
        if(len(hex(d)[2:])==1):
            aux += '0' + hex(d)[2:] #conversao pra decimal de 2 em 2, adiciona 0 quando for só 1 valor (0x9 ->0x09)  
        else:
            aux += hex(d)[2:]
            
    return aux

def Encriptar(chave, mensagem):
    tamC = len(chave)
    
    chave = converterStrDec(chave)
    mensagem = converterStrDec(mensagem)
    
    S = list(range(256))

    j=0
    for i in range(256):
        j = (j + S[i] + chave[i%tamC])%256
        S[i], S[j] = S[j], S[i]
    
    i=j=0
    keystream=[]
    
    for c in mensagem:
        i=(i+1)%256
        j=(j+S[i])%256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j])%256]
        keystream.append(K)
    
    keystream = np.array(keystream)
    
    cipher = keystream ^ mensagem #xor
    cipher = converterDecHex(cipher)
    return cipher
    

def Desencriptar(chave, mensagem):
    tamC = len(chave)
    mensagem = converterHexDec(mensagem)
    
    S = list(range(256))

    j=0
    for i in range(256):
        j = (j + S[i] + ord(chave[i%tamC]))%256
        S[i], S[j] = S[j], S[i]
    
    i=j=0
    mensagemSaida = []

    for c in mensagem:
        i=(i+1)%256
        j=(j+S[i])%256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j])%256]
        mensagemSaida.append(c^K)
    
    mensagemSaida = converterDecStr(mensagemSaida)
    return mensagemSaida
    
opcao = int(input('Deseja encriptar(1) ou desencriptar(2): '))

if opcao==1:
    arquivoMensagem = open('mensagem.txt', 'r')
    mensagem = arquivoMensagem.read()
    arquivoMensagem.close()
    
    arquivoChave = open('chave.txt', 'r')
    chave = arquivoChave.read()
    arquivoChave.close()

    print('Chave: ', chave)
    print('Mensagem: ', mensagem)

    mensagemCriptografada = Encriptar(chave, mensagem)
    print('Mensagem criptografada: ', mensagemCriptografada)
    
    arquivoSaidaCrip = open('mensagemCriptografada.txt', 'w')
    arquivoSaidaCrip.write(mensagemCriptografada)
    arquivoSaidaCrip.close()
    
elif opcao==2:
    arquivoMensagemCrip = open('mensagemCriptografada.txt', 'r')
    mensagemCriptografada = arquivoMensagemCrip.read()
    arquivoMensagemCrip.close()
    
    arquivoChave = open('chave.txt', 'r')
    chave = arquivoChave.read()
    arquivoChave.close()

    print('Chave: ', chave)
    print('Mensagem Criptografada: ', mensagemCriptografada)

    mensagemDescriptografada = Desencriptar(chave, mensagemCriptografada)
    print('Mensagem descriptografada: ', mensagemDescriptografada)
    
    arquivoSaida = open('mensagemDescriptografada.txt', 'w')
    arquivoSaida.write(mensagemCriptografada)
    arquivoSaida.close()
else:
    print('Opção invalida.')









