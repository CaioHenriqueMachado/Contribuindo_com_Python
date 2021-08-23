## faça um programa que leia uma palavra e troque as vogais por'*'

palavra=input('Digite uma palavra: ')

k=0
troca=' '
while k< len(palavra):
    if palavra[k] in 'aeiou':
        troca += '*'
    else:
        troca= troca + palavra [k]
    k+= 1

print('Nova palavra %s' %troca)
