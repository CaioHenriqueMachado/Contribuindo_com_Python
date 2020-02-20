notas = {}
notas[9.12]= 'Juan'
notas[7.21]= 'Zack'

for chave in notas.keys():
    print('%s tem nota %4.2f'%(notas[chave],chave))


print(' ')
print(' EXEMPLO 2')
print(' ')

for nota, nome in notas.items():
    print('%s tem nota %4.2f'%(nome,nota))


sorted(notas)
print('\n',notas)
sorted(notas,reverse=True)
print('\n',notas)

print(' \nEXEMPLO 3\n')

for nota in sorted(notas,reverse=True):
    print('%s tem nota %4.2f'%(notas[nota],nota))
