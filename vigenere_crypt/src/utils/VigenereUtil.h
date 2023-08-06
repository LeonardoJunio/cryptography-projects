#include <stdio.h>
#include <stdbool.h> 

/*
    Include file "../domain/structs/VigenereStruct.h" with 'include' had an error,
    because it was already being imported by VigenereCrypt.c, which calls this file    
*/

struct VigenereStruct getDataVigenere();

FILE *getFileVigenere(int songOption);

bool validateDataVigenere(struct VigenereStruct dataVigenere, FILE* songFile);
