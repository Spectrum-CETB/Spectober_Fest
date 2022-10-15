#include <stdio.h>
#include <string.h>

int main()
{
    char s[100], t[100];
    printf("Enter 1st string: ");
    gets(s);
    printf("Enter 2nd string: ");
    gets(t);
    int n = 0;
    int len_s = strlen(s);
    int len_t = strlen(t);
    for (int i = 0; i < len_s; i++)
    {
        for (int j = 0; j < len_t; j++)
        {
            if (s[i] == t[j])
            {
                n++;
            }
        }
    }

    if (n == len_s)
    {
        printf("True");
    }
    else
    {
        printf("False");
    }

    return 0;
}
