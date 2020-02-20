'''

AULA 6

OPERADORES RELACIONAIS:
ORDEM DE PRECEDÊNCIA:

MAIOR:          >
MENOR:          <
MAIOR IGUAL:    >=
MENOR OU IGUAL: <=
IGUAL:          ==
DIFERENTE:      !=

A ORDEM DE PRECEDÊNCIA QUE OS OPERADORES SÃO EXECUTADOS SERÁ A SEGUINTE:

1° = ()
2° = **
3° = *, / , %    (Os três contêm a mesma ordem)
4° = +, -        (Os dois contêm a mesma ordem)
5° = OPERADORES RELACIONAIS


ATENÇÃO : OPERADORES RELACIONAIS SÃO RESOLVIDOS DEPOIS DOS ARITMETICOS.

ORDEM:
1° OPERADORES ARITMETICOS.
2° OPERADORES RELACIONAIS.


'''

#MAIOR

teste = 5 > 2
resposta = True
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#MENOR

teste = 5 < 2
resposta = False
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#MAIOR OU IGUAL

teste = 8 >= 8
resposta = True
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#MENOR OU IGUAL

teste = 9 <= 8
resposta = False
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#IGUAL

teste = (5 == 2)
resposta = False
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

#DIFERENTE

teste = 5 != 2
resposta = True
assert(teste == resposta)
#Se ASSERT não retorna nada significa que a condição dada é verdadeira.

print("Parabens, todas estão corretas !!")

