import re

# Define as regras da gramática usando a sintaxe EBNF
expr = r"(?P<expr>(?P<term>(?P<factor>(?P<number>\d+)|\((?P<expr>)\)))(?P<op1>[*/](?P<factor>(?P<number>\d+)|\((?P>expr)\)))*)"
term = r"(?P<term>(?P<factor>(?P<number>\d+)|\((?P<expr>)\)))(?P<op2>[+-](?P<factor>(?P<number>\d+)|\((?P>expr)\)))*)"
factor = r"(?P<factor>(?P<number>\d+)|\((?P<expr>)\))"
number = r"(?P<number>\d+)"


# Define uma função para avaliar uma expressão matemática
def eval_expr(match):
    expr = match.group()
    return str(eval(expr))


# Loop principal
while True:
    # Lê uma expressão matemática do usuário
    expr = input("Digite uma expressão matemática (ou 'q' para sair): ")

    # Sai do loop se o usuário digitar 'q'
    if expr.lower() == "q":
        break

    # Avalia a expressão matemática usando as regras da gramática EBNF
    expr = re.sub(
        expr,
        eval_expr,
        re.sub(
            factor, eval_expr, re.sub(term, eval_expr, re.sub(expr, eval_expr, expr))
        ),
    )

    # Imprime o resultado da avaliação da expressão matemática
    try:
        result = float(expr)
        print(f"Resultado: {result}")
    except:
        print("Erro ao avaliar a expressão.")
