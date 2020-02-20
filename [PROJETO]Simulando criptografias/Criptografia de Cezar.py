#             Criptografia de Cézar

Alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chave=3
num=int (input("  1 <--- Criptografar\n  2 <---Descriptografar\n  0 <--- Sair: \n    "))
while (num !=0) :
    frase_digitada=input("Digite a frase:  ")
    frase_digitada=frase_digitada.upper()
    frase_gerada=" "
    i=-1
    if (num == 1 ):                                                          #<------ criptografa

        for caracter in frase_digitada:                         # <-----  Pega caracter a caracter da frase digitada
            if(caracter==(chr(32))):                                  # <---- (Se o caracter for um espaço) Pega só os espaços
                frase_gerada+=chr(32)                             #<---- Joga os espaços na frases
            else:
                resto=(((ord(caracter)+3)%26)-13)         #<-----(Se nao for espaço ) Pega o caracter, transforma no numero, poe na formula e obtem o resto
                frase_gerada+=Alfabeto[resto]               #<----- Coloca o resto como indice para procura-lo na lista. 
        print("%s"%frase_gerada)

    if (num == 2 ):                                                         #<------ descriptografa
        
        for caracter in frase_digitada:
            if(caracter==(chr(32))):
                frase_gerada+=chr(32)
            else:
                resto=(((ord(caracter)-3)%26)-13)
                frase_gerada+=Alfabeto[resto]
                
        print("%s"%frase_gerada)




    num=int (input("  1 <--- Criptografar\n  2 <---Descriptografar\n  0 <--- Sair:\n    "))







    
