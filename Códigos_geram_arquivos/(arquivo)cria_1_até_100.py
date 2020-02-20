arquivo= open('numerosh.txt','w')
for linha in range(1,101):                  # de 1 até 100
    arquivo.write('%d\n' %linha)       #escreve em arquivos o num
arquivo.close()
