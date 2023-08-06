#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "StringUtil.h"

/*
   Can't return a char array, so there are some other ways 
   https://stackoverflow.com/questions/31060404/how-can-i-return-a-character-array-from-a-function-in-c
   In this one: Make the caller allocate the array and use it as a reference
*/
void manipulateStringEncrypted(char text[], char key[], int *indexKey, char *textModified){
    int lengthText = (int) strlen(text);
    int indexKeyAux = *indexKey;

    for (int i = 0; i < lengthText; i++) {
        if (text[i] > 31 && text[i] < 127) { // vocabulary


            int charModified = text[i] - key[indexKeyAux];

            if (charModified != 0) {
                if (charModified < 0) {
                    charModified = (-1) * charModified;
                }

                // Mod 95 + 32 is the beginning of the vocabulary
                charModified = (95 - charModified) + 32;
            } else {
                charModified = 32;
            }

            // Convert to char, to assemble the modified text
            textModified[i] = (char) charModified;

            indexKeyAux++;

            if (indexKeyAux == (int) strlen(key)) {
                indexKeyAux = 0;
            }
        } else {
            textModified[i] = text[i];
        }
    }

    *indexKey = indexKeyAux;
    // Line break
    textModified[lengthText - 1] = '\0';
}
