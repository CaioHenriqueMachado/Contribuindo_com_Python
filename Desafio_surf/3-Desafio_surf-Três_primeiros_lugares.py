f= open ('surf.txt')
notas=[]
for linha in f:
    nome, pontos = linha.split()
    notas.append(float(pontos))
f.close()
notas.sort()        #ordena.
notas.reverse()     #poe em ord. decrescente.
print (notas[0])
print (notas[1])
print (notas[2])
