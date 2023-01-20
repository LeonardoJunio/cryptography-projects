/*
 ============================================================================
 Name        : Taf1RedesC.c
 Author      : Leonardo
 Version     :
 Copyright   : Your copyright notice
 Description : in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void converter(int parametro, char *mensagem, char *mensagemCod, char *dataN){

	for(int i=0, j=0; i<strlen(mensagem); i++){
		if(mensagem[i]!=32){
			int auxI;

			if(parametro==1)
				auxI = mensagem[i] + (dataN[j] - 48);
			else if (parametro==2)
				auxI = mensagem[i] - (dataN[j] - 48);

			char auxC = auxI;

			mensagemCod[i]=auxC;
			j++;

			if(i==strlen(dataN))
				j=0;
		}else{
			mensagemCod[i]=32;
		}
		mensagemCod[strlen(mensagem)]='\0';
	}

	printf("Mensagem Codificada: %s \n", mensagemCod);

	if(parametro==1){
		FILE *arq_saida;
		arq_saida = fopen("textoCSaidaredes.sec", "w");

		if (arq_saida == NULL){
			printf("Problemas na abertura do arquivo \n");
		}else{
			fprintf(arq_saida, "%s", mensagemCod);
			printf("Mensagem codificada salva. \n");
		}

		fclose(arq_saida);
	}
}

int main(void) {
	FILE *arq_entrada;
	char texto_str[100];
	int parametro;

	printf("\n Deseja cifrar (1) ou descifrar (2): ");
	scanf("%d", &parametro);

	if(parametro==1)
		arq_entrada = fopen("textoCredes.txt", "r");
	else if(parametro==2)
		arq_entrada = fopen("textoCSaidaredes.sec", "r");
	else
		printf("\n Selecione uma opção valida ");

	if (arq_entrada == NULL){
		printf("Problemas na abertura do arquivo \n");
	}

	fgets(texto_str, 100, arq_entrada);  // o 'fgets' lê até 99 caracteres ou até o '\n'

	fclose(arq_entrada);

	char data[9];
	char dataN[7];
	char mensagemCod[strlen(texto_str)];

	printf("\n Informe uma data para realizar a operação no seguinte formato, ex '01/01/18': ");
	scanf("%s", &data);

	for (int i=0, j=0; i<strlen(data); i++){
		if(data[i]!='/'){
			dataN[j] = data[i];
			j++;
		}
	}

	printf("Mensagem: %s \n", texto_str);

	converter(parametro, texto_str, mensagemCod, dataN);

	return EXIT_SUCCESS;
}
