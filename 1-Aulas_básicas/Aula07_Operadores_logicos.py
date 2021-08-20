'''

AULA 7

OPERADORES LÓGICOS:
ORDEM DE PRECEDÊNCIA

NEGAÇÃO:          not
CONJUNÇÃO:        and
DISJUNÇÃO:        or


A ORDEM DE PRECEDÊNCIA QUE OS OPERADORES SÃO EXECUTADOS SERÁ A SEGUINTE:

1° = ()
2° = **
3° = *, / , %    (Os três contêm a mesma ordem)
4° = +, -        (Os dois contêm a mesma ordem)
5° = OPERADORES RELACIONAIS
6° = OPERADORES LÓGICOS


ATENÇÃO : OPERADORES LÓGICOS SÃO RESOLVIDOS DEPOIS DOS RELACIONAIS.

ORDEM:
1° OPERADORES ARITMETICOS.
2° OPERADORES RELACIONAIS.
3° OPERADORES LÓGICOS.

'''

#NEGAÇÃO

#EXEMPLO 1
teste = not(True)
resposta = False

assert(teste == resposta)


#EXEMPLO 2

teste = not(False)
resposta = True

assert(teste == resposta)


#CONJUNÇÃO ("and")

#EXEMPLO 1

teste = ( True and True )
resposta = True
assert(teste == resposta)

#EXEMPLO 2

teste = ( True and False )
resposta = False
assert(teste == resposta)

#EXEMPLO 3

teste = ( False and True )
resposta = False
assert(teste == resposta)

#EXEMPLO 4

teste = ( False and False )
resposta = False
assert(teste == resposta)


#DISJUNÇÃO ("or")

#EXEMPLO 1

teste = ( True or True )
resposta = True
assert(teste == resposta)

#EXEMPLO 2

teste = ( True or False )
resposta = True
assert(teste == resposta)

#EXEMPLO 3

teste = ( False or True )
resposta = True
assert(teste == resposta)

#EXEMPLO 4

teste = ( False or False )
resposta = False
assert(teste == resposta)

print("Parabens, todas estão corretas !!")

