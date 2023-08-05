/*
 ============================================================================
 Name        : PraticaViginereRedesC.c
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
	char texto_str[60];
	int opcaoMusica;

	printf("\n Escolha uma musica (1-Silvio) (2-Tropa de Elite): ");
	scanf("%d", &opcaoMusica);

	if(opcaoMusica==1)
		arq_entrada = fopen("textoViginereRedesSilvio.txt", "r");
	else if(opcaoMusica==2)
		arq_entrada = fopen("textoViginereRedes.txt", "r");
	else
		printf("Selecione uma musica valida. \n");

	if (arq_entrada == NULL)
		printf("Problemas na abertura do arquivo \n");

	printf("Musica para descifrar: \n");

	while (!feof(arq_entrada)){
		char *result = fgets(texto_str, 60, arq_entrada);
			if (result)
				printf("%s",texto_str);
	 }

	fclose(arq_entrada);

	char chave[10];
	char mensagemCod[60];
//	segredo		Despacito
	printf("\n Escolha uma chave para decodificar o texto completo: ");
	scanf("%s", &chave);

	printf("\n Musica encriptada : \n");

	if(opcaoMusica==1)
		arq_entrada = fopen("textoViginereRedesSilvio.txt", "r");
	else if(opcaoMusica==2)
		arq_entrada = fopen("textoViginereRedes.txt", "r");

	int j=0;
	while (!feof(arq_entrada)){ //feof indica o fim do arquivo
		char *result = fgets(texto_str, 60, arq_entrada);

		if (result){
			for(int i=0; i<strlen(texto_str); i++){ //
				if(texto_str[i]>31 && texto_str[i]<127){ //vocabulario
					int auxI = texto_str[i] - chave[j];

					if(auxI!=0){
						if(auxI<0)
							auxI=(-1)*auxI;

						auxI=(95-auxI)+32; //Mod 95 + 32 q eh o inicio do vocabulario
					}else
						auxI=32;

					char auxC = auxI;

					mensagemCod[i]=auxC;
					j++;

					if(j==strlen(chave))
						j=0;
				}else{
					mensagemCod[i]=texto_str[i];
				}
			}

			mensagemCod[strlen(texto_str)-1]='\0';
			printf("%s \n", mensagemCod);
		}
	}

	return EXIT_SUCCESS;
}
