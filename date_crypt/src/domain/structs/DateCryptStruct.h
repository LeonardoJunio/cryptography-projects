#define LENGTH_MAX_DATE 9
#define LENGTH_MIN_DATE 1

#define LENGTH_MAX_DATE_NUMBER 7
#define LENGTH_MIN_DATE_NUMBER 1

struct DateCryptStruct
{
    int cryptOption;
    char date[LENGTH_MAX_DATE];
    char dateNumber[LENGTH_MAX_DATE_NUMBER];
};
