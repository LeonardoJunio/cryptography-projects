from PIL import Image
import numpy as np
import cv2

def mensagemBinario(mensagem):
    binario = ''
    for i in mensagem:
        binario += bin(ord(i))[2::].zfill(8)
    binario+='00000000' #sera usada como condicao de parada
    return binario

def binarioMensagem(binario):
    caractere = ''
    string = ''
    k = 1
    
    for j in binario:
        caractere += j
        if (k == 8):
            string += chr(int(caractere, 2))
            k=1
            caractere = ''
        else:
            k += 1
    return string

def inserirMensagem(texto, image):
    textoBinario = mensagemBinario(texto)
    indiceMensagem = 0

    for h in image:
        for w in h:
            r = bin(w[0])[2::].zfill(8)
            g = bin(w[1])[2::].zfill(8)
            b = bin(w[2])[2::].zfill(8)
            
            if(indiceMensagem<len(textoBinario)):
                w[0] = int(r[0:7] + textoBinario[indiceMensagem], 2)
                indiceMensagem+=1

            if(indiceMensagem<len(textoBinario)):
                w[1] = int(g[0:7] + textoBinario[indiceMensagem], 2)
                indiceMensagem+=1      
                
            if(indiceMensagem<len(textoBinario)):
                w[2] = int(b[0:7] + textoBinario[indiceMensagem], 2)
                indiceMensagem+=1 
          
    cv2.imwrite('imdM.bmp', image)
    
    print('Mensagem criptografada feita.')

def retirarMensagem(image):
    mensagemBinaria = ''
    count = 0
    terminou = False #indica se a mensagem terminou de ser criptografada
    
    for h in image:
        for w in h:
            for componentRGB in w:
                mensagemBinaria += bin(componentRGB)[2::].zfill(8)[7]
                if(mensagemBinaria[-8::] == '00000000'):
                    terminou=True
                    break
                if(count==8):
                    count=0
                    break
                count+=1
            if(terminou):
                break
        if(terminou):
            break
                    
                   
    mensagemRetirada = binarioMensagem(mensagemBinaria)
    
    arquivoMensagemSaida = open('mensagemSaida.txt', 'w')
    arquivoMensagemSaida.write(mensagemRetirada)
    arquivoMensagemSaida.close()
    
    print("Mensagem desencriptada: ", mensagemRetirada)


opcao = int(input('Deseja encriptar(1) ou desencriptar(2): '))

if (opcao==1) :
    arquivoMensagem = open('mensagem.txt', 'r')
    mensagem = arquivoMensagem.read()
    #imagem "imd.bmp" anexada no sigaa
    #por ser maior que 10mb (limite do sigaa para envio), não poderá ser anexada na tarefa
    arquivoImagem = cv2.imread('imd.bmp')
        
    inserirMensagem(mensagem, arquivoImagem)
    
    arquivoMensagem.close()
elif (opcao==2):
    arquivoImagemCrip = cv2.imread("imdM.bmp")
    retirarMensagem(arquivoImagemCrip)
else:
    print('Opcao invalida.')
