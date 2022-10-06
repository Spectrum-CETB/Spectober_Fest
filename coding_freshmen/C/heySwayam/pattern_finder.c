#include <stdio.h>
#include <string.h>
void search(char pat[100], char txt[100])
{
    int pat_len = strlen(pat);
    int txt_len = strlen(txt);
    int sum, n = 0;
    for (int i = 0; i < txt_len; i++)
    {
        if (txt[i] == pat[0])
        {
            sum = 0;
            for (int j = 0; j < (pat_len - 1); j++)
            {
                if (txt[i + j + 1] == pat[j + 1])
                {
                    sum++;
                }
            }

            if (sum == 2)
            {
                n++;
                printf("Pattern found at index %d\n",i);
            }
        }
    }
}
int main()
{
    char pat[100];
    char txt[100];
    printf("Enter the pattern\n");
    gets(pat);
    printf("Enter the text\n");
    gets(txt);
    search(pat, txt);
    return 0;
}