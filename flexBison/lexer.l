%{
#include "parser.tab.h"
%}

%%

"hora_de_brilhar"        { printf("achei hora_de_brilhar\n");  return HORA_DE_BRILHAR; }
"sempre_diva"            { printf("achei sempre_diva\n"); return SEMPRE_DIVA; }
"grunido"                { printf("achei grunido\n"); return GRUNIDO; }
"a_mimir"                { printf("achei a_mimir\n"); return A_MIMIR; }
"ENQUANTO_ELA_NAO_MUDA_DE_IDEIA"  { printf("achei ENQUANTO_ELA_NAO_MUDA_DE_IDEIA\n"); return ENQUANTO_ELA_NAO_MUDA_DE_IDEIA; }
"SE"                     { printf("achei SE\n"); return SE; }
"."                      { printf("achei .\n"); return DOT; }
"<<"                     { printf("achei <<\n"); return TAREFA_DECLARATION; }
">>"                     { printf("achei >>\n"); return ACAO_DECLARATION; }
"tarefa"                 { printf("task\n"); return TAREFA; }
"hablar"                 { printf("achei hablar\n"); return HABLAR; }
"acao"                   { printf("achei acao\n"); return ACAO; }
"("                      { printf("open paren\n"); return '('; }
")"                      { printf("close paren\n"); return ')'; }
","                      { printf("achei ,\n"); return ','; }
"\n"                     { printf("n\n"); return '\n'; }
"{"                      { printf("open {\n"); return BLOCK_BEGIN; }
"}"                      { printf("close }\n"); return BLOCK_END; }
[a-zA-Z_]+               { yylval.string = strdup(yytext); printf("achei string: %s\n", yylval.string); return STRING; }
[0-9]+                   { yylval.integer = atoi(yytext); printf("achei number: %d\n", yylval.integer); return NUMBER; }
[ \t]+                   ; /* ignore whitespace */
.                        { printf("Unexpected character: %s\n", yytext); }

%%
