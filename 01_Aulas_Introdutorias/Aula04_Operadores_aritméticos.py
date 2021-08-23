'''

AULA 4

OERADORES MATEMATICOS:
SOMA            = +
SUBTRAÇÃO       = -
MULTIPLICAÇÃO   = *
DIVISÃO REAL    = /
DIVISÃO INTEIRA = %
EXPONENCIAÇÃO   = **


A ORDEM DE PRECEDÊNCIA QUE OS OPERADORES SÃO EXECUTADOS SERÁ A SEGUINTE:

1° = ()
2° = **
3° = *, / , %    (Os três contêm a mesma ordem)
4° = +, -        (Os dois contêm a mesma ordem)



IMAGINANDO QUE VOCÊ IRÁ RESOLVER A SEGUINTE EXPRESSÃO:

= ( 1 + 2**2 ) * 2 -1
= ( 1 + 4 ) * 2 -1
= 5 * 2 - 1
= 10 - 1
= 9
OBS: Testado no ultimo exemplo.
'''

#SOMA

teste = 5 + 2
resposta = 7
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#SUBTRAÇÃO

teste = 5 - 2
resposta = 3
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#MULTIPLICAÇÃO

teste = 5 * 2
resposta = 10
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#DIVISÃO REAL

teste = 5 / 2
resposta = 2.5
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#DIVISÃO INTEIRA

teste = 5 % 2
resposta = 1
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#EXPONENCIAÇÃO

teste = 5 ** 2
resposta = 25
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#EXPRESSÃO FEITO NO INICIO

teste = ( 1 + 2**2 ) * 2 -1
resposta = 9
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.


print("Parabens, todas estão corretas !!")

