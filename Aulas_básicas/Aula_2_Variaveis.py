
# AULA 2

# Variáveis


"""
Nome das variáveis:

- Podem começar com letra ou _

- O nome pode contem acentos

- Não podem conter espaços

- Não podem ser palavras reservadas
"""

#Variavel com nome "teste" guardando um texto "Olá mundo!!"

teste = "Olá mundo!!"


#Exibindo na tela o que tem na variavel:

print(teste)

'''------------EXIBE TEXTO ABAIXO:
Olá mundo!!
'''

#Exibindo sem a variavel:

print("Olá mundo!!")

'''------------EXIBE TEXTO ABAIXO:
Olá mundo!!
'''


"""

Tipos de variáveis:

Em python, não é necessário que informada seu tipo antes
de atribuir um valor para ela. A linguagem mesmo irá
determinar dependo do valor.

Para a gente entender mais, vamos usar a função "type()"
para descobrir qual o das varia
"""
print("\n Tipos de variaveis: \n")


print("\nString:")
teste1 = "oi"
print(teste1)
print("\nComo a função irá mostrar:")
print(type(teste1))

print("\nInteiro:")
teste1 = 4
print(teste1)
print("\nComo a função irá mostrar:")
print(type(teste1))

print("\nFlutuante:")
teste1 = 4.1
print(teste1)
print("\nComo a função irá mostrar:")
print(type(teste1))

print("\nLista:")
teste1 = [1,2]
print(teste1)
print("\nComo a função irá mostrar:")
print(type(teste1))

print("\nDicionario:")
teste1 = {1:"oi"}
print(teste1)
print("\nComo a função irá mostrar:")
print(type(teste1))
