# wife-s-programming-language

Linguagem de programação baseada na minha esposa, focando em programar o dia a dia dela, com as ações que ela geralmente faz.

## Exemplo de código

```bash
hora_de_brilhar
    grunido
        tarefa << (instagram, 1) 
        tarefa << (se_arrumando_para_sair, 3)
        tarefa << (soneca, 2)
        tarefa << (brigar_com_nenem, 1)
        ENQUANTO_ELA_NAO_MUDA_DE_IDEIA tarefa.se_arrumando_para_sair
        TO_COM_FOME
            acao >> (maquiagem, 60)
            acao >> (escolhendo_roupa, 60)
            acao >> (arrumando_cabelo, 60)
        QUERO_PITIDAS
        SE tarefa.instagram
        TO_COM_FOME
            acao >> (tirando_foto, 30)
            acao >> (postando_foto, 30)
        QUERO_PITIDAS
    a_mimir
    grunido
        tarefa << (instagram, 1)
    a_mimir
sempre_diva
```

## EBNF

PROGRAM = { BLOCK };

BLOCK = "hora_de_brilhar", "\n", { DAY }, "sempre_diva", "\n";

DAY = "grunido", "\n", { STATEMENT }, "a_mimir", "\n";

STATEMENT = ("λ" | TASK_DECLARATION | ACTION_DECLARATION | WHILE_STATEMENT | IF_STATEMENT | HABLAR), "\n";

TASK_DECLARATION = "tarefa", "<<", "(", STRING, ",", NUMBER, ")", "\n";

ACTION_DECLARATION = "acao", ">>", "(", STRING, ",", NUMBER, ")", "\n";

WHILE_STATEMENT = "ENQUANTO_ELA_NAO_MUDA_DE_IDEIA", CONDICIONAL, "\n", BLOCK;

IF_STATEMENT = "SE", CONDICIONAL, "\n", BLOCK;

HABLAR = "hablar", "(", STRING, ",", NUMBER, ")", "\n";

CONDICIONAL = "tarefa", ".", STRING;

STRING = {CHAR};

CHAR = ("a" | ... | "z" | "A" | ... | "Z" | "0" | ... | "9" | "_" | " ");

NUMBER = {DIGIT};

DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

BLOCK = "{", "\n", { STATEMENT }, "}", "\n";

## Diagrama Sintático

![Diagrama Sintático](diagrama.png)
