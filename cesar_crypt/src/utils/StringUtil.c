#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "StringUtil.h"

/*
   Can't return a char array, so there are some other ways 
   https://stackoverflow.com/questions/31060404/how-can-i-return-a-character-array-from-a-function-in-c
   In this one: Make the caller allocate the array and use it as a reference
*/
void manipulateStringEncrypted(char text[], int key, char *textModified){
    int lengthText = (int) strlen(text);
    // The modification of the character is based on whether it is lowercase or uppercase, 
    // i.e. if it is lowercase, after the 'z' comes the 'a'.
    for (int i = 0; i < lengthText; i++) {
        // Used to ensure that the character type remains the same (upper or lower case).
        int charModified = text[i] + key;

        // Uppercase 65 --- 90 / Lowercase 97 --- 122
        if (text[i] > 64 && text[i] < 91) {
            if (charModified > 90) {
                charModified = 65 + (charModified - 91);
            }
        } else if (text[i] > 96 && text[i] < 123) {
            if (charModified > 122) {
                charModified = 97 + (charModified - 123);
            }
        } else {
            charModified = text[i];
        }

        // Convert to char, to assemble the modified text
        textModified[i] = (char) charModified;
    }

    // Line break
    textModified[lengthText] = '\0';
}
