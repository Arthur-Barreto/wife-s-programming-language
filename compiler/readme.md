# Python Compiler

## Um pouco sobre a linguagem

`comentários` são feitos com `hummm`, se atende para usar 3 `m`'s.

## Para rodar

```bash
python3 main.py input_code.txt
```

Caso queira o log em um arquivo separado, basta rodar:

```bash
python3 main.py input_code.txt > log.txt
```

## Fatos importantes sobre o log

- O log é gerado em tempo de execução, ou seja, a cada linha de código lida.
- Sempre que um `DIA` termina, temos **==========** no final, indicando que o dia terminou, bem como as tasks daquele dia, que passam a não valer para o dia seguinte.
- Sempre entre um `CONDICIONAL`, temos ********** entre a região gerada pela condição.
- Sempre entre um `LOOP`, temos **-+--+--+--+-** entre a região gerada pelo loop.
