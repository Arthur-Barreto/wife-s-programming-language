%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

void yyerror(const char *s);
extern int yylex();
%}

%union {
    char *string;
    int integer;
}

%token <string> STRING
%token <integer> NUMBER
%token HORA_DE_BRILHAR A_MIMIR SEMPRE_DIVA GRUNIDO ENQUANTO_ELA_NAO_MUDA_DE_IDEIA SE
%token TAREFA_DECLARATION ACAO_DECLARATION TAREFA ACAO DOT COLON HABLAR

%%

program: block
       ;

block: HORA_DE_BRILHAR '\n' days SEMPRE_DIVA
      ;

days: days day
    | day
    ;

day: GRUNIDO '\n' statements A_MIMIR '\n'
    ;

statements: statements statement
    | statement
    ;

statement:
         TASK_DECLARATION
         | ACTION_DECLARATION
         | WHILE_STATEMENT
         | IF_STATEMENT
         | HABLAR_STATEMENT
         ;

TASK_DECLARATION: TAREFA TAREFA_DECLARATION '(' STRING ',' NUMBER ')' '\n'
                {
                    printf("TAREFA\n");
                }
                ;

ACTION_DECLARATION: ACAO ACAO_DECLARATION '(' STRING ',' NUMBER ')' '\n'
                {
                    printf("ACAO\n");
                }
                ;

WHILE_STATEMENT: ENQUANTO_ELA_NAO_MUDA_DE_IDEIA CONDICIONAL COLON '\n' statement '\n'
                {
                    printf("ENQUANTO\n");
                }
                ;

IF_STATEMENT: SE CONDICIONAL COLON '\n' statement
                {
                    printf("SE\n");
                }
                ;

HABLAR_STATEMENT: HABLAR '(' STRING ',' NUMBER ')' '\n'
                {
                    printf("HABLAR\n");
                }
                ;

CONDICIONAL: TAREFA DOT STRING
                {
                    printf("tarefa . dot");
                }
                ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    if (yyparse() == 0) {
        printf("Programa aceito\n");
    } else {
        printf("Programa rejeitado\n");
    }
    return 0;
}
