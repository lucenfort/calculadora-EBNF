## Atividade Avaliativa: Criar produções com as regras de 1 a 4 e gerar o EBNF:


Regras:

1. A produção deve começar com um não-terminal.
2. As produções podem ter zero ou mais terminais ou não-terminais.
3. Cada produção deve terminar com um símbolo de fim de linha.
4. As produções podem ter comentários começando com o caractere '#' e terminando com um fim de linha.

Passo 1: Especificação da sintaxe da produção
O primeiro passo na criação de uma produção é especificar a sintaxe que será utilizada. Nesse caso, foram usadas duas produções como exemplo:

Aqui, as produções foram especificadas usando uma notação próxima à usada em gramáticas formais. Cada produção começa com um não-terminal, seguido de '::=', que significa "é definido como". Em seguida, vêm as alternativas, separadas por '|'. As produções terminam com um símbolo de fim de linha.

Passo 2: Criação da EBNF
O próximo passo é criar a EBNF a partir da especificação da sintaxe. A EBNF é uma notação que descreve a gramática de uma linguagem de forma mais precisa e formal do que a notação usada nas produções.

Para criar a EBNF, primeiro é necessário identificar os não-terminais e os terminais em cada produção. Os não-terminais são indicados por ângulos ('<' e '>'), enquanto os terminais podem ser representados por símbolos literais ou aspas ('"').

Em seguida, é necessário usar os símbolos da EBNF para representar as regras de produção. Por exemplo, '|' é usado para indicar alternativas e ',' é usado para indicar concatenação.

Por fim, é necessário indicar quais regras de produção são opcionais ou repetitivas. Por exemplo, a regra (expr)? indica que a expressão pode aparecer zero ou uma vez.



# Produção 1

```
1. <expr> ::= <term> '+' <expr>
             | <term> '-' <expr>
             | <term>
```
> Esta é uma produção para expressões matemáticas simples


## EBNF:

```
expr = term , ( "+" | "-" ) , expr | term .
term = ( <nonterminal> | <terminal> ) , term .
```

# Produção 2

```
1. <statement> ::= 'if' <expression> ':' <block> 'else' ':' <block> '\n'
                  | 'while' <expression> ':' <block> '\n'
```

> Esta é uma produção para estruturas de controle em uma linguagem de programação


## EBNF: 

```
statement = ( "if" , expression , ":" , block , "else" , ":" , block , eol )
          | ( "while" , expression , ":" , block , eol ) .
expression = <nonterminal> | <terminal> .
block = <nonterminal> | <terminal> .
eol = "\n" .
```
> Para o EBNF, os não-terminais devem ser indicados por ângulos e os terminais por aspas ou símbolos literais. Além disso, o símbolo '|' é usado para indicar alternativas e o símbolo ',' é usado para indicar concatenação. As EBNFs seguem as regras estabelecidas, com cada regra começando com um não-terminal, usando símbolos adequados para representar a gramática e indicando opções ou repetições conforme necessário.



#### Produção 'expr'
```
+------------+
|    expr    |
+------------+
     /  \
  term   ( '+' | '-' ) term
     \  /
```

#### Produção 'term'
```
+------------+
|    term    |
+------------+
     /  \
  factor ( '*' | '/' ) factor
     \  /

```
#### Produção 'factor'
```
+------------+
|   factor   |
+------------+
     /  \
  number  |  '(' expr ')'
     \  /
```

#### Produção 'number'
```
+------------+
|   number   |
+------------+
     /  \
  int  |  float
     \  /
```

