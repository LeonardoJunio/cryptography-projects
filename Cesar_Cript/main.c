/*
 ============================================================================
 Name        : PraticaCesarRedesC.c
 Author      : Leonardo
 Version     :
 Copyright   : Your copyright notice
 Description : in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	FILE *arq_entrada;
	char texto_str[100];

	arq_entrada = fopen("textoCesarRedes.txt", "r");//'a' cria caso nao tenha

	if (arq_entrada == NULL){
		printf("Problemas na abertura do arquivo \n");
	}

	fgets(texto_str, 100, arq_entrada);

	fclose(arq_entrada);

	char mensagem[strlen(texto_str)];
	char mensagemCod[strlen(texto_str)];
	char mensagemEncriptada[strlen(texto_str)];

	int chave;

	strcpy(mensagem, texto_str);

	printf("Mensagem base: %s \n", mensagem);

	for(chave=0; chave<26; chave++){
		for(int j=0; j<strlen(mensagem); j++){
			int auxI = mensagem[j] + chave;
			//M 65 --- 90  / m 97 --- 122
			if(mensagem[j]>64 && mensagem[j]<91){ //Maiuscula
				if(auxI>90)
					auxI=65 + (auxI-91);
			}else if(mensagem[j]>96 && mensagem[j]<123){ //Minuscula
				if(auxI>122)
					auxI=97 + (auxI-123);
			}else
				auxI = mensagem[j];

			char auxC = auxI;
			mensagemCod[j]=auxC;
		}
		mensagemCod[strlen(mensagem)]='\0';


		printf("Mensagem decodificada %d: %s \n", chave, mensagemCod);
	}


	printf("\n Escolha uma chave para decodificar o texto completo: ");
	scanf("%d", &chave);

	printf("Mensagem encriptada : \n");

	arq_entrada = fopen("textoCesarRedes.txt", "r");

	while (!feof(arq_entrada)){ //feof indica o fim do arquivo
		char *result = fgets(texto_str, 50, arq_entrada);  // o 'fgets' lê até 50 caracteres ou até o '\n'

		if (result){
			for(int j=0; j<strlen(texto_str); j++){
				int auxI = texto_str[j] + chave;

				if(texto_str[j]>64 && texto_str[j]<91){ //Maiuscula
					if(auxI>90)
						auxI=65 + (auxI-91);
				}else if(texto_str[j]>96 && texto_str[j]<123){ //Minuscula
					if(auxI>122)
						auxI=97 + (auxI-123);
				}else
					auxI = texto_str[j];

				char auxC = auxI;
				mensagemEncriptada[j]=auxC;
			}

			mensagemEncriptada[strlen(texto_str)]='\0';
			printf("%s", mensagemEncriptada);
		}
	}

	fclose(arq_entrada);

	return EXIT_SUCCESS;
}
