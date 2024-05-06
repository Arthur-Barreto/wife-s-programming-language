# Flex e Bison

## Flex

Funciona como o tokenizer, irá reconhecer tokens e passar para o Bison.

Me ajudou muito os seguintes materiais:

- [Flex e Bison](https://youtu.be/LpVufkH4gog?list=PLImMVrOC3KFn0US0AiW0JYLaU8mCtrqG0)
- [Flex e Bison](https://splimter.medium.com/quick-start-with-flex-bison-19ab53f36d75)

## Bison

Funciona como o parser, irá reconhecer a gramática e gerar a árvore sintática.

Me ajudou muito o seguinte material:

- [Flex e Bison](https://youtu.be/fFRxWtRibC8?list=PLImMVrOC3KFn0US0AiW0JYLaU8mCtrqG0)

## Pipeline

1.Rode o Bison

```bash
bison -d parser.y
```

2.Rode o Flex

```bash
flex lexer.l
```

3.Compile

```bash
gcc -o run parser.tab.c lex.yy.c -lfl
```

Ou, use o compile.sh

```bash
./compile.sh
```

Antes de rodar, de permissão de execução

```bash
chmod +x compile.sh
```
