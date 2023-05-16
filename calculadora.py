"""
Calculadora para expressões matemáticas simples usando EBNF


Explicação do código:

A função eval_expr avalia uma expressão matemática simples.
Ela recebe uma string expr como entrada e retorna o resultado 
da expressão. A função primeiro verifica se a expressão é 
válida usando a EBNF definida na variável expr_pattern. Se a
expressão não for válida, a função levanta uma exceção ValueError.
Se a expressão for válida, a função usa a função eval do Python 
para avaliar a expressão. Se houver uma tentativa de divisão por 
zero, a função levanta uma exceção ZeroDivisionError.

A função main é a função principal que interage com o usuário. Ela 
pede ao usuário para digitar uma expressão matemática simples, chama 
a função eval_expr para avaliar a expressão e exibe o resultado.

O bloco if __name__ == '__main__': garante que a função main seja 
executada somente se o arquivo for executado diretamente, não se for 
importado como um módulo em outro arquivo.

"""

import re


def eval_expr(expr):
    """
    Avalia uma expressão matemática simples.

    Args:
        expr (str): a expressão matemática a ser avaliada.

    Returns:
        O resultado da expressão matemática.

    Raises:
        ValueError: se a expressão contiver caracteres inválidos.
        ZeroDivisionError: se houver uma tentativa de divisão por zero.
    """

    # Define a EBNF para a expressão matemática simples
    expr_pattern = r'\s*((\d+(\.\d*)?)|(\.\d+))\s*([+\-*/]\s*((\d+(\.\d*)?)|(\.\d+))\s*)*'

    # Verifica se a expressão é válida
    if not re.fullmatch(expr_pattern, expr):
        raise ValueError('Expressão inválida')

    # Avalia a expressão
    try:
        return eval(expr)
    except ZeroDivisionError:
        raise ZeroDivisionError('Divisão por zero')


def main():
    """
    Função principal que recebe a entrada do usuário e exibe o resultado da expressão.
    """

    # Recebe a entrada do usuário
    expr = input('Digite uma expressão matemática simples: ')

    # Avalia a expressão
    try:
        result = eval_expr(expr)
    except (ValueError, ZeroDivisionError) as e:
        print(f'Erro: {e}')
        return

    # Exibe o resultado da expressão
    print(f'Resultado: {result}')


if __name__ == '__main__':
    main()
