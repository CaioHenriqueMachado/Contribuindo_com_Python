def distancia_hamming(s1, s2):
    assert len(s1) == len(s2)                      #assert = Caso a condição nao for cumprida da erro no código
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))



#Reformulado
def Distancia_hamming(s1,s2):
    cont=0
    for letra1,letra2 in zip(s1,s2):
        if(letra1 != letra2):
            cont+=1
    return cont
              
