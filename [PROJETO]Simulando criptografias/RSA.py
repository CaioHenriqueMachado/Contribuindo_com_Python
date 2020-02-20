#    Criptografia RSA                 P=3; Q=11;E=7

Alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

P=3
Q=11
E=7
N= (P * Q)
Totiente= (P-1)*(Q-1)

for i in range(Totiente):
    if((i*E)%Totiente ==1%Totiente):
        D=i
    

print("\n Chaves Publicas: |N=%d| e |E=%d|\n Chaves Privadas: |P=%d|,|Q=%d| e |D=%d|\n"%(N,E,P,Q,D))



num=int (input("  1 <--- Criptografar\n  2 <---Descriptografar\n  0 <--- Sair: \n    "))
while (num !=0) :
    frase_digitada=input("Digite a frase:  \n")
    frase_digitada=frase_digitada.upper()
    frase_gerada='-'
    separa=''
    frase=[]
    conversor=0
    palavra=''
    
    if (num == 1 ):                                                          #<------ criptografa

        for caracter in frase_digitada:
            
            if(caracter==(chr(32))):                              
                frase_gerada+=(chr(42))+"-"                          
            else:
                resto=((((ord(caracter)-65)**E)%N))
                p=(resto+N)
                frase_gerada+=(str(p))+'-'
        print("%s"%frase_gerada)



    if (num == 2 ):                                                         #<------ descriptografa
    
        for caracter in frase_digitada:                       #<----Transforma os numeros digitados em um vetor
            
            if(caracter== chr(45)):
                x=0
                if(palavra != ""):
                    frase.append(palavra)
                    palavra=""
            else:
                palavra+=caracter


        for letra in frase:                                        #<------Pega os numeros e transforma em letras.
            if(letra==(chr(42))):
                frase_gerada+=chr(32)
            else:
                resto=(((int(letra))**D)%N)
    
                frase_gerada+=Alfabeto[resto]
                
        print("%s"%frase_gerada)
                
        




    num=int (input("  1 <--- Criptografar\n  2 <---Descriptografar\n  0 <--- Sair:\n    "))










