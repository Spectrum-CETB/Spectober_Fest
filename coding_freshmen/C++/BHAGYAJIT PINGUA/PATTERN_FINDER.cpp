#include<string.h>
#include<iostream>
#include<stdio.h>
using namespace std;
void search(char pat[],char text[]);
int main()
{
	char a[10000],b[10000];
	gets(a);
	gets(b);
	search(b,a);
	return 0;
}
void search(char pat[],char txt[])
{
	int c,m,n,i,j;
	m=strlen(pat);
	n=strlen(txt);
	for(i=0;i<n;i++)
	{
		if(i==(n-m+1))
			break;
		else
		{
			c=0;
			for(j=0;j<m;j++)
			{
				if(pat[j]==txt[i+j])
				{
					c++;
				}
			}
			if(c==m)
				cout<<"Patten found at index "<<i<<endl;
		}
	}
}
