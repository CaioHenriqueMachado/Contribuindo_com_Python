
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

# CRIAR APENAS UM ARQUIVO 
#https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python?gclid=CjwKCAjwgviIBhBkEiwA10D2j5i1hewT55M0nXEqVlKAMneweMd6ngkrjhB2giZThN4_4EcD96gKwRoCB8cQAvD_BwE


# Exemplo 0:

teste = dict(nome = 'Caio', Idade = 20, cor = 'Pardo')

assert( teste == {'nome': 'Caio', 'Idade': 20, 'cor': 'Pardo'})


# Exemplo 1:

teste = {1:"oi"}
assert teste == {1:"oi"}

assert(teste[1] == 'oi')

tipo = str(type(teste))
assert tipo == "<class 'dict'>"

# Exemplo 2:

teste = {}

teste['a'] = 'alpha'
teste['o'] = 'omega'
teste['g'] = 'gama'

assert (teste == {'a': 'alpha', 'o': 'omega', 'g': 'gama'})

# print (teste.items())
# return: dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gama')])

# print(teste.keys())
# return: dict_keys(['a', 'o', 'g'])

#print(teste.values())
# return: dict_values(['alpha', 'omega', 'gama'])

assert (teste['a'] == 'alpha')

# Imprime todas as chaves:
result = []
for chave in teste: result.append(chave)

assert(result[0] == 'a')
assert(result[1] == 'o')
assert(result[2] == 'g')


# Imprime todos os valores nas chaves:
result = []
for chave in teste: result.append(teste[chave])

assert(result[0] == 'alpha')
assert(result[1] == 'omega')
assert(result[2] == 'gama')

# Exemplo 3:
notas = { 9.12: 'Juan', 7.21:'Zack' }


# caso 1:
result = []
for chave in notas.keys():
    result.append('%s tem nota %4.2f' %(notas[chave],chave))

assert(result[0] == 'Juan tem nota 9.12')
assert(result[1] == 'Zack tem nota 7.21')

# caso 2:
result = []
for nota, nome in notas.items():
    result.append('%s tem nota %4.2f' %(nome,nota))

assert(result[0] == 'Juan tem nota 9.12')
assert(result[1] == 'Zack tem nota 7.21')

# caso 3: 
result = []
for nota in sorted(notas):
    result.append('%s tem nota %4.2f'%(notas[nota],nota))

assert(result[0] == 'Zack tem nota 7.21')
assert(result[1] == 'Juan tem nota 9.12')


# caso 4:
assert( sorted(notas) == [7.21, 9.12] )
assert( sorted(notas, reverse = True) == [9.12, 7.21] )

assert( sorted(notas.items()) == [(7.21, 'Zack'), (9.12, 'Juan')] )
assert( sorted(notas.items(), reverse = True) == [(9.12, 'Juan'), (7.21, 'Zack')] )
