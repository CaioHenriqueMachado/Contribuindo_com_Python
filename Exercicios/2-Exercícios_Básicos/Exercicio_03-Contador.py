
# IMPRIMA DE 1 ATÉ O NÚMERO DIGITADO



FIM = int(input("\nDigite o ultimo numero da lista: "))

CONT = 1
NUMEROS = ""

while(CONT <= FIM):
    NUMEROS +=str(CONT)+" " 
    CONT +=1

print(NUMEROS)
