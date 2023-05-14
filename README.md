# Calculadora EBNF

Este programa implementa uma calculadora que segue as regras da notação EBNF para avaliar expressões matemáticas simples. As regras EBNF definidas para a gramática da calculadora são:

```
<expr> ::= <term> ('+' <term>)*
<term> ::= <factor> ('' <factor>)
<factor> ::= <number> | '(' <expr> ')'
<number> ::= [0-9]+
```
  
  
## Como funciona?

A expressão de entrada é avaliada seguindo as seguintes etapas:

1. Os dígitos que compõem o número são lidos um a um e concatenados para formar o número inteiro correspondente.
2. Se a expressão contiver parênteses, a expressão dentro dos parênteses é avaliada primeiro.
3. A expressão é avaliada seguindo a ordem de precedência dos operadores: primeiro as multiplicação e divisão e depois as adição e subtração.
4. O resultado da expressão é retornado como um número de ponto flutuante.

A calculadora solicita ao usuário que insira uma expressão matemática para avaliar. A expressão pode conter os operadores de adição, subtração, multiplicação e divisão, além de parênteses para definir a precedência das operações. O usuário pode sair do programa a qualquer momento digitando "q" ou "Q" em vez de uma expressão matemática.

## Como usar?

1. Certifique-se de que o Python esteja instalado em seu computador.
2. Faça o download do arquivo `calculadora.py`.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo `calculadora.py` está localizado.
4. Execute o arquivo `calculadora.py` digitando `python calculadora.py`.
5. Digite uma expressão matemática quando solicitado.
6. Observe o resultado da expressão na saída do programa.
7. Repita os passos 5-6 para avaliar outras expressões ou digite "q" ou "Q" para sair do programa.

## Referências

Este projeto foi baseado nas seguintes referências:

- [Notação EBNF (Wikipedia)](https://pt.wikipedia.org/wiki/EBNF)
- [Python 3.7.3 Documentation - regras de gramática do Python](https://docs.python.org/3/reference/grammar.html)

