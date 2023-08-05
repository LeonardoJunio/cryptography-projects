#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 
	#include <file> This form is used for system header files. 
	It searches for a file named 'file' in a standard list of system directories
 
	#include "file" This form is used for header files of your own program. 
	It searches for a file named 'file' in the directory containing the current file
*/

#include "CesarCrypt.h"

int main(void)
{
	char pathFile[] = "files/textoCesarRedes.txt";

	initCesarCrypt(pathFile);		

	return EXIT_SUCCESS;
}
