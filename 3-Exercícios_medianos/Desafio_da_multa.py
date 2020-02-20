#Pergunte a velocidade de um carro,supondo valor inteiro.
#Caso ultrapasse 110 km/h, exiba multado. Exiba o valor da multa cobrando 5 reais por
#km ultrapassado acima de 110.

VELOCIDADE = int(input('Qual foi a velocidade que o carro chegou:  '))

if ( VELOCIDADE <= 110 ):
    print("Voce nao foi multado!!")
    
if ( VELOCIDADE > 110 ):
    print("Voce foi multado!!")
    AUX = VELOCIDADE - 110
    VALOR = AUX * 5
    print('Sua multa foi de',VALOR,'reais!!')
