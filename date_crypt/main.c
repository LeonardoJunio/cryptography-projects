#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void converter(int optionCrypt, char *text, char *processedText, char *dateNumber) {
	int indexDateNumber = 0;

	for (int i = 0; i < strlen(text); i++) {
		int charModified;

		if (optionCrypt == 1) {
			charModified = text[i] + (dateNumber[indexDateNumber] - 48);
		} else if (optionCrypt == 2) {
			charModified = text[i] - (dateNumber[indexDateNumber] - 48);
		}

		processedText[i] = (char)charModified;

		indexDateNumber++;

		if (indexDateNumber == strlen(dateNumber)) {
			indexDateNumber = 0;
		}

		processedText[strlen(text)] = '\0';
	}

	printf("Processed text: %s \n", processedText);

	if (optionCrypt == 1) {
		FILE *outputFile = fopen("textoCSaidaredes.sec", "w");

		if (outputFile == NULL) {
			printf("Problems opening the file \n");
		} else {
			fprintf(outputFile, "%s", processedText);
			printf("Processed text saved \n");
		}

		fclose(outputFile);
	}
}

int main(void)
{
	FILE *inputFile;
	char text[100];
	int optionCrypt;

	printf("Do you want to encrypt (1) or decrypt (2)? \n");
	scanf("%d", &optionCrypt);

	// if(optionCrypt != 1 && optionCrypt != 2){
	// 	printf("Select a valid option \n");
	// 	return;
	// }

	if (optionCrypt == 1) {
		inputFile = fopen("textoCredes.txt", "r");
	} else if (optionCrypt == 2) {
		inputFile = fopen("textoCSaidaredes.sec", "r");
	} else {
		printf("Select a valid option \n");
		return EXIT_SUCCESS;
	}

	if (inputFile == NULL) {
		printf("Problems opening the file \n");
		return EXIT_SUCCESS;
	}

	// 'fgets' reads up to 100 characters or up to '\n'
	fgets(text, 100, inputFile);

	fclose(inputFile);

	char date[9];
	char dateNumber[7];
	char processedText[strlen(text)];

	printf("Enter a date to perform the operation in the following format (e.g. '01/01/18'): ");
	scanf("%s", &date);

	for (int i = 0, j = 0; i < strlen(date); i++) {
		if (date[i] != '/') {
			dateNumber[j] = date[i];
			j++;
		}
	}

	converter(optionCrypt, text, processedText, dateNumber);

	return EXIT_SUCCESS;
}
