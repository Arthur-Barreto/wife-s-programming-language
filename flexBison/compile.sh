#!/bin/bash

# Parar a execução se algum comando falhar
set -e

# Gerar o parser com Bison
bison -d parser.y

# Gerar o lexer com Flex
flex lexer.l

# Compilar os arquivos gerados com GCC
gcc -o run parser.tab.c lex.yy.c -lfl
