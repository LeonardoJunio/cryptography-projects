#include <stdio.h>
#include <stdbool.h> 

struct DateCryptStruct getDataDateCrypt();

FILE *getFileDateCrypt(int cryptOption);

bool validateDataDateCrypt(struct DateCryptStruct dataDateCrypt, FILE* file);

void getDateNumber(char date[], char* dateNumber);
