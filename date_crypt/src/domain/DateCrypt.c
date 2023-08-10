#include <stdio.h>

#define LENGTH_TEXT 100

#include "DateCrypt.h"
#include "structs/DateCryptStruct.h"
#include "../utils/StringUtil.h"
#include "../utils/DateCryptUtil.h"
#include "../utils/FileUtil.h"

void initDateCrypt(){
	struct DateCryptStruct dataDateCrypt = getDataDateCrypt();
    FILE *file = getFileDateCrypt(dataDateCrypt.cryptOption);
	
	if(!validateDataDateCrypt(dataDateCrypt, file)){
		return;
	}

	char text[LENGTH_TEXT];
	char processedText[LENGTH_TEXT];

	getTextFile(text, file);

	processText(dataDateCrypt.cryptOption, text, processedText, dataDateCrypt.dateNumber);

	printf("Processed text: %s \n", processedText);

	if (dataDateCrypt.cryptOption == 1) {
		writeTextFile(processedText);
	}    
}
