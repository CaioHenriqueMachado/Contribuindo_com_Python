arquivo = open ('antigo.txt')

lista = []
lista1 = []
palavra = ''
for linha in arquivo:
    ajustada = linha.replace('::VARCHAR(50)','')
    lista.append(ajustada)



novo = open ('novo.txt','w')
for linha in lista:                  
    novo.write('%s\n' %linha)       
novo.close()
