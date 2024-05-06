%{
#include "parser.tab.h"
%}

%%

hora_de_brilhar        { printf("achei hora_de_brilhar\n");  return HORA_DE_BRILHAR; }
sempre_diva            { printf("achei sempre_diva\n"); return SEMPRE_DIVA; }
grunido                { printf("achei grunido\n"); return GRUNIDO; }
a_mimir                { printf("achei a_mimir\n"); return A_MIMIR; }
ENQUANTO_ELA_NAO_MUDA_DE_IDEIA  { return ENQUANTO_ELA_NAO_MUDA_DE_IDEIA; }
SE                     { return SE; }
"<<"                   { return TAREFA_DECLARATION; }
">>"                   { return ACAO_DECLARATION; }
":"                    { return ':'; }
"("                    { return '('; }
")"                    { return ')'; }
","                    { return ','; }
"\n"                   { return '\n'; }
[a-zA-Z_]+             { yylval.string = strdup(yytext); return STRING; }
[0-9]+                 { yylval.integer = atoi(yytext); return NUMBER; }
[ \t]+                 ; /* ignore whitespace */
"."                    ; /* ignore period */
.                      { printf("Unexpected character: %s\n", yytext); }

%%