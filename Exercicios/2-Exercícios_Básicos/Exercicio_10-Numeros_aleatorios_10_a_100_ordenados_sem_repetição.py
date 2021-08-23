

# GERE 15 NÚMEROS ALEATÓRIOS ENTRE 1 ATÉ 100, SENDO QUE,
# NÃO PODE TER NÚMEROS REPITIDOS E ESTEJAM EM ORDEM


import random

lista = [ ]

while (len (lista) < 15):  # len =le quantas variaveis tem na 'lista'
    x = random.randint(10,100)
    if x not in lista:              #Pergunta se o numero nao esta na lista
        lista.append(x)

#FUNÇAO DEIXA EM ORDEM CRESCENTE
lista.sort()           

print(lista)
