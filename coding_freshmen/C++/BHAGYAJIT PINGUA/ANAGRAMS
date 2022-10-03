#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	char s[100],t[100];
	cout<<"s=";
	gets(s);
	cout<<"t=";
	gets(t);
    int j,l,m,x,c=0,i;
	l=strlen(s);
	m=strlen(t);
	if(l==m)
	{
		for(i=0;i<l;i++)
		{
			for(j=0;j<l;j++)
			{
				if(s[i]==t[j])
				{
					c++;
					t[j]='\0';
					s[i]='\t';
				}
			}
		}
		if(c==l)
			cout<<"true";
		else
			cout<<"false";
	}
	else
		cout<<"false";
	return(0);
}
