arquivo= open('numerosh.txt','r')#opção de leitura
for linha in arquivo.readlines():   #cria uma lista onde cada elemento é uma linha
    print(linha)                                #for pega cada linha do arquivo e imprime.
arquivo.close()
