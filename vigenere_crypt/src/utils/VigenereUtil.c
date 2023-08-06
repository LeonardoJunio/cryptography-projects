#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "VigenereUtil.h"
#include "../domain/structs/VigenereStruct.h"

#define TEXT_SONG_SILVIO "files/textoViginereRedesSilvio.txt"
#define TEXT_SONG_TROPA "files/textoViginereRedes.txt"
#define ID_SONG_SILVIO 1
#define ID_SONG_TROPA 2

struct VigenereStruct getDataVigenere(){
	struct VigenereStruct dataVigenere;

    printf("Choose a song (1-Silvio) (2-Tropa de Elite): ");
	scanf("%d", &dataVigenere.songOption);

	// Despacito segredo
	printf("Choose a key to decrypt the full text: ");
	scanf("%s", dataVigenere.key);

    return dataVigenere;
}

FILE *getFileVigenere(int songOption){
    FILE *songFile;

    if (songOption == 1) {
		songFile = fopen(TEXT_SONG_SILVIO, "r");
	} else if (songOption == 2) {
		songFile = fopen(TEXT_SONG_TROPA, "r");
	}

    return songFile;
}

bool validateDataVigenere(struct VigenereStruct dataVigenere, FILE* songFile){    
    if(dataVigenere.songOption != ID_SONG_SILVIO && dataVigenere.songOption != ID_SONG_TROPA){
		printf("Song option invalid. \n");
        return false;
    }
    
    if(strlen(dataVigenere.key) < LENGTH_MIN_KEY || strlen(dataVigenere.key) > LENGTH_MAX_KEY){
		printf("Key option invalid. \n");
        return false;
    }
    
    if (songFile == NULL) {
		printf("Problems opening the file. \n");
        return false;
	}

    return true;
}
