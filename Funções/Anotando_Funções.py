'''
LISTA DE FUNÇÕES QUE PODEM SER UTEIS NA HORA DE FAZER SEU CÓDIGO:

Funções:
'''

#len() - Conta a quantidade casas na string 

teste = "cai o"

resposta = len(teste)

assert(resposta == 5)
#Quando a função ASSERT não retorna nada significa que a condição dada é verdadeira.




# LISTA
lista = [12, 10, 4, 5]

# append() - Adiciona item na lista.
lista.append(1)
assert(lista == [12, 10, 4, 5, 1])


# sort() - Ordena a lista.
lista.sort()
assert(lista == [1, 4, 5, 10, 12])

# reverse() - Ordena a lista de forma reversa.
lista.reverse()
assert(lista == [12, 10, 5, 4, 1])

# pop() - Remove o ultimo da lista.
lista.pop()
assert(lista == [12, 10, 5, 4])


# CONJUNTO

# set() - Converte para conjunto ( PONTO POSITIVO: Conjunto remove duplicidade )
lista = ['peixe', 'gato', 'cachorro', 'leão', 'peixe', 'peixe']

result = set(lista)
assert(result == {'cachorro', 'gato', 'peixe', 'leão'})



conjunto1 = {12, 10, 4, 5, 1, 1, 1}
conjunto2 = {1, 2, 3, 4, 5, 6}
conjunto3 = {1, 2, 3}

assert(conjunto1 == {12, 10, 5, 4, 1})

# add() - Adiciona um numero ao conjunto
conjunto1.add(6)
assert(conjunto1 == {12, 10, 5, 4, 1, 6})

# discard() - Remove um número do conjunto
conjunto1.discard(6)
assert(conjunto1 == {12, 10, 5, 4, 1})

# union() - Retorna a união de dois conjuntos
result = conjunto1.union(conjunto2)
assert(result == {1, 2, 3, 4, 5, 6, 10, 12})

# intersection() - Retorna a intersecção de dois conjuntos
result = conjunto1.intersection(conjunto2)
assert(result == {1, 4, 5})

# difference() - Retorna a diferença do primeiro conjunto para o segundo.
result = conjunto1.difference(conjunto2)
assert(result == {10, 12})

result = conjunto2.difference(conjunto1)
assert(result == {2, 3, 6})


# difference() - Retorna a diferença simetrica, diferença dos dois conjuntos
result = conjunto1.symmetric_difference(conjunto2)
assert(result == {2, 3, 6, 10, 12})

result = conjunto2.symmetric_difference(conjunto1)
assert(result == {2, 3, 6, 10, 12})


# issubset() - Retorna se um conjunto X está contido conjunto Y
result = conjunto1.issubset(conjunto2)
assert(result == False)

result = conjunto3.issubset(conjunto2)
assert(result == True)

# issuperset() - Retorna se um conjunto X contém o conjunto Y
result = conjunto3.issuperset(conjunto2)
assert(result == False)

result = conjunto2.issuperset(conjunto3)
assert(result == True)


