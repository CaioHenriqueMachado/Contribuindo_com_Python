#TESTE DE PROCURA DE SEQUENCIA. PT1
texto= ['A','C','T','G','C','G','T','A','C','A','T','T','G','C','A','C','T','G']


cont=0
print(texto)
i=0
while (i != len(texto)):
    if (texto[i]=='A' and texto[i+1]=='C'and texto[i+2]=='T'and texto[i+3]=='G'):
        cont+=1
    i+=1

print(cont)



molecula=['A C T G A T A C G A T C A G G A C T ']
    

molecula=molecula[0].split()
print(molecula)

cont=0

i=0
while (i != len(molecula[0])):
    if (molecula[i]=='A' and molecula[i+1]=='C'and molecula[i+2]=='T'and molecula[i+3]=='G'):
        cont+=1
    i+=1

print(cont)

