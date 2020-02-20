# Considere uma empresa telefonica, Abaixo de 200 min cobra 0,20 Reais/min
#200-400 cobra 0,18R/min e acima de 400 cobra 0,15r/min.Calcule sua conta de telefone

minutos = int(input("Quantos minutos voce falou este mês: "))

if ( minutos < 200):
    conta = minutos * 0.20
    print("Sua conta este mês foi de ",conta,'reais')
    
if( 200 < minutos < 400 ):
    conta = minutos * 0.18
    print("Sua conta este mês foi de %.1f reais" %conta)

if( minutos <= 800 ):
    conta = minutos * 0.15
    print("Sua conta este mês foi de %.1f reais" %conta)

else:
    conta = minutos * 0.08
    print("Sua conta este mês foi de %.2f reais" %conta)

