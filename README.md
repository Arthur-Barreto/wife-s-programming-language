# wife-s-programming-language

Linguagem de programação baseada na minha esposa, focando em programar o dia a dia dela, com as ações que ela geralmente faz.

## Exemplo de código

```bash
hora_de_brilhar

    grunido
        tarefa >> ("instagram", 60) 
        tarefa >> ("se_arrumando_para_sair", 180)
        tarefa >> ("soneca", 120)
        tarefa >> ("brigar_com_nenem", 60)

        ENQUANTO_ELA_NAO_MUDA_DE_IDEIA tarefa.se_arrumando_para_sair:
            acao >> ("maquiagem", 60)
            acao >> ("escolhendo_roupa", 60)
            acao >> ("arrumando_cabelo", 60)

        SE tarefa.instagram:
            acao >> ("tirando_foto", 30)
            acao >> ("postando_foto", 30)
        
        ENQUANTO_ELA_NAO_MUDA_DE_IDEIA tarefa.soneca:
            acao >> ("sonha_com_nenem", 10)

        ENQUANTO_ELA_NAO_MUDA_DE_IDEIA tarefa.brigar_com_nenem:
            hablar ("tira o sapato do meio da casa", 15)
            hablar ("limpa a mesa", 15)
            hablar ("tira a toalha da cama", 15)
            hablar ("tira a roupa da maquina", 15)

    a_mimir

sempre_diva
```

## EBNF

PROGRAM = { BLOCK };

BLOCK = "hora_de_brilhar", "\n", { DAY }, "sempre_diva";

DAY = "grunido", "\n", { STATEMENT }, "a_mimir";

STATMENT = ("λ" | TASK_DECLARATION | ACTION_DECLARATION | WHILE_STATEMENT | IF_STATEMENT), "\n";

TASK_DECLARATION = "tarefa", ">>", "(", STRING, ",", NUMBER, ")" , "\n";

ACTION_DECLARATION = "acao", ">>", "(", STRING, ",", NUMBER, ")", "\n";

WHILE_STATEMENT = "ENQUANTO_ELA_NAO_MUDA_DE_IDEIA", CONDICIONAL, ":", STATEMENT, "\n";

IF_STATEMENT = "SE", CONDICIONAL, ":", STATEMENT, "\n";

CONDICIONAL = "tarefa", ".", STRING, "\n";

STRING = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ;

NUMBER = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;


## Diagrama Sintático

![Diagrama Sintático](diagrama.png)
