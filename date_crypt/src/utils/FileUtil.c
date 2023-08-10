#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "FileUtil.h"

#define FILE_OUTPUT "files/textoCSaidaredes.sec"
#define LENGTH_TEXT 100

void getTextFile(char* text, FILE* file){
    // 'fgets' reads up to 100 characters or up to '\n'
	fgets(text, LENGTH_TEXT, file);

	fclose(file);
}

void writeTextFile(char processedText[]){
    FILE *outputFile = fopen(FILE_OUTPUT, "w");

    if (outputFile == NULL) {
        printf("Problems opening the file \n");
        fclose(outputFile);
        
        return;
    }

    fprintf(outputFile, "%s", processedText);
    printf("Processed text saved \n");    

    fclose(outputFile);
}
