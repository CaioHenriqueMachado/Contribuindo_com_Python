import random
nomes='Ana Carol Beatriz Janaina Sabrina'.split()
nomes.sort()            # Coloca em ordem crescente.
print(' '.join(nomes))
sorteado=random.choice(nomes)
chute=' '
while chute != sorteado:
    chute= input ('Chute:  ')
    if chute == sorteado:
        print('Parabéns!')
    elif chute> sorteado:
        print ('Alto')
    else:
        print('Baixo')
        
