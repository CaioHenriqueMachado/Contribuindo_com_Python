# Leia um vetor de 10 num caracteres minusculos, e diga quantas
#consoantes foram lidas.
consoantes=0
vetor=[]
i=0

while (i<=9):
    n=(str(input('Digite um caractere: ')))     # POSSO USAR SEM O STR
    vetor.append(n)
    if vetor[i] not in 'aeiou':
           consoantes+=  1
    i+=1
print('O numero de consoantes é: ',consoantes)
