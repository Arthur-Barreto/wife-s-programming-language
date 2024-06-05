%{
#include "parser.tab.h"
%}

%%

"HORA_DE_BRILHAR"        { return HORA_DE_BRILHAR; }
"SEMPRE_DIVA"            { return SEMPRE_DIVA; }
"GRUNIDO"                { return GRUNIDO; }
"A_MIMIR"                { return A_MIMIR; }
"ENQUANTO_ELA_NAO_MUDA_DE_IDEIA"  { return ENQUANTO_ELA_NAO_MUDA_DE_IDEIA; }
"SE"                     { return SE; }
"."                      { return DOT; }
"<<"                     { return TAREFA_DECLARATION; }
">>"                     { return ACAO_DECLARATION; }
"TAREFA"                 { return TAREFA; }
"HABLAR"                 { return HABLAR; }
"ACAO"                   { return ACAO; }
"("                      { return '('; }
")"                      { return ')'; }
","                      { return ','; }
"\n"                     { return '\n'; }
"TO_COM_FOME"            { return BLOCK_BEGIN; }
"QUERO_PITDAS"           { return BLOCK_END; }
[a-zA-Z_]+               { yylval.string = strdup(yytext); return STRING; }
[0-9]+                   { yylval.integer = atoi(yytext); return NUMBER; }
[ \t]+                   ; /* ignore whitespace */
.                        { printf("Unexpected character: %s\n", yytext); }

%%
