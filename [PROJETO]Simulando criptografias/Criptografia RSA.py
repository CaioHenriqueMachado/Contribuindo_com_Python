#    Criptografia RSA                 P=3; Q=11;E=7

Alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

primo=0
while( primo == 0):
    d=2
    P = int(input("Digite um valor da chave P (primo): "))
    primo=1
    while(P==1 or P==0):
        P=int(input("Digite um valor Primo correto para P: "))
    while(primo==1 and d<=P /2):
        if (P% d==0):
            primo=0
        else:
            d+=1

print("\n") 

primo=0
while( primo == 0):
    d=2
    Q= int(input("Digite um valor da chave Q (primo): "))
    primo=1
    while(Q==1 or Q==0):
        Q=int(input("Digite um valor Primo correto para Q: "))
    while(primo==1 and d<=Q /2):
        if (Q% d==0):
            primo=0
        else:
            d+=1
    
N= (P * Q)
Totiente= (P-1)*(Q-1)


primo=0
while( primo == 0):
    d=2
    E = int(input("Digite o valor de E...\nTal que : (1<E<%d ) e (E e %d sejam primos entre si): "%(Totiente,Totiente)))
    primo=1
    while(E==1 or E==0 or 1>E or E>Totiente):
        E = int(input("Digite o valor de E...\nTal que : (1<E<%d ) e (E e %d sejam primos entre si): "%(Totiente,Totiente)))
    while( d<=E /2 and primo ==1):
        y=E/2
        if (E% d==0):
            primo=0
            
        else:
            d+=1
            primo =1
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










