
#Ordene uma pilha tendo uma outra auxiliar. Lembrando que a pilha só pode mexer no ultimo valor.


principal   = [0,0,0,0,0,0]
aux         = [0,0,0,0,0,0]
tam         = 5
pilha       = [10,5,3,4,9,1]
j = -1
k = 0

print('PILHA: ')
print(pilha)

while True:
    if ( tam == -1 ):                               #Se a pilha estiver vazia, para o código.
        break
    if ( tam == 5 ):                                #Joga o primeiro valor da pilha na principal.
        principal[k] = pilha[tam]
        pilha[tam]   = 0
        tam -= 1
        
    if ( pilha[tam] > principal[k] ):               #Se o ultimo valor da pilha for maior que o ultimo valor da principal, recorta valor e coloca na principal. 
        k += 1
        principal[k] = pilha[tam]
        pilha[tam]   = 0
        tam -=1


    if(pilha[tam] < principal[k] and tam != -1): #Se o ultimo valor da pilha for menor que o ultimo valor da principal, joga na aux.
        while (pilha [tam]< principal[k]):
            j+=1
            aux[j]=principal[k]
            principal[k]=0
            k-=1

        k+=1
        principal[k]=pilha[tam]
        pilha[tam]=0
        tam-=1
        while( j != -1):
            k+=1
            principal[k]= aux[j]
            aux[j]=0
            j-=1

print('PRINCIPAL: ' )
print(principal)        


	

