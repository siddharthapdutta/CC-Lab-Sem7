%{
	#include<stdio.h>
%}

%%
"if"|"else"|"while"|"do"|"switch"|"case" { printf("Keyword"); }
[a-zA-Z][a-z|0-9]* { printf("Identifier"); }
[0-9]* { printf("Constant"); }
"!"|"@"|"*"|"&"|"^"|"%"|"$"|"#" { printf("Special Character"); }

%%
int yywrap()
{
	return 1;
}

int main()
{
	printf("Enter a string of data\n");
	yylex();
}




