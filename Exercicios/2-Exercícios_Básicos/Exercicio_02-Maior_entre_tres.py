
# DESCUBRA QUAL O MAIOR NÚMERO ENTRE OS TRÊS DIGITADOS PELO USUÁRIO

print("DESCUBRA QUAL O MAIOR NÚMERO !! \n")

NUM_1 = int(input("Digite o 1° numero: "))

NUM_2 = int(input("Digite o 2° numero: "))

NUM_3 = int(input("Digite o 3° numero: "))

if (NUM_1 > NUM_2) and (NUM_1 > NUM_3):
    print('O maior é o : ',NUM_1)
    
if (NUM_2 > NUM_3):
    print('O maior é o : ', NUM_2)
    
else:
    print('O maior é o : ', NUM_3)
