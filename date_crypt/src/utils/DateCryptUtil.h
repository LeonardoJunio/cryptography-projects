#include <stdio.h>
#include <stdbool.h> 

extern const char* FILE_INPUT;
extern const char* FILE_OUTPUT;

struct DateCryptStruct getDataDateCrypt();

FILE *getFileDateCrypt(int cryptOption);

bool validateDataDateCrypt(struct DateCryptStruct dataDateCrypt, FILE* file);

void getDateNumber(char date[], char* dateNumber);
