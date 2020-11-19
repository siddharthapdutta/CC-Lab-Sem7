%{ 
/* Definition section */
#include<stdio.h> 
#include <stdlib.h> 
void yyerror(const char *str)  
{ 
 printf("\nSequence Rejected\n");         
} 
  
%} 
  
%token ZERO ONE 
  
/* Rule Section */
%% 
  
r : s {printf("\nSequence Accepted\n\n");} 
; 
  
s : n 
| ZERO a 
| ONE b 
; 
  
a : n a 
| ZERO 
; 
  
b : n b 
| ONE 
; 
  
n : ZERO 
| ONE 
; 
  
%% 
  
#include"lex.yy.c" 
//driver code 
int main()  
{ 
  printf("\nEnter Sequence of Zeros and Ones : "); 
  yyparse(); 
  printf("\n"); 
  return 0; 
} 