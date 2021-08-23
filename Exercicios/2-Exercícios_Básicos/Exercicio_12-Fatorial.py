

#CALCULADORA DE FATORIAL


num = int(input('\nDigite um numero para obter seu fatorial:\n'))
i = 2
fatorial = 1
expressão = '( 1'

while (i <= num):
    fatorial*=i
    expressão +="* " + str(i)
    i+=1
     


expressão+= " ) = "+ str(fatorial)
print(expressão)
print('\nO fatorial de ',num,' é :',fatorial)
