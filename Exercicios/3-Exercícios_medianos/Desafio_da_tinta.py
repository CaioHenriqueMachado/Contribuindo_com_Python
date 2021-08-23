'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1
litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam RS 80,00.
    Informe ao usuario a quantidade de latas de tinta a serem compradas e o preço total.
    OBS: Somente são vendidos um numero inteiro de latas.
'''

METROS = int(input('Metros:  '))

if (METROS% 54 != 0):
    LATAS = int(METROS/54)+1

else:
    LATAS = METROS/54

VALOR = LATAS*80
print('%d latas a um custo de %.2f !! ' %(LATAS,VALOR ))
    
