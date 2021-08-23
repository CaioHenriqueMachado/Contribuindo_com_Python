
#IMPRIMIR OS IMPARES DE 0 ATÉ O NÚMERO DIGITADO

FIM = int(input("\nDigite o ultimo numero da lista: "))

CONT = 0
NUMEROS = ""

while(CONT <= FIM):
    if  CONT%2!=0:
        NUMEROS +=str(CONT)+" " 
        
    CONT+=1

print(NUMEROS)
