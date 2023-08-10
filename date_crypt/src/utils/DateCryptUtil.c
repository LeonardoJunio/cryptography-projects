#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "DateCryptUtil.h"
#include "../domain/structs/DateCryptStruct.h"

#define FILE_INPUT "files/textoCredes.txt"
#define FILE_OUTPUT "files/textoCSaidaredes.sec"
#define OPTION_ENCRYPT 1
#define OPTION_DECRYPT 2

struct DateCryptStruct getDataDateCrypt(){
	struct DateCryptStruct dataDateCrypt;

    printf("Do you want to encrypt (1) or decrypt (2)? ");
	scanf("%d", &dataDateCrypt.cryptOption);

	printf("Enter a date to perform the operation in the following format (e.g. '01/01/18'): ");
	scanf("%s", dataDateCrypt.date);

    getDateNumber(dataDateCrypt.date, dataDateCrypt.dateNumber);

    return dataDateCrypt;
}

FILE *getFileDateCrypt(int cryptOption){
    FILE *file;

    if (cryptOption == 1) {
		file = fopen(FILE_INPUT, "r");
	} else if (cryptOption == 2) {
		file = fopen(FILE_OUTPUT, "r");
	}

    return file;
}

bool validateDataDateCrypt(struct DateCryptStruct dataDateCrypt, FILE* file){    
    if(dataDateCrypt.cryptOption != OPTION_ENCRYPT && dataDateCrypt.cryptOption != OPTION_DECRYPT){
		printf("Crypt option invalid. \n");
        return false;
    }
    
    if(strlen(dataDateCrypt.date) < LENGTH_MIN_DATE || strlen(dataDateCrypt.date) > LENGTH_MAX_DATE){
		printf("Date invalid. \n");
        return false;
    }
    
    if(strlen(dataDateCrypt.dateNumber) < LENGTH_MIN_DATE_NUMBER || strlen(dataDateCrypt.dateNumber) > LENGTH_MAX_DATE_NUMBER){
		printf("Date invalid. \n");
        return false;
    }
    
    if (file == NULL) {
		printf("Problems opening the file. \n");
        return false;
	}

    return true;
}

void getDateNumber(char date[], char* dateNumber){
    for (int i = 0, j = 0; i < (int) strlen(date); i++) {
		if (date[i] != '/') {
			dateNumber[j] = date[i];
			j++;
		}
	}
}
