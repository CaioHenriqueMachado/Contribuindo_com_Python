
# AULA 2

# Variáveis


"""
Nome das variáveis:

- Podem começar com letra ou _

- O nome pode contem acentos

- Não podem conter espaços

- Não podem ser palavras reservadas
"""

# 1. Exibir texto 

# print("Olá mundo!!")
# retun: Olá mundo!!


# 2. Exibir texto em variável

teste = "Olá mundo!!"
# print(teste)
# retun: Olá mundo!!


"""
Tipos de variáveis:

Em python, não é necessário que informada seu tipo antes
de atribuir um valor para ela. A linguagem mesmo irá
determinar dependo do valor.

Para a gente entender mais, vamos usar a função "type()"
para descobrir qual o das varia
"""

# Tipos de variaveis:

# String:

teste = "Bem vindo"
assert teste == "Bem vindo"

tipo = str(type(teste))
assert tipo == "<class 'str'>"


# Inteiro:

teste = 4
assert teste == 4

tipo = str(type(teste))
assert tipo == "<class 'int'>"



# Flutuante:

teste = 4.1
assert teste == 4.1

tipo = str(type(teste))
assert tipo == "<class 'float'>"


# Lista:
    
teste = [1,2]
assert teste == [1,2]

tipo = str(type(teste))
assert tipo == "<class 'list'>"


# Tupla:
# A diferença entre as tuplas e lista é que as tuplas são imutaveis, não podem ser alteradas.

teste = (1, 2, 3, 4, 5)
assert teste == (1, 2, 3, 4, 5)

tipo = str(type(teste))
assert tipo == "<class 'tuple'>"


# Conjuntos:
# Os conjuntos não aceitam valores iguais.

teste = {1, 2, 3, 4, 4, 5}
assert teste == {1, 2, 3, 4, 5}

tipo = str(type(teste))
assert tipo == "<class 'set'>"


# Dicionario:
# É composto por chaves e valores

teste = {1:"oi"}
assert teste == {1:"oi"}

assert(teste[1] == 'oi')

tipo = str(type(teste))
assert tipo == "<class 'dict'>"



