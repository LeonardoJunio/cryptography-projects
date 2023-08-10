#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "DateCrypt.h"

const char* FILE_INPUT = "files/textoCredes.txt";
const char* FILE_OUTPUT = "files/textoCSaidaredes.sec";

int main(void)
{
	initDateCrypt();

	return EXIT_SUCCESS;
}
