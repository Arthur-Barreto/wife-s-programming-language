# wife-s-programming-language

Linguagem de programação baseada na minha esposa, focando em programar o dia a dia dela, com as ações que ela geralmente faz.

## Exemplo de código

```bash
HORA_DE_BRILHAR
    GRUNIDO
        TAREFA << (instagram, 1) 
        TAREFA << (se_arrumando_para_sair, 3)
        TAREFA << (soneca, 2)
        TAREFA << (brigar_com_nenem, 1)
        ENQUANTO_ELA_NAO_MUDA_DE_IDEIA TAREFA.se_arrumando_para_sair
        TO_COM_FOME
            ACAO >> (maquiagem, 60)
            ACAO >> (escolhendo_roupa, 60)
            ACAO >> (arrumando_cabelo, 60)
            HABLAR (vou_sair, 1)
        QUERO_PITDAS
        SE TAREFA.instagram
        TO_COM_FOME
            HABLAR (vou_sair, 1)
            ACAO >> (tirando_foto, 30)
            ACAO >> (postando_foto, 30)
        QUERO_PITDAS
    A_MIMIR
    GRUNIDO
        HABLAR (vou_dormir, 1)
        TAREFA << (soneca, 2)
        SE TAREFA.soneca
        TO_COM_FOME
            HABLAR (vou_comer, 1)
        QUERO_PITDAS
    A_MIMIR
SEMPRE_DIVA
```

## EBNF

PROGRAM = { BLOCK };

BLOCK = "HORA_DE_BRILHAR", "\n", { DAY }, "SEMPRE_DIVA", "\n";

DAY = "GRUNIDO", "\n", { STATEMENT }, "A_MIMIR", "\n";

STATEMENT = ( "λ" | TASK_DECLARATION | WHILE_STATEMENT | IF_STATEMENT | BLOCK_STATEMENTS), "\n";

BLOCK_STATEMENTS = "TO_COM_FOME", "\n", { BLOCK_SPECIFIC_STATEMENT }, "QUERO_PITDAS", "\n";

BLOCK_SPECIFIC_STATEMENT = ( HABLAR | ACTION_DECLARATION), "\n";

TASK_DECLARATION = "TAREFA", "<<", "(", STRING, ",", NUMBER, ")";

ACTION_DECLARATION = "ACAO", ">>", "(", STRING, ",", NUMBER, ")";

WHILE_STATEMENT = "ENQUANTO_ELA_NAO_MUDA_DE_IDEIA", CONDICIONAL, "\n", BLOCK_STATEMENTS;

IF_STATEMENT = "SE", CONDICIONAL, "\n", BLOCK_STATEMENTS;

HABLAR = "HABLAR", "(", STRING, ",", NUMBER, ")";

CONDICIONAL = "TAREFA", ".", STRING;

STRING = { CHAR };

CHAR = ( "a" | "..." | "z" | "A" | "..." | "Z" "0" | "..." | "9" | "_" | " ");

NUMBER = { DIGIT };

DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

## Diagrama Sintático

![Diagrama Sintático](diagrama.png)

## Flex/Bison e Compilação

- Para validação do `flex` e `bison`, vá para o diretório **flexBison**.
- Para compilar o código, vá para o diretório **compiler**.

## Para saber mais

Leia o pdf em anexo, que explica um pouco mais sobre a linguagem e o processo de desenvolvimento.
