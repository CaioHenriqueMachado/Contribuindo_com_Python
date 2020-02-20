#TESTE DE SEQUENCIA PT2
z=1
j=0
vetor_mol=['A C T G A G A C T C A T C ', 'A A C T C T G C A C T G A C T G ']
cont=0
busca=vetor_mol[z]
busca=busca.split()
while (j != len(busca)):
    if (busca[j]=='A' and busca[j+1]=='C'and busca[j+2]=='T'and busca[j+3]=='G'):
        cont+=1
    j+=1
    z+=1
            

print('A seq. (A C T G) foi achada %d vezes'%cont)
