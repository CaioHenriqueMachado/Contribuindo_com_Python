# Faça um programa que leia um veor de dez numeros reais e mostre-os na ordem
#inversa.
i=0
vetor=[]
while (i<= 9):
    vetor.append(int(input('Digite  10 numeros para o vetor :  ')))
    i+=1
print('Vetor normal: ',vetor)
print('O vetor inversamente:  ')
i=9
while(i>=0):
    print(vetor[i])
    i-=1
