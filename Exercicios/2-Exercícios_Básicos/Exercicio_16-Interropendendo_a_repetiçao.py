#Calcule a soma de numeros inteiros até ser digitado zero.

soma=0
while True:
    x=int(input('Digite o numero (0 sai):  '))
    soma=soma+x
    if(x==0):
        break
print('A soma deu: %d ' %soma)
