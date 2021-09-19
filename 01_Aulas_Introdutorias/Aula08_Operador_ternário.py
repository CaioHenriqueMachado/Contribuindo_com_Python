'''

AULA 8

OPERADOR TERNÁRIO

EM PYTHON NÃO EXISTE ALGO ESPECIFICO PARA ESTE CASO,
PORÉM PODE SER FEITO DO SEGUNTE MODO:

EXPRESSÃO CONDICIONAL:

(EXPRESSÃO1) IF (CONDIÇÃO) ELSE (EXPRESSÃO2)

OU:

OPERADORES BOOLEANOS:

(CONDIÇÃO) AND (EXPRESSÃO1) OR (EXPRESSÃO2)

'''


#EXEMPLO 1- EXPRESSÃO CONDICIONAL:


media = 6

nota = 7

teste = ( "APROVADO" if (nota >= media) else "REPORVADO")

resposta = "APROVADO"

assert(teste == resposta)


#EXEMPLO 2- OPERADORES BOOLEANOS:

media = 6

nota = 5

resposta = "REPROVADO"


teste = ( (nota >= media) and "APROVADO" or "REPROVADO")
assert(teste == resposta)
# OU

# Mais usual
teste = "APROVADO" if (nota >= media) else "REPROVADO"
assert(teste == resposta)

print("Parabens, todas estão corretas !!")

