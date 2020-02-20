#TEVE O USO DO DICIONARIO POIS SE FIZESSE IGUAL AO PROGRAMA PASSADO
# O NOME NAO BATERIA COM A NOTA 
f= open ('surf.txt')
notas={}

for linha in f:
    nome, pontos = linha.split()
    notas[float(pontos)]=nome

f.close()

for nota in sorted(notas, reverse= True):
    print ('%s tem nota %4.2f' %(notas[nota], nota))

