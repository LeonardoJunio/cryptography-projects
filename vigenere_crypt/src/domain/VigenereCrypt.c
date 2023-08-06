#include <stdio.h>

#include "VigenereCrypt.h"
#include "structs/VigenereStruct.h"
#include "../utils/StringUtil.h"
#include "../utils/VigenereUtil.h"

#define LENGTH_TEXT_SONG 100

void initVigenereCrypt(){
	struct VigenereStruct dataVigenere = getDataVigenere();	
    FILE *songFile = getFileVigenere(dataVigenere.songOption);
	
	if(!validateDataVigenere(dataVigenere, songFile)){
		return;
	}

	char textModified[LENGTH_TEXT_SONG];
	char textSongPart[LENGTH_TEXT_SONG];
	int indexKey = 0;
	
	printf("Decrypted music: \n");

	while (!feof(songFile)) { 
		//'feof' indicates end of file
		char *result = fgets(textSongPart, LENGTH_TEXT_SONG, songFile);

		if (!result) {
			continue;
		}

		manipulateStringEncrypted(textSongPart, dataVigenere.key, &indexKey, textModified);

		printf("%s \n", textModified);
	}

	fclose(songFile);
}
