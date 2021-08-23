
#FAÇA A MÉDIA DE 10 NÚMEROS DIGITADOS PELO USUARIO

NUMERO     = 0
QUANTIDADE = 1 
SOMA  = 0
MEDIA = 0


while(QUANTIDADE <= 10):
    NUMERO = int(input("Digite o %d° numero: "%QUANTIDADE))
    QUANTIDADE += 1
    SOMA += NUMERO

    
MEDIA=SOMA/10
print("A média desses 10 numeros é: ",MEDIA)
