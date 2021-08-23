
#Achando a maior e menor palavra de uma lista


x=['caio','caramba','lives','sabonete']


maior = max(x)
print("\nA maior palavra da lista:", maior)
maior = max(map(len,x))
print("\nQuantas letras tem a maior palavra da lista:",maior)


menor = min(x)
print("\nA menor palavra da lista :",menor)
menor = min(map(len,x))
print("\nQuantas letras tem a menor palavra da lista:",menor)
