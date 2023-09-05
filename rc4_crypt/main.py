import numpy as np

# Returns an integer representing the Unicode character (string to decimal)
def converterStrDec(texto) -> list:
    aux = []
    for c in texto:
        aux.append(ord(c))
    return aux

# Converts an integer to its Unicode character (decimal to string)
def converterDecStr(texto) -> str: 
    aux = ''
    for c in texto:
        aux += chr(c)
    return aux

def converterHexDec(texto): #hex para decimal
    aux = []
    for i in range(0, len(texto), 2):
        byte = texto[i:i+2]
        aux.append(int('0x' + byte, 16))
    return aux

# Converts an integer to the corresponding hexadecimal number (decimal to hex)
def converterDecHex(text) -> str:
    result = ''
    
    # Works with 0x0 to 0x99
    for item in text:
        # Takes the characters after '0x'
        sufixHex = hex(item)[2:] 
        
        # Add '0' when only 1 number (0x9 ->0x09)  
        # Ternary: a if condition else b
        result += ('0' + sufixHex) if (len(sufixHex) == 1) else sufixHex
            
    return result

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
    arquivoSaida.write(mensagemDescriptografada)
    arquivoSaida.close()
else:
    print('Opção invalida.')









