%{
#include <stdio.h>
#include <stdlib.h>
#include "parser.tab.h"
%}

%%

hora_de_brilhar        { return HORA_DE_BRILHAR; }
a_mimir                { return A_MIMIR; }
sempre_diva            { return SEMPRE_DIVA; }
grunido                { return GRUNIDO; }
ENQUANTO_ELA_NAO_MUDA_DE_IDEIA  { return ENQUANTO_ELA_NAO_MUDA_DE_IDEIA; }
SE                     { return SE; }
"<<"                   { return TAREFA_DECLARATION; }
">>"                   { return ACAO_DECLARATION; }
":"                    { return ":"; }
"("                    { return "("; }
")"                    { return ")"; }
","                    { return ","; }
"\n"                   { return "\n'; }
[a-zA-Z_]+             { yylval.string = strdup(yytext); return STRING; }
[0-9]+                 { yylval.integer = atoi(yytext); return NUMBER; }
[ \t]+                 ; /* ignore whitespace */
"."                    ; /* ignore period */
.                      { printf("Unexpected character: %s\n", yytext); }

%%