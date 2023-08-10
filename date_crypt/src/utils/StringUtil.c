#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "StringUtil.h"

/*
   Can't return a char array, so there are some other ways 
   https://stackoverflow.com/questions/31060404/how-can-i-return-a-character-array-from-a-function-in-c
   In this one: Make the caller allocate the array and use it as a reference
*/
void processText(int cryptOption, char *text, char *processedText, char *dateNumber){
	int indexDateNumber = 0;
	int lengthText = (int) strlen(text);
	int lengthDateNumber = (int) strlen(dateNumber);

	for (int i = 0; i < lengthText; i++) {
		int charModified;

		if (cryptOption == 1) {
			charModified = text[i] + (dateNumber[indexDateNumber] - 48);
		} else if (cryptOption == 2) {
			charModified = text[i] - (dateNumber[indexDateNumber] - 48);
		}

		processedText[i] = (char)charModified;

		indexDateNumber++;

		if (indexDateNumber == lengthDateNumber) {
			indexDateNumber = 0;
		}

		processedText[lengthText] = '\0';
	}
}
