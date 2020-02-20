import random

class Replicação_de_DNA:

    def __init__( self , mol , tam ):
        self.mol=mol
        self.tam=tam
#Função 1 -------------------------------------------------------------------------------------------------------------------------------------------------
    def gera_mol( self ):
        geradas=[]
        for i in range(self.mol) :
            bases=["A","T","C","G"]
            sequencia=""
            k=0
            while k<self.tam:
                sequencia+=bases[random.randint(0,3)]
                k+=1
            #print(sequencia)                              #Talvez sairá
                
            geradas.append(sequencia)       # Armazenamento de moleculas geradas.
        return geradas
#Função 2 -------------------------------------------------------------------------------------------------------------------------------------------------
    def mutação( self , gerada , taxa ):
        self.gerada=gerada
        self.taxa=taxa
        bases=["A","T","C","G"]
        novas_moleculas=[]
        
        for j in self.gerada:
            mutação=''
            for i in j:
                mutada=''
                x=random.randint(0,100)
                if (x >= self.taxa):
                    mutação+= i
                else:
                    mutada=bases[random.randint(0,3)]
                    while( i == mutada):
                        mutada=bases[random.randint(0,3)]
                    mutação+=mutada
            #print('mutada=%s'%mutação)                              #Talvez sairá           
            novas_moleculas.append(mutação)   # Armazenamento de moleculas mutadas.
        return novas_moleculas            
#Função 3 -----------------------------------------------------------------------------------------------------------------------------------------------------
    def d_hamming(self , gerada , mutada ):
        self.gerada=gerada
        self.mutada=mutada
        distancia=[]
        for gene1 , gene2 in zip (self.gerada , self.mutada) :
            cont=sum(ch1 != ch2 for ch1, ch2 in zip(gene1, gene2))
            distancia.append(cont)
        return distancia
 #Função 4 -----------------------------------------------------------------------------------------------------------------------------------------------------
    def busca(self, molecula):
        self.molecula=molecula
        filtro=[]
        total=0
        separa=[]
        for busca in self.molecula[0]:
            separa.append(busca)
                
        for gene in self.molecula:
            j=0                                                            
            cont=0
            while (j+4 != len(separa)):
                if (gene[j:j+1]=='A' and gene[j+1:j+2]=='C'and gene[j+2:j+3]=='T'and gene[j+3:j+4]=='G'):
                    cont+=1
                j+=1
            filtro.append(cont)
        return filtro
        
#Função Principal  --------------------------------------------------------------------------------------------------------------------

mol=int(input('\nQuantidade de molécula:'))
tam=int(input('\nTamanho da molécula:'))
taxa=int(input('\nDigite a taxa de mutação:'))
DNA=Replicação_de_DNA(mol ,tam)

gerados=DNA.gera_mol()                            # Armazenamento de moleculas geradas.

mutados=DNA.mutação(gerados,taxa)    # Armazenamento de moleculas geradas.
print(gerados)
print(mutados)
distancia=DNA.d_hamming(gerados, mutados)
print(distancia)
filtro=DNA.busca(gerados)
print(filtro)













