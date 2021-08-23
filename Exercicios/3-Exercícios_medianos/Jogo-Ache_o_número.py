
#FAÇA UM JOGO NO QUAL A PESSOA DEVE ACERTAR QUAL O NÚMERO FOI GERADO PELO COMPUTADOR !!

from random import randint
chave = randint (1,100)


print("\nSeja bem vindo !!")
print("\nVamos Jogar? Descubra qual número estou pensando entre 1 e 100.")
print("\nEscolha o modo:")
print("\nFácil   - (1)")
print("\nMédio   - (2)")
print("\nDificil - (3)")


#ESCOLHA DE MODO

while True:
    modo = input("\n>>> ")
    if (modo == "1" or modo == "2" or modo == "3"):
        break
    else:
        print("Por favor, escolha um dos três modos!!")

#QUANTIDADES DE TENTATIVAS

        
if ( modo == "1" ):
    tentativas = 15
elif( modo == "2" ):
   tentativas = 10
else:
    tentativas = 6

print("\nVamos começar, você tem", tentativas, "tentativas. Boa sorte :")


while True:
    chute= int(input('Chute:  '))
    if chute == chave:
        print('Parabéns, voce é foda! Acertou o numero %d'%chave)
        break
    else:
        print('Alto' if (chute > chave) else 'Baixo')        #operador Ternario


    tentativas-=1
    if (tentativas == 0):
        print("\nVocê perdeu !!")
        print("\n O número era:",chave)
        break
    
print('\nFim de jogo!!')
