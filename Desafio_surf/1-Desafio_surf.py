
#EXIBINDO COMO ESTÁ NO TXT

f= open ('surf.txt')
for linha in f:
    print (linha.strip()) #.strip tira o caracter de controle que faz pular linha.
f.close()
