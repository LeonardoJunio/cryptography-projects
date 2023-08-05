#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../helper/CesarDecryptHelper.h"
#include "../utils/StringUtil.h"

#define KEY_MIN 0
#define KEY_MAX 26
#define LENGTH_TEXT 100

/*
    Access to static functions is restricted to the file except where they are declared.
    When we want to restrict access to functions from outer world, we have to make them static
    Declaring a function as static, requires the function to be defined in all .c file(s) in which it is included
    In other words, should only have the static declarations inside the .c file and not in the header file
*/
static void showOptionsKey(char pathFile[]);
static int defineKeyDecrypt();
static void showMessageDecrypted(int key, char pathFile[]);

void initCesarDecrypt(char pathFile[]){
	showOptionsKey(pathFile);
	int key = defineKeyDecrypt();
	showMessageDecrypted(key, pathFile);
}

static void showOptionsKey(char pathFile[]){
    FILE *inputFile;
	char text[LENGTH_TEXT];

	// Use 'a' to create if it doesn't exist
	// The path starts where the Makefile is located
	inputFile = fopen(pathFile, "r");

	if (inputFile == NULL) {
		printf("Problems opening the file \n");
		return;
	}

	// 'fgets' reads up to 100 characters or the n '\n'
	fgets(text, LENGTH_TEXT, inputFile);

	fclose(inputFile);

	char message[strlen(text)];
	char messageCod[strlen(text)];

	strcpy(message, text);

	printf("Base message: %s \n", message);

	for (int key = KEY_MIN; key < KEY_MAX; key++) {
		manipulateStringEncrypted(message, key, messageCod);

		printf("Decoded message %d: %s \n", key, messageCod);
	}
}

static int defineKeyDecrypt(){
	int key;
	
	do{
		printf("\n Choose a key to decrypt the full text (between 0 and 26): ");
		scanf("%d", &key);
	} while (key < KEY_MIN || key > KEY_MAX);

	return key;
}

static void showMessageDecrypted(int key, char pathFile[]){
    FILE *inputFile;
	char text[LENGTH_TEXT];

	printf("Encrypted message: \n");

	inputFile = fopen(pathFile, "r");

	if (inputFile == NULL) {
		printf("Problems opening the file \n");
		return;
	}

	//'feof' indicates end of file
	while (!feof(inputFile)) {
		char *result = fgets(text, LENGTH_TEXT, inputFile);
		char messageEncrypted[strlen(text)];

		if (result) {
			manipulateStringEncrypted(text, key, messageEncrypted);

			printf("%s", messageEncrypted);
		}
	}

	fclose(inputFile);
}

