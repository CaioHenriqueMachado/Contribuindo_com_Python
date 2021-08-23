# COMANDO FOR E WHILE

#FOR
print("\n1º EXEMPLO - FOR:")
for letra in 'AEIOU':
    print (letra)
    
print("\n2º EXEMPLO - FOR:")
for i in range(5):
    print(i)
    
print("\n3º EXEMPLO - FOR:")
for x in ['cpoe', 42, 3.14]:
    print (x)


print("\n4º EXEMPLO - FOR:")    
cabe=['ADCFGD','QWQWQWQ']
for i in cabe[0]:
    print(i)

print("\n5º EXEMPLO - FOR:")
for i in cabe:
    print(i)



#WHILE

print("\n1º EXEMPLO - WHILE:")
texto = 'aeiou'
k = 0

while (k < len(texto)):
    letra = texto[k]
    print(letra)
    k = k + 1


print("\n2º EXEMPLO - WHILE:")
lista = list(range(5))
k = 0

while k < len(lista):
        i = lista[k]
        print(i)
        k = k + 1

print("\n3º EXEMPLO - WHILE:")
lista = ['cpoe', 42, 3.14]
k = 0

while k < len(lista):
        x = lista[k]
        print(x)
        k = k + 1
